---
layout: default
title: Sysadmin
description: Cheatsheets containing Powershell & Bash commands and oneliners
---

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
