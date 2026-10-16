---
layout: default
title: Sysadmin
description: Cheatsheets containing Powershell & Bash commands and oneliners
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
* [Powershell Commands & Plugins](#powershell-commands-and-plugins)
  	* [Getting Help](#getting-help)
  	* [Checking DNS Entries](#checking-dns-entries)
  	* [Execution Policy](#execution-policy)
  	* [User Accounts and Sessions](#user-accounts-and-sessions)
  	* [Windows Logs and Server Manager](#windows-logs-and-server-manager)
  	* [Quick Script to Connect to vCenters](#quick-script-to-connect-to-vcenters)
  	  	* [Example with Two vCenters](#example-with-two-vcenters)
  	  	* [Example with Several vCenters](#example-with-several-vcenters)
  	  	* [Connect to Several vCenters with a Loop](#connect-to-several-vcenters-with-a-loop)
  	* [Connecting to ESX Hosts](#connecting-to-esx-hosts)
  	* [Host HBAs, Disks and SCSI Paths](#host-hbas-disks-and-scsi-paths)
  	* [PowerShell Oneliners](#powershell-oneliners)
  	* [Snapshot a List of Servers](#snapshot-a-list-of-servers)
  	* [List All IP Addresses](#list-all-ip-addresses)
  	* [Check Something on Multiple Linux VMs](#check-something-on-multiple-linux-vms)
  	* [Other PowerShell and PowerCLI Commands](#other-powershell-and-powercli-commands)
  	* [Open a VM Console](#open-a-vm-console)
  	* [Example Script to Create a New VM](#example-script-to-create-a-new-vm)
  	* [Listing VMs](#listing-vms)
  	* [VM, Host and Storage Cmdlets](#vm-host-and-storage-cmdlets)
  	* [Increasing the Disk of a Linux VM](#increasing-the-disk-of-a-linux-vm)
  	* [Random Numbers and Services](#random-numbers-and-services)
  	* [Keyboard Layout via PowerShell](#keyboard-layout-via-powershell)
  	* [Active Directory Management](#active-directory-management)
  	* [Task Scheduler](#task-scheduler)
  	* [Other Commands](#other-commands)

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

## Powershell Commands and Plugins

> **Note:** this section covers PowerShell, VMware PowerCLI and a few classic Windows CMD commands (`wmic`, `systeminfo`, `net user`, `query user`, `logoff`, `ipconfig`), which also work from a PowerShell prompt. All hostnames, FQDNs, IP addresses, accounts and passwords are generic examples (`example.com`, `esx01`, `vcenter01`, `admin.user`, ...): replace them with your own values.

### Getting Help

List all the PowerShell commands containing "disk".

```bash
Get-Command *disk*
```

Show the help of a command (equivalent of `man` on Linux). You can also use `man $my_command`.

```bash
Get-Help $my_command
```

Read the online documentation of a command.

```bash
Get-Help -Online $my_command
```

Show the history of the commands you ran previously.

```bash
Get-History
```

List the modules whose name matches an expression (here, containing "Directory").

```bash
Get-Module *Directory*
```

List the properties and methods of an object (pipe an object into it).

```bash
Get-Member
```

Get information about a server (model, hypervisor, etc.) — CMD version.

```bash
wmic computersystem get model
```

Get detailed information about the system (OS, hotfixes, uptime, hardware, ...) — CMD version.

```bash
systeminfo
```

Get the model and manufacturer of the computer — PowerShell version.

```bash
Get-WmiObject -Class Win32_ComputerSystem | Select-Object -Property Model, Manufacturer
```

### Checking DNS Entries

Resolve a hostname (PowerShell equivalent of `nslookup`).

```bash
Resolve-DnsName example.com
```

Resolve a hostname and query a specific record type (here `A`).

```bash
Resolve-DnsName -Type A example.com
```

Query the `TXT` records of a hostname.

```bash
Resolve-DnsName txt.example.com -Type TXT
```

### Execution Policy

Allow the current user to run local scripts (downloaded scripts must be signed).

```bash
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

### User Accounts and Sessions

Show information about a domain user account (CMD). Replace `USERNAME` with the account name.

```bash
net user USERNAME /domain
```

List the users connected to the machine (short form: `quser`). Run it with an administrator account.

```bash
query user
```

List the users connected to a remote server.

```bash
query user /server:$SERVER
```

Log off a user. Get the `user_ID` from the output of `query user`, which lists the connected users.

```bash
logoff user_ID
```

### Windows Logs and Server Manager

Open the Windows Event Viewer to read the Windows Server logs (or press `Win + R`, type `eventvwr` and press Enter).

```bash
eventvwr
```

Open Server Manager. It can be used as a central console to manage a whole Windows server fleet.

```bash
servermanager
```

### Quick Script to Connect to vCenters

Small `.ps1` script to quickly connect to several vCenters with PowerCLI.

#### Example with Two vCenters

Ignore invalid (self-signed) certificates for PowerCLI.

```bash
Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false
```

Ask for the credentials once and store them in a variable.

```bash
$Credentials = Get-Credential -Message "Enter credentials" -Username "DOMAIN\admin.user"
```

Connect to each vCenter with the stored credentials.

```bash
Connect-VIServer -Server 192.0.2.10 -Credential $Credentials
Connect-VIServer -Server 192.0.2.11 -Credential $Credentials
```

#### Example with Several vCenters

Ignore invalid certificates, and opt out of the VMware Customer Experience Improvement Program (CEIP) for the current user.

```bash
Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false
Set-PowerCLIConfiguration -Scope User -ParticipateInCEIP $false -Confirm:$false
```

Ask for the credentials once and store them in a variable.

```bash
$Credentials = Get-Credential -Message "Enter credentials" -Username "admin.user@example.com"
```

Connect to each vCenter (one line per vCenter).

```bash
Connect-VIServer -Server vcenter01.example.com -Credential $Credentials
Connect-VIServer -Server vcenter02.example.com -Credential $Credentials
Connect-VIServer -Server vcenter03.example.com -Credential $Credentials
Connect-VIServer -Server vcenter04.us.example.com -Credential $Credentials
Connect-VIServer -Server vcenter05.asia.example.com -Credential $Credentials
```

#### Connect to Several vCenters with a Loop

Same result with a `foreach` loop over an array containing the FQDN of every vCenter. To add a vCenter, just add one line to the array. The `try/catch` block reports a failed connection without stopping the loop.

```bash
Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false
$Credentials = Get-Credential -Message "Enter credentials" -Username "admin.user@example.com"

$vCenters = @(
    "vcenter01.example.com",
    "vcenter02.example.com",
    "vcenter03.example.com",
    "vcenter04.us.example.com",
    "vcenter05.asia.example.com"
)

foreach ($vCenter in $vCenters) {
    try {
        Connect-VIServer -Server $vCenter -Credential $Credentials -ErrorAction Stop | Out-Null
        Write-Host "Connected to $vCenter"
    }
    catch {
        Write-Error "Unable to connect to $vCenter : $_"
    }
}
```

Check which vCenters you are currently connected to.

```bash
$global:DefaultVIServers | Select-Object Name, User, IsConnected
```

### Connecting to ESX Hosts

Ignore invalid certificates for PowerCLI.

```bash
Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false
```

Connect to the first vCenter with a username and a password stored in variables (prefer `Get-Credential` to avoid typing a password in clear text).

```bash
Connect-VIServer 192.0.2.10 -User $username -Password $password
```

Connect to the second vCenter.

```bash
Connect-VIServer 192.0.2.11 -User $username -Password $password
```

Connect to another vCenter using its hostname.

```bash
Connect-VIServer vcenter.example.com
```

### Host HBAs, Disks and SCSI Paths

List the Fibre Channel HBAs of an ESX host.

```bash
Get-VMHostHba -VMHost esx02.example.com -Type FibreChannel
```

List the disks of an ESX host.

```bash
Get-VMHostDisk -VMHost esx02.example.com
```

Get the HBAs, the SCSI LUNs and the SCSI paths of an ESX host (`$esxi` is the host object, for example `$esxi = Get-VMHost esx02.example.com`).

```bash
$hbas = $esxi | Get-VMHostHba
$scsiluns = $hbas | Get-ScsiLun
$scsipaths = $scsiluns | Get-ScsiLunPath
```

### PowerCLI Oneliners

The oneliners below read VM names from text files (one VM name per line): `stop_vms.txt` lists the VMs to shut down, `start_vms.txt` the VMs to start afterwards.

Print each VM name of the stop list (quick check that the file is read correctly).

```bash
foreach($VM in Get-Content F:\Scripts\stop_vms.txt){echo "$VM is present"}
```

Print each VM name of the start list.

```bash
foreach($VM in Get-Content F:\Scripts\start_vms.txt){echo "$VM is present"}
```

Gracefully shut down every VM of the stop list.

```bash
foreach($VM in Get-Content F:\Scripts\stop_vms.txt){echo "$VM is being stopped" ; Stop-VM -VM $VM -Confirm:$false}
```

Check that every VM of the start list exists in the vCenter.

```bash
foreach($VM in Get-Content F:\Scripts\start_vms.txt){Get-VM $VM}
```

Create a snapshot of every VM of the stop list that is powered off (here named after a change ticket).

```bash
foreach($VM in Get-Content F:\Scripts\stop_vms.txt){if ((Get-VM $VM).PowerState -eq "PoweredOff"){New-Snapshot -VM $VM -Name "CHG123456" -Quiesce}}
```

Check that the snapshot exists on every VM of the stop list.

```bash
foreach($VM in Get-Content F:\Scripts\stop_vms.txt){echo "$VM" ; get-vm $VM | Get-Snapshot -name "CHG123456";echo `n }
```

Start every VM of the start list that has the snapshot, waiting 60 seconds between each VM.

```bash
foreach($VM in Get-Content F:\Scripts\start_vms.txt){if (Get-Snapshot -VM $VM -Name "CHG123456"){Start-VM -VM $VM; Start-Sleep -Seconds 60}}
```

Remove all the snapshots of the VMs of the start list, without waiting for the task to complete (asynchronous).

```bash
foreach($VM in Get-Content F:\Scripts\start_vms.txt){Get-VM $VM | Get-Snapshot | Remove-Snapshot -RunAsync -Confirm:$false}
```

Remove all the snapshots of the VMs of the start list and wait for each task to complete.

```bash
foreach($VM in Get-Content F:\Scripts\start_vms.txt){Get-VM $VM | Get-Snapshot | Remove-Snapshot -Confirm:$false}
```

### Snapshot a List of Servers

Create a snapshot of every powered-on VM listed in `server_list.txt` (one VM name per line).

```bash
foreach($VM in Get-Content .\server_list.txt){if ((Get-VM $VM).PowerState -eq "PoweredOn"){New-Snapshot -VM $VM -Name "Before Change" -Quiesce}}
```

### List All IP Addresses

List the IP addresses of all the VMs of the vCenter.

```bash
Get-VM | Select-Object Name, @{Name="IP Address"; Expression={$_ | Get-VMGuest | Select-Object -ExpandProperty IPAddress}}
```

### Check Something on Multiple Linux VMs

These commands use `plink.exe` (the command-line SSH client of PuTTY). Replace `admin_user` and the server names with your own.

Check that the `check_mk` agent is active on several Linux servers.

```bash
$servers = @("server01", "server02") ; $servers | ForEach-Object{plink.exe -ssh admin_user@$_ "systemctl is-active check_mk.service"}
```

Check that `firewalld` is active on several Linux servers. Passing the password on the command line is insecure: prefer SSH keys (`-i key.ppk`) when possible.

```bash
$servers = @("server01", "server02") ; $servers | ForEach-Object{plink.exe -ssh -l admin_user -pw $password $_ "systemctl is-active firewalld"}
```

### Other PowerShell and PowerCLI Commands

#### General PowerShell cmdlets

Get information about commands and cmdlets.

```bash
Get-Help
```

Show all the available commands.

```bash
Get-Command
```

Get the system family and the OS display version of the computer.

```bash
Get-ComputerInfo -Property CsSystemFamily,OSDisplayVersion
```

List the running processes.

```bash
Get-Process
```

Stop a process.

```bash
Stop-Process
```

Show the services (and their state).

```bash
Get-Service
```

Start a service.

```bash
Start-Service
```

Stop a service.

```bash
Stop-Service
```

Change the properties of a service.

```bash
Set-Service
```

Get the event logs.

```bash
Get-EventLog
```

Clear the event logs.

```bash
Clear-EventLog
```

Get information about a file or a folder.

```bash
Get-Item
```

Modify a file or a folder.

```bash
Set-Item
```

Display the content of a file.

```bash
Get-Content
```

Write to a file.

```bash
Set-Content
```

Get information about Active Directory users.

```bash
Get-ADUser
```

Modify an Active Directory user.

```bash
Set-ADUser
```

Create a new file or folder.

```bash
New-Item
```

Delete a file or a folder.

```bash
Remove-Item
```

### Open a VM Console

Open the console of a VM in full screen.

```bash
Open-VMConsoleWindow -VM "server01" -FullScreen
```

Same thing, passing the VM through the pipeline.

```bash
Get-VM server01 | Open-VMConsoleWindow -FullScreen
```

### Example Script to Create a New VM

List all the possible `GuestID` values for the `-GuestID` parameter.

```bash
[System.Enum]::GetNames([VMware.Vim.VirtualMachineGuestOsIdentifier])
```

List the available hosts.

```bash
Get-VMHost
```

List the available datastores.

```bash
Get-Datastore
```

Create a new VM on the first vCenter: 2 vCPUs, 16 GB of memory, a 40 GB thin-provisioned disk and a RHEL 9 guest OS.

```bash
New-VM -Name "vm-int01" -Server "192.0.2.10" -VMHost "esx01.example.com" -Datastore "datastore01" -NumCpu 2 -MemoryGB 16 -DiskGB 40 -DiskStorageFormat Thin -NetworkName "VM Network" -GuestID rhel9_64Guest
```

Attach an installation ISO to the new VM, connected at power-on.

```bash
New-CDDrive -VM vm-int01 -ISOPath "[ISODatastore] ISO/Linux/RHEL/9/rhel-9.4-x86_64-boot.iso" -StartConnected
```

Add a second 200 GB thin-provisioned disk to the new VM.

```bash
New-HardDisk -VM vm-int01 -CapacityGB 200 -Datastore datastore01 -StorageFormat Thin
```

The same procedure on the second vCenter (repeat it for each VM you need to create).

```bash
New-VM -Name "vm-prd01" -Server "192.0.2.11" -VMHost "esx02.example.com" -Datastore "datastore02" -NumCpu 2 -MemoryGB 16 -DiskGB 40 -DiskStorageFormat Thin -NetworkName "VM Network" -GuestID rhel9_64Guest
New-CDDrive -VM vm-prd01 -ISOPath "[ISODatastore] ISO/Linux/RHEL/9/rhel-9.4-x86_64-boot.iso" -StartConnected
New-HardDisk -VM vm-prd01 -CapacityGB 200 -Datastore datastore02 -StorageFormat Thin
```

Delete a VM permanently (removes it from the disk too). This cannot be undone.

```bash
Remove-VM vm-int01 -DeletePermanently
```

### Listing VMs

See also this tutorial: [Lister les machines virtuelles avec PowerCLI (IT-Connect)](https://www.it-connect.fr/lister-les-machines-virtuelles-avec-powercli%EF%BB%BF/).

List the VMs whose name starts with "server".

```bash
Get-VM server*
```

List the VMs located on a specific datastore.

```bash
Get-VM -Datastore datastore1
```

List the VMs of a specific vCenter.

```bash
Get-VM -Server "vcenter_name"
```

Example: list all the VMs of the vCenter `192.0.2.10`.

```bash
Get-VM -Server "192.0.2.10"
```

Show on which ESX host a VM is located (plus its power state and hardware version).

```bash
Get-VM server01 | Select-Object Name,VMHost,PowerState,HardwareVersion
```

Show the datacenters of the vCenter (for instance `DC1` and `DC2`).

```bash
Get-Datacenter
```

### VM, Host and Storage Cmdlets

Get information about all the VMs of the vCenter.

```bash
Get-VM
```

Create a new virtual machine.

```bash
New-VM
```

Start a virtual machine.

```bash
Start-VM
```

Shut down a virtual machine.

```bash
Stop-VM
```

Restart a virtual machine.

```bash
Restart-VM
```

Get information about the ESXi hosts.

```bash
Get-VMHost
```

Add a new ESXi host.

```bash
New-VMHost
```

Modify the properties of a virtual machine (for example CPU or memory).

```bash
Set-VM
```

Show the datastores of the vCenter.

```bash
Get-Datastore
```

Create a new datastore.

```bash
New-Datastore
```

Get information about the ESXi clusters.

```bash
Get-Cluster
```

Show the resource pools available in a cluster.

```bash
Get-ResourcePool
```

Retrieve the storage policies.

```bash
Get-SpbmStoragePolicy
```

Show the storage details of an ESXi host.

```bash
Get-VMHostStorage
```

Get information about the SCSI LUNs.

```bash
Get-ScsiLun
```

Show the network adapters of a VM.

```bash
Get-NetworkAdapter -VM $VM
```

Modify the network settings of a VM.

```bash
Set-NetworkAdapter
```

Get information about the guest operating system of a VM.

```bash
Get-VMGuest
```

Show the snapshots of the VMs.

```bash
Get-Snapshot
```

Create a new snapshot of a VM.

```bash
New-Snapshot
```

Add a new disk to a VM.

```bash
New-HardDisk -VM $VM -Datastore "DS Name" -CapacityGB $size -StorageFormat Thin
```

Show the last 10 tasks and events (all types) of a VM.

```bash
Get-VIEvent -Entity $VMname -MaxSamples 10
```

Test the connectivity to a TCP port (equivalent of `ping` and `netstat` / `telnet`). Here: SSH port 22.

```bash
Test-NetConnection -ComputerName $IP -Port 22
```

### Increasing the Disk of a Linux VM

Procedure to increase the disk of a Linux VM. First connect to the vCenters (see [Quick Script to Connect to vCenters](#quick-script-to-connect-to-vcenters)).

Check that the VM is found.

```bash
Get-VM $VMName
```

List the disks of the VM.

```bash
Get-HardDisk -VM vm_name
```

List the disks of the VM with their size, file name and ID, to get the name of the hard disk you want to increase.

```bash
Get-VM VMName | Get-HardDisk | Select Name,CapacityGB,FileName,Id
```

Increase "Hard disk 1" by giving it its new final size in GB (this resizes the VMDK).

```bash
Get-VM VMName | Get-HardDisk -Name "Hard disk 1" | Set-HardDisk -CapacityGB Final_Size
```

Then, on the Linux side, rescan the disk (see [SCSI Devices](#scsi-devices)) and grow the partition and the filesystem (see [Disks and Partitions](#disks-and-partitions) and [LVM](#lvm)).

### Random Numbers and Services

Generate a random number.

```bash
Get-Random
```

Show the status of all services, or of a specific service (alias: `gsv`).

```bash
Get-Service -Name servicename
```

Start a service.

```bash
Start-Service -Name servicename
```

Stop a service.

```bash
Stop-Service -Name servicename
```

### Keyboard Layout via PowerShell

Add the US English language to the current language list.

```bash
$LanguageList = Get-WinUserLanguageList
$LanguageList.Add("en-US")
Set-WinUserLanguageList $LanguageList
```

Or: replace the language list with US English only.

```bash
Set-WinUserLanguageList -LanguageList "en-US" -Force
```

Or: create a language list with both the US keyboard and the US International keyboard (with dead keys).

```bash
$LangList = New-WinUserLanguageList en-US
$LangList[0].InputMethodTips.Add("0409:00000409")  # US keyboard
$LangList[0].InputMethodTips.Add("0409:00020409")  # US International (with dead keys)
Set-WinUserLanguageList $LangList -Force
```

To make sure the US International layout is the default one, use the `Set-WinDefaultInputMethodOverride` cmdlet with the appropriate input tip.

```bash
Set-WinDefaultInputMethodOverride -InputTip "0409:00020409"
```

### Active Directory Management

Install the RSAT tools on Windows Server.

```bash
Install-WindowsFeature -Name RSAT-AD-PowerShell
```

Or on Windows 10/11.

```bash
Add-WindowsCapability -Online -Name Rsat.ActiveDirectory.DS-LDS.Tools~~~~0.0.1.0
```

Import the Active Directory module.

```bash
Import-Module ActiveDirectory
```

Unlock an account.

```bash
Unlock-ADAccount -Identity "jdoe"
```

Enable a disabled account.

```bash
Enable-ADAccount -Identity "jdoe"
```

Check the properties of an account (last password change, password expired, locked out).

```bash
Get-ADUser -Identity "firstname.lastname" -Properties PasswordLastSet, PasswordExpired, LockedOut
```

Reset the password, unlock the account and force a password change at next logon, all in one command.

```bash
Set-ADAccountPassword -Identity "jdoe" -Reset -NewPassword (ConvertTo-SecureString "TempPass123!" -AsPlainText -Force) -PassThru |
    Unlock-ADAccount -PassThru |
    Set-ADUser -ChangePasswordAtLogon $true
```

Change (reset) the password of a user.

```bash
Set-ADAccountPassword -Identity "username" -Reset -NewPassword (ConvertTo-SecureString "NewPassword123!" -AsPlainText -Force)
```

Force a password change at the next logon.

```bash
Set-ADUser -Identity "username" -ChangePasswordAtLogon $true
```

Prompt for the passwords. It asks for the old password, the new one and a confirmation.

```bash
Set-ADAccountPassword -Identity $username
```

Combined command: reset the password, force the user to change it at next logon and unlock the account.

```bash
Set-ADAccountPassword -Identity "firstname.lastname" -Reset -NewPassword (ConvertTo-SecureString "<TempPassword>" -AsPlainText -Force) -PassThru | Set-ADUser -ChangePasswordAtLogon $true -PassThru | Unlock-ADAccount
```

Specify the domain controller to use.

```bash
Set-ADAccountPassword -Identity "jdoe" -Server "dc01.example.local" -Reset -NewPassword (ConvertTo-SecureString "NewPassword!" -AsPlainText -Force)
```

Use administrator credentials.

```bash
$AdminCred = Get-Credential
Set-ADAccountPassword -Identity "jdoe" -Credential $AdminCred -Reset -NewPassword (ConvertTo-SecureString "NewPassword!" -AsPlainText -Force)
```

> **Note:** passwords typed in clear text in a command are kept in the PowerShell history. Use temporary passwords only, and force a change at next logon.

### Task Scheduler

List the scheduled tasks.

```bash
Get-ScheduledTask
```

Create a new scheduled task.

```bash
New-ScheduledTask
```

### Other Commands

Run commands on a remote computer (IP address or hostname).

```bash
Invoke-Command -ComputerName "ip_or_hostname" -ScriptBlock { my_commands }
```

Print text to the console (equivalent of `echo` on Linux).

```bash
Write-Host "text"
```

Write an error message to the error stream (like `echo`, but the output goes to the error stream so it can be redirected separately).

```bash
Write-Error "error message"
```

Release the DHCP IP address.

```bash
ipconfig /release
```

Get a new IP address from DHCP.

```bash
ipconfig /renew
```
