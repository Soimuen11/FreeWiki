---
layout: default
title: Linux Sysadmin
description: Cheatsheets containing Bash commands and oneliners
---

* [Bash Commands & Oneliners](#bash-commands-and-oneliners)
	* [SCSI Devices](#scsi-devices)
	* [Disks and Partitions](#disks-and-partitions)
	* [Journalctl](#journalctl)
	* [Multipathing](#multipathing)
	* [Scan Crontab](#scan-crontab)
	* [Check lsof via For Loop](#check-lsof-via-for-loop)
	* [TBS](#tbs)
	* [Disk Space Usage](#disk-space-usage)
	* [Kernel Modules, Filesystem Checks and Memory Errors](#kernel-modules-filesystem-checks-and-memory-errors)
	* [Backups and File Searches](#backups-and-file-searches)
	* [Searching Shell History of All Users](#searching-shell-history-of-all-users)
	* [History](#history)
	* [TMUX](#tmux)
	* [RPM and DNF](#rpm-and-dnf)
	* [SNMP](#snmp)
	* [SELinux](#selinux)
	* [SUSE Linux](#suse-linux)
	* [Firewall Management](#firewall-management)
	* [Firewalld](#firewalld)
	* [UFW](#ufw)
	* [IPTables](#iptables)
	* [Networking](#networking)
	* [GRUB](#grub)
	* [Managing Daemons](#managing-daemons)
	* [Clean Up /boot](#clean-up-boot)
	* [LVM](#lvm)
	* [User Management](#user-management)
	* [ACLs (Access Control Lists)](#acls-access-control-lists)
	* [Keyboard Layouts](#keyboard-layouts)

## Bash Commands and Oneliners

### SCSI Devices

Scan and list the connected SCSI devices (requires the `lsscsi` package).

```bash
lsscsi
```

List SCSI devices as `device - SCSI address`, using the `scsi_device` entries in sysfs.

```bash
ls -ld /sys/block/sd*/device/scsi_device/* | awk -F '[/]' '{print $4,"- SCSI",$7}'
```

Same output, using the `scsi_disk` entries in sysfs.

```bash
ls -ld /sys/block/sd*/device/scsi_disk/* | awk -F '[/]' '{print $4,"- SCSI",$7}'
```

Raw listing of the `scsi_device` entries (device to SCSI address mapping).

```bash
ls -ld /sys/block/sd*/device/scsi_device/*
```

Raw listing of the `scsi_disk` entries.

```bash
ls -ld /sys/block/sd*/device/scsi_disk/*
```

Rescan all SCSI hosts after adding a new disk (run as root).

```bash
for x in $(ls /sys/class/scsi_host/); do echo "- - -" > "/sys/class/scsi_host/${x}/scan"; done
```

Rescan SCSI disks after increasing the size of a disk on the hypervisor side — **RHEL and Debian systems** (run as root).

```bash
for x in $(ls /sys/class/scsi_disk/); do echo "- - -" > "/sys/class/scsi_disk/${x}/device/rescan"; done
```

Rescan SCSI devices after increasing the size of a disk on the hypervisor side — **Oracle Linux systems** (run as root).

```bash
for x in $(ls /sys/class/scsi_device/); do echo "- - -" > /sys/class/scsi_device/${x}/device/rescan; done
```

### Disks and Partitions

Grow a physical partition (`growpart` is provided by the `cloud-utils-growpart` package). Replace `/dev/sdX` with the disk and `partnumber` with the partition number.

```bash
sudo growpart /dev/sdX partnumber
```

Same as above, forcing the C locale (workaround if `growpart` fails because of the system language). See [this thread](https://forum.ubuntu-fr.org/viewtopic.php?id=2047783).

```bash
LC_ALL=C sudo growpart /dev/sdX partnumber
```

List block devices with their UUID and mount point.

```bash
lsblk -o NAME,UUID,MOUNTPOINT
```

Get the WWNs of the physical disks (on a physical server).

```bash
ls -ldt /dev/disk/by-id/wwn-*
```

Get detailed information about a disk.

```bash
smartctl -i /dev/sdX
```

### Journalctl

List the boots recorded in the journal.

```bash
journalctl --list-boots
```

Show the journal entries within a given time window.

```bash
journalctl --since "2025-04-02 00:00:00" --until "2025-04-02 00:30:00"
```

### Multipathing

List the HBA (Host Bus Adapter) cards.

```bash
ls -ld /sys/class/fc_host/host*
```

Rescan all multipath devices on **Red Hat Linux** (run as root).

```bash
for x in $(ls /sys/block) ; do echo 1 > /sys/block/${x}/device/rescan ; done
```

Rescan all multipath devices on **Oracle Linux** (run as root).

```bash
for x in $(ls -d /sys/block/sd*) ; do echo 1 > ${x}/device/rescan ; done
```

### Scan Crontab

Show the crontab of every user declared in `/etc/passwd`.

```bash
for user in $(cat /etc/passwd | awk -F ':' '{print $1}'); do crontab -l -u $user; done
```

Show the crontab of the current user.

```bash
crontab -l -u $USER
```

### Check lsof via For Loop

List the PIDs of processes holding open files on `/var` (excluding the noise from `lsof`, `grep`, `bash` and the header line).

```bash
for PID in $(lsof +L1 /var | egrep -v "lsof|grep|bash|PID" | awk '{print $2}'); do echo "$PID"; done
```

List the PIDs of processes holding **deleted** files open on `/var` (typical cause of "disk full but nothing to delete").

```bash
for PID in $(lsof +L1 /var | grep "deleted" | awk '{print $2}'); do echo "$PID"; done
```

Kill the processes holding deleted files open on `/var` to release the disk space. Use with care: this kills the processes immediately.

```bash
for PID in $(lsof +L1 /var | grep "deleted" | awk '{print $2}'); do kill -9 "$PID"; done
```

Show the 15 most CPU-consuming processes.

```bash
ps -eo user,comm,pid,ppid,pcpu,%mem --sort -pcpu | head -n 15
```

Show the most resource-consuming processes on **AIX**.

```bash
ps aux | head -1; ps aux | sort -rn | head
```

Show the processes attached to a directory.

```bash
lsof +D /var/log
```

### TBS

Check whether Secure Boot is enabled: if the directory `/sys/firmware/efi` exists, the system booted in UEFI mode, otherwise it did not.

```bash
ls -d /sys/firmware/efi
```

Check the Secure Boot state with `mokutil` (install the package first; available on Red Hat).

```bash
mokutil --sb-state
```

Count the number of processors.

```bash
grep -c processor /proc/cpuinfo
```

Count the number of processors (alternative).

```bash
nproc
```

Show the current runlevel (equivalent to the default systemd target).

```bash
who -r
```

Show the default systemd target.

```bash
systemctl get-default
```

### Disk Space Usage

Quickly find what is eating up your disk space: size of each entry under `/var`.

```bash
du -msh /var/*
```

Show the size of each top-level directory on the root filesystem only, excluding the listed directories.

```bash
du -chx --max-depth 1 --exclude=/{proc,sys,dev,home,var,tmp,apps,manh,autosys,logs,batchs} /
```

Show the size of each top-level directory on the root filesystem, excluding `/proc`, `/sys` and `/dev`.

```bash
du -chxd 1 --exclude=/{proc,sys,dev} /
```

Show the size of each directory under `/opt`, excluding `Passerelle` and `pts22`.

```bash
du -chxd 1 /opt --exclude={Passerelle,pts22}
```

Show the size of each directory under `/opt`.

```bash
du -chxd 1 /opt
```

Top 10 biggest entries at the root. Permission errors are hidden so the output stays clean.

```bash
du -sh /* 2>/dev/null | sort -rh | head -10
```

Interactive disk usage analyzer (requires the `ncdu` package).

```bash
ncdu
```

### Kernel Modules, Filesystem Checks and Memory Errors

Load a kernel module (use `-r` to remove it).

```bash
modprobe [-r] $modulename
```

Display information about a kernel module.

```bash
modinfo $modulename
```

Check and repair a filesystem (ext2/3/4 with `fsck`, XFS with `xfs_repair`). The filesystem must be unmounted.

```bash
fsck /dev/sdXN
xfs_repair /dev/sdXN
```

Look for Out Of Memory (OOM killer) events in the kernel ring buffer.

```bash
dmesg -T | grep -i "Out of memory"
```

Look for Out Of Memory events in the system logs (`/var/log/messages` on Red Hat, `/var/log/syslog` on Debian). Memory overcommit is tuned in `/etc/sysctl.conf`.

```bash
grep -i "Out of memory" /var/log/messages
```

Introspect and monitor the D-Bus bus.

```bash
busctl monitor
```

### Backups and File Searches

Create a compressed archive of a user's home directory, named after the user and the date (`ddmmyyyy`).

```bash
tar zcvf /root/_SAV/${USER}_$(date +%d%m%Y).tar.gz /home/${USER}
```

List the files modified in the last 5 days with their size in MB.

```bash
find / -xdev -type f -mtime -5 -exec du -m {} \;
```

List the files that contain the word `boot` in the history files under `/home`.

```bash
find /home/ -type f -name "*_history" -exec grep -l boot {} \;
```

Count the number of files per top-level directory, sorted by count.

```bash
find . -xdev -type f | cut -d "/" -f 2 | sort | uniq -c | sort -n
```

### Searching Shell History of All Users

Search the history of every login user for a keyword (here `dmmigrate`), using `su`.

```bash
for user in $(egrep -v "false|nologin|/dev/null" /etc/passwd | awk -F ":" '{print $1}'); do echo "checking history for $user:" && su -c "history | grep dmmigrate" $user || echo "found nothing"; done
```

Same search, using `sudo -u`.

```bash
for user in $(egrep -v "false|nologin|/dev/null" /etc/passwd | awk -F ":" '{print $1}'); do echo "checking history for $user:" && sudo -u $user "history | grep dmmigrate"; done
```

### History

Delete a specific line from the shell history.

```bash
history -d $line_number
```

Wipe the first 1000 lines of the shell history.

```bash
for num in $(seq 1 1000); do history -d $num; done
```

### TMUX

List the existing tmux sessions.

```bash
tmux list-sessions
```

Create a new tmux session.

```bash
tmux new-session
```

Rename a session.

```bash
tmux rename-session -t $target_session $new_name
```

Attach to an existing session (here named `myspace`).

```bash
tmux attach -t myspace
```

Show the pane numbers, then press the number of the pane you want to select (key binding, inside tmux).

```bash
ctrl + b + q
```

Enable mouse support: add this line to `~/.tmux.conf`.

```bash
set -g mouse on
```

### RPM and DNF

List all installed packages.

```bash
rpm -qa
```

Show information about an installed package (useful to know its version).

```bash
rpm -qi $package_name
```

Show the version of an installed package (example with `systemd`).

```bash
rpm -qi systemd | grep Version
```

Check the installation date of a system (look at the `Install Date` of the `basesystem` package).

```bash
rpm -qi basesystem
```

Install a package from an optional repository (Oracle Linux 7 example).

```bash
yum --enablerepo=ol7_optional_latest install systemd-networkd
```

Install a package from the EPEL repository.

```bash
dnf --enablerepo=epel install $package_name
```

Install a package from the `extras` repository.

```bash
dnf --enablerepo=extras install $package_name
```

Apply only the critical security updates and log the output to a dated file.

```bash
/usr/bin/yum update --security --sec-severity=Critical -y &> /root/maj-sec-critical-$(date +%y%m%d).log
```

Get a list of all orphaned packages (packages that nothing depends on).

```bash
package-cleanup --leaves
```

Remove all orphaned packages. Equivalent of `apt autoremove`.

```bash
yum remove $(package-cleanup --leaves)
```

Update packages, keeping the old (obsolete) ones. On `yum`, `update` preserves obsolete packages.

```bash
yum update
```

Upgrade packages, deleting the older (obsolete) ones. On `dnf`, `update` and `upgrade` are aliases.

```bash
yum upgrade
```

Downgrade a package to the previous version.

```bash
dnf downgrade $packagename
```

Roll back a package or version update (transaction ID taken from `dnf history`). Take a snapshot first!

```bash
dnf history undo $transaction_id
```

Show the history of transactions and the details of one of them.

```bash
dnf history info $transaction_id
```

List all the dependencies of a package. Equivalent of `apt depends packagename`.

```bash
dnf deplist $packagename
```

### SNMP

Translate an SNMP object name into its numeric OID.

```bash
snmptranslate -On SNMPv2-MIB::system.sysUpTime
```

Walk the whole SNMP tree of a host using SNMPv1 and the `public` community.

```bash
snmpwalk -c public -v1 localhost
```

Same, paginated with `less`.

```bash
snmpwalk -c public -v1 localhost | less
```

Walk the SNMP tree using SNMPv3 with authentication and privacy (user `LogPoint`, SHA-256 / AES-128).

```bash
snmpwalk -v3 -u LogPoint -l authPriv -a SHA-256 -A "authmdp" -x AES-128 -X "privatepass" localhost
```

### SELinux

SELinux modes: `enforcing` = enabled; `permissive` = disabled but logs the activity; `disabled`. Show the current status and mode:

```bash
sestatus
getenforce
```

Set SELinux to permissive mode (temporary, until the next reboot).

```bash
setenforce 0
```

Enable SELinux enforcing mode (temporary, until the next reboot).

```bash
setenforce 1
```

For a permanent change, edit `/etc/selinux/config` and set `SELINUX=enforcing`, `permissive` or `disabled`.

```bash
vi /etc/selinux/config
```

List the SELinux labels (contexts) of a directory.

```bash
ls -lZ $dirname
```

Manage SELinux policy settings (ports, file contexts, booleans, ...).

```bash
semanage
```

List all SELinux booleans.

```bash
getsebool -a
```

List all SELinux booleans with their description (via `semanage`).

```bash
semanage boolean -l
```

Turn a boolean on or off persistently (`-P`).

```bash
setsebool -P boolean_name on|off
```

Change the SELinux context of a file or directory.

```bash
chcon
```

### SUSE Linux

Refresh the repositories and list the available updates.

```bash
zypper refresh && zypper list-updates
```

Remove a package (short form: `zypper rm`).

```bash
zypper remove package
```

Install a package. Tip: `nss-resolve` is needed for systemd-resolved and `systemd-network` for networkd.

```bash
zypper install packagename
```

Show information about a package (check whether it is installed or not).

```bash
zypper info packagename
```

Check whether a package is installed (alternative).

```bash
rpm -qi systemd
```

Check whether `wicked` is running. Wicked is a network management utility (like NetworkManager).

```bash
systemctl is-active wicked
```

The `wicked` configuration file for an interface is `/etc/sysconfig/network/ifcfg-ethXX`.

```bash
cat /etc/sysconfig/network/ifcfg-ethXX
```

Add a repository (short form: `zypper ar URL`).

```bash
zypper addrepo URL
```

Remove a repository (short form: `zypper rr URL`).

```bash
zypper removerepo URL
```

List all repositories (short form: `zypper lr`).

```bash
zypper repos
```

### Firewall Management

Check which firewall service is running (only one of them should be active).

```bash
systemctl status firewalld.service
systemctl status ufw.service
systemctl status iptables.service
```

On Red Hat, the file `/etc/services` lists all the services and their ports (for example `http`: port 8080).

```bash
cat /etc/services
```

Custom service definitions for firewalld live in `/etc/firewalld/services`.

```bash
ls /etc/firewalld/services
```

### Firewalld

Firewalld can be managed with a GUI (`sundry`) and ships with predefined service rules (XML format) that are very easy to turn on/off (NFS, NTP, HTTP, etc.). You first need to disable `iptables.service` before using firewalld. Do not create rules with `iptables` while firewalld is running, as they will be overwritten.

Main command-line client for firewalld.

```bash
firewall-cmd
```

Check whether firewalld is active.

```bash
firewall-cmd --state
```

Check whether firewalld is active (alternative).

```bash
systemctl is-active "firewalld"
```

List all firewalld rules.

```bash
firewall-cmd --list-all
```

Get the list of all services firewalld is aware of.

```bash
firewall-cmd --get-services
```

Reload the firewall configuration after adding one or several new rules.

```bash
firewall-cmd --reload
```

List all firewalld zones (public, work, dmz, home, ...).

```bash
firewall-cmd --get-zones
```

List the active zones.

```bash
firewall-cmd --get-active-zones
```

List all the rules of the `public` zone.

```bash
firewall-cmd --zone=public --list-all
```

Add a third-party service: copy any XML file in `/usr/lib/firewalld/services/`, then replace the service name and the port number in the copy.

```bash
cp /usr/lib/firewalld/services/ssh.xml /usr/lib/firewalld/services/checkmk-agent.xml
```

Permanently allow the third-party service in the default zone (example with `checkmk-agent`).

```bash
firewall-cmd --zone="$(firewall-cmd --get-default-zone)" --permanent --add-service="checkmk-agent"
```

Remove/disable a service (runtime only).

```bash
firewall-cmd --remove-service=http
```

Permanently remove/disable a service.

```bash
firewall-cmd --remove-service=http --permanent
```

Add/allow a service (runtime only).

```bash
firewall-cmd --add-service=http
```

Permanently add/allow a service (otherwise it disappears after a reload).

```bash
firewall-cmd --add-service=http --permanent
```

Add/enable a port on your firewall.

```bash
firewall-cmd --add-port=1110/tcp --permanent
```

Remove/disable a port on your firewall.

```bash
firewall-cmd --remove-port=1110/tcp --permanent
```

Block an IP address.

```bash
firewall-cmd --add-rich-rule='rule family="ipv4" source address="192.168.0.25" reject'
```

Block all incoming ICMP traffic.

```bash
firewall-cmd --add-icmp-block-inversion
```

Allow all incoming ICMP traffic.

```bash
firewall-cmd --remove-icmp-block-inversion
```

Find the IP address of a website (needed for the next command).

```bash
host -t a www.facebook.com
```

Block all outgoing traffic to a specific website/IP address.

```bash
firewall-cmd --direct --add-rule ipv4 filter OUTPUT 0 -d $IP -j DROP
```

### UFW

Show the status of UFW, or enable/disable it.

```bash
ufw status|enable|disable
```

### IPTables

Rules are processed in order: if a `DROP` rule comes first, everything is dropped without going to the next rule. All iptables logs are in `/var/log/messages` by default.

Check whether iptables is enabled.

```bash
systemctl is-active "iptables"
```

Permanently save the firewall rules.

```bash
sudo iptables-save > /etc/iptables/rules.v4
```

List the rules, chains and their policies, with line numbers.

```bash
iptables -L --line-numbers
```

Show the rules as commands (alternative listing of rules and policies).

```bash
iptables -S
```

Show the content of the NAT table.

```bash
iptables -L -t nat --line-numbers
```

Block an IP address. `-A` adds the rule at the end of the chain; use `-I` to add it at the beginning.

```bash
iptables -A INPUT -s 192.168.0.25 -j DROP
```

Block an entire IP range.

```bash
iptables -A INPUT -s 192.168.0.0/24 -j DROP
```

Delete a rule by its line number (here line 1 of the `INPUT` chain).

```bash
iptables -D INPUT 1
```

Flush all firewall rules.

```bash
iptables -F
```

Restore firewall rules from a file.

```bash
iptables-restore /location/of/file
```

Block all ICMP traffic (with an error message returned to the sender).

```bash
iptables -A INPUT -p icmp -j REJECT
```

Block all ICMP traffic (silently, without any error message).

```bash
iptables -A INPUT -p icmp -j DROP
```

Block all traffic on port 80.

```bash
iptables -A INPUT -p tcp --dport 80 -j DROP
```

Block all traffic from an IP address on a given network interface.

```bash
iptables -A INPUT -i enp0s3 -s 192.168.0.25 -j DROP
```

Allow all traffic on port 6556.

```bash
iptables -I INPUT -p tcp -m tcp --dport 6556 -j ACCEPT
```

Block all outgoing traffic to a website. First find its IP address, then add the rule.

```bash
host -t a facebook.com
iptables -A OUTPUT -d 31.13.71.36 -j DROP
```

Block all outgoing traffic to a network range.

```bash
iptables -A OUTPUT -d 31.13.71.0/24 -j DROP
```

Block all incoming traffic except SSH. The two rules must be added in this exact order (the `ACCEPT` rule first, then the final `DROP`):

```bash
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
iptables -A INPUT -j DROP
```

> **Note:** do not use `iptables -P INPUT DROP` to drop everything. Leave the policy on `ACCEPT` and use a final `DROP` rule instead, as in the `FORWARD` chain example below.

```text
Chain FORWARD (policy ACCEPT)
num target prot opt source destination
1 DROP all -- anywhere anywhere
```

> **Note:** `telnet` only does TCP, so it cannot be used to test a UDP port such as SNMP (`telnet localhost 161` will not work).

### Networking

Show the IP routing table with numerical addresses.

```bash
route -n
```

Show the ARP table (find the MAC address matching an IP).

```bash
arp -n
```

Show the IP addresses and masks (colored output).

```bash
ip -c a
```

Show the routes and gateway addresses.

```bash
ip route
```

Turn a network interface on or off.

```bash
ip link set $interface_name down | up
```

Delete the default route.

```bash
ip route del default via 172.16.10.1
```

Show the DNS server addresses.

```bash
cat /etc/resolv.conf
```

Show the settings of a network interface.

```bash
ethtool $interface_name
```

Network interface configuration file on Red Hat-like systems.

```bash
cat /etc/sysconfig/network-scripts/ifcfg-ensXXX
```

Restart the network service (depending on which one is used).

```bash
systemctl restart systemd-networkd
systemctl restart NetworkManager
```

Turn networking off.

```bash
nmcli networking off
```

Turn networking on.

```bash
nmcli networking on
```

Check the status of `wicked`, the network utility for SUSE Linux.

```bash
systemctl status wicked
```

### GRUB

Set a password for GRUB2 (physical machines).

```bash
grub2-set-password
```

List the installed kernels (rescue kernels excluded).

```bash
grubby --info=ALL | grep ^kernel | grep -v rescue
```

Show the default kernel.

```bash
grubby --default-kernel
```

### Managing Daemons

List the daemons managed by SysV init (equivalent to listing `/etc/init.d`).

```bash
chkconfig --list
ls /etc/init.d
```

Enable or disable a daemon at boot.

```bash
chkconfig $daemon_name on|off
```

Show the runlevel configuration of a daemon.

```bash
chkconfig --list $daemon_name
```

Add a new daemon to chkconfig management.

```bash
chkconfig --add $daemon_name
```

Check that the symbolic links exist for a runlevel (replace `X` with the runlevel).

```bash
ls -l /etc/init.d/rcX.d/
```

### Clean Up /boot

**Red Hat:** remove old kernels with the package manager (avoid `rm`).

```bash
yum remove $kernel_name
```

**Debian:** regenerate the GRUB configuration after removing old kernels.

```bash
update-grub
```

### LVM

Scan for physical volumes.

```bash
pvscan
```

Scan for volume groups.

```bash
vgscan
```

If you have a mount problem, do not hesitate to run the next commands from a live CD (or from dracut in emergency mode — a reboot is enough to get there).

Enter the LVM utility from dracut.

```bash
lvm
```

Activate a volume group so its logical volumes become available (check that the `a` appears in the attributes with `lvs`).

```bash
vgchange -ay vg_name
```

Restore the metadata of a volume group from a backup file.

```bash
vgcfgrestore --file /etc/lvm/backup/$vg_name $vg_name
```

Recreate a lost physical volume from a backup file (test mode). Use the old UUID of the PV, as shown in the backup file. See the [Red Hat KB](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/logical_volume_manager_administration/mdatarecover#mdatarecover).

```bash
pvcreate --test --restorefile /etc/lvm/backup/$vg_name --uuid <the old UUID of /dev/sdc from the backup file> /dev/sdX
```

Create and format the `lv_system` logical volume.

```bash
lvcreate -L 5G -n lv_system vg_system && mkfs.ext4 /dev/mapper/vg_system-lv_system
```

Create a swap logical volume and enable it.

```bash
lvcreate -L 2G -n swaplv rootvg ; mkswap /dev/mapper/rootvg-swaplv ; swapon -a
```

Create a volume group and assign physical volumes to it.

```bash
vgcreate vg_name /dev/sdX /dev/sdY /dev/...
```

Create the physical volume `/dev/sdX`.

```bash
pvcreate /dev/sdX
```

Extend the physical volume `/dev/sdX` (after extending a partition or a disk).

```bash
pvresize /dev/sdX
```

Extend a logical volume with all the free space of its volume group and resize its filesystem (`-r`).

```bash
lvextend -r -l +100%FREE /dev/mapper/vg_name-lv_name
```

Extend a logical volume by 10 GB and resize its filesystem (`-r`).

```bash
lvextend -L+10G -r /dev/mapper/vg_name-lv_name
```

Add a physical volume to an existing volume group.

```bash
vgextend <VG_name> /dev/sdX
```

List the disk devices.

```bash
ls -l /dev/sd*
```

Show the device-mapper devices as a tree.

```bash
dmsetup ls --tree
```

Show device-mapper information in a compact format.

```bash
dmsetup info -c
```

Show hardware information from the BIOS/DMI tables.

```bash
dmidecode
```

Filesystem tools: resize an ext2/ext3/ext4 filesystem, check an ext3 filesystem, and the legacy online resizing tools (`e2fsadm`, `ext2online`).

```bash
resize2fs /dev/mapper/vg_name-lv_name
ext3.fsck /dev/mapper/vg_name-lv_name
e2fsadm
ext2online /dev/sdb1
```

Resize a partition: use `cloud-utils-growpart`, `parted` with `resizepart`, or `fdisk`.

```bash
growpart /dev/sdX partnumber
```

### User Management

Get the passwd entry of a user.

```bash
getent passwd $username
```

Kill all the processes of a user (effectively logs the user off).

```bash
killall -u username
```

Add a user to supplementary groups.

```bash
usermod -aG groupname,groupname username
```

Lock a user account.

```bash
usermod -L username
passwd -l username
```

Unlock a user account.

```bash
usermod -U username
passwd -u username
```

Assign a new UID to a user.

```bash
usermod -u UID username
```

Assign a new GID to a group.

```bash
groupmod -g GID groupname
```

Create several users from a file in batch (passwd-format file).

```bash
newusers $file
```

Create a user (add `-m` to create the home directory). Defaults are defined in `/etc/default/useradd`.

```bash
useradd -m username
```

Delete a user. Defaults are defined in `/etc/default/userdel`.

```bash
userdel username
```

Important configuration files for user creation: `/etc/login.defs` and `/etc/skel` (template for new home directories).

```bash
cat /etc/login.defs
ls -a /etc/skel
```

Show the password aging information of a user (including the date of the last password change).

```bash
chage -l username
```

Show the last password change date (alternative: look at `/etc/shadow`).

```bash
ls -l /etc/shadow
```

Show the information about a user's home directory.

```bash
stat /home/username
```

Show the information about a file.

```bash
stat filename
```

Re-enable a user account that has expired.

```bash
chage -E -1 username
```

Set a user account as expired.

```bash
chage -E 0 username
```

Set the password of a group.

```bash
gpasswd groupname
```

Set the password of a user.

```bash
passwd username
```

Show all the limits of a user. They are defined in `/etc/security/limits.conf`.

```bash
ulimit -a
```

Safely edit the `passwd` file.

```bash
vipw
```

Safely edit the `sudoers` file.

```bash
visudo
```

Check the syntax of the `sudoers` file.

```bash
visudo -c
```

Send a message to the users: `write` targets one user, `wall` broadcasts to everyone. You can also edit `/etc/motd` or run the `/etc/profile.d/motd.sh` script (message of the day).

```bash
wall "Please log off, this system is going down for maintenance -- Philippe Iannetta -- Systems Administrator"
```

Show the last connection time of a user.

```bash
lastlog -u username
```

Show the connected users and their PIDs.

```bash
who -u
```

Log off a connected user by killing the PID of their session.

```bash
kill "pid_of_connected_user_I_want_to_log_off"
```

### ACLs (Access Control Lists)

> **Notes:** setting the `-w` permission on a file/directory does not allow a user/group to remove said file/directory. Don't forget to add the necessary options for your filesystem in `/etc/fstab` (e.g. `acl`).

Show the ACLs of a file or directory.

```bash
getfacl /path/to/file
```

Add a permission for a user.

```bash
setfacl -m u:user:rwx /path/to/file
```

Add a permission for a group.

```bash
setfacl -m g:group:rw /path/to/file
```

Make all new files and directories inherit the ACL entries of the directory they belong to (default ACL).

```bash
setfacl -dm "entry" /path/to/dir
```

Remove the ACL of a user on a file.

```bash
setfacl -x u:user /path/to/file
```

Remove all the ACLs of all users on a file.

```bash
setfacl -b /path/to/file
```

### Keyboard Layouts

Set the keyboard layout to French (Latin-9).

```bash
localectl set-keymap fr-latin9
```

Set the keyboard layout to US international.

```bash
localectl set-keymap us-intl
```

List the available keymaps.

```bash
localectl list-keymaps
```

Permanent change on Debian: set the `XKBLAYOUT` variable in `/etc/default/keyboard`.

```bash
vi /etc/default/keyboard
```

Apply the change to the current session (Debian).

```bash
dpkg-reconfigure keyboard-configuration && service keyboard-setup restart
```
