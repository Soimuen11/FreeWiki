## Table Of Contents

* [SSH: could not open connection to authentication agent](#ssh-could-not-open-connection-to-authentication-agent)
* [Removing SSH passphrase](#removing-ssh-passphrase)
* [df:/run/user/1000 permission denied](#dfrunuser1000-permission-denied)
* [Trackpad Stops Working](#trackpad-stops-working)
* [Fix Brave Black Screen](#fix-brave-black-screen)
* [Xbacklight: No Outputs Have Backlight Property](#xbacklight-no-outputs-have-backlight-property)
* [Copying Content On A Website With Disabled Text Selection](#copying-content-on-a-website-with-disabled-text-selection)

## SSH: could not open connection to authentication agent

Option 1:

This means that the ssh-agent is not running. Type this in your terminal:
```bash
eval "$(ssh-agent -s)"
```
Then you only need retype ssh-add:
```bash
ssh-add
```
NB: This fix will only work for the current session. If you close your
terminal, you will have to re-enter your passphrase. I recommend you couple
this method with tmux, this way you can keep working with the same session.
If this is not enough for you and would prefer not entering your passphrase
ever again, you may also use gnome-keyring.

Option 2:
Run
```bash
ssh-agent
# Output:
SSH_AUTH_SOCK=/tmp/ssh-hZQhwQlxahPX/agent.1833; export SSH_AUTH_SOCK; 
SSH_AGENT_PID=1834; export SSH_AGENT_PID; 
echo Agent pid 496; 

# Copy and paste the first 2 lines of output
SSH_AUTH_SOCK=/tmp/ssh-hZQhwQlxahPX/agent.1833; export SSH_AUTH_SOCK; 
SSH_AGENT_PID=1834; export SSH_AGENT_PID; 

# Finally, run:
ssh-add

# List your keys with
ssh-add -l
```

## Removing SSH passphrase

+ [Stackoverflow Response](https://stackoverflow.com/questions/112396/how-do-i-remove-the-passphrase-for-the-ssh-key-without-having-to-create-a-new-ke#112409)
+ [Set up passwordless login](https://linuxize.com/post/how-to-setup-passwordless-ssh-login/)

Install keychain and combine it with ssh-agent to save passphrase for all
shell sessions.

+ [Stop Entering Passphrase All The Time](https://keyboardinterrupt.org/stop-entering-your-ssh-passphrase-all-the-time)
+ [Stachexchange Response To Stop Entering passphrase](https://stackoverflow.com/questions/10032461/git-keeps-asking-me-for-my-ssh-key-passphrase)
+ [Keychain Funtoo Docs](https://www.funtoo.org/Keychain)

## df:/run/user/1000 permission denied

Df is a very handy command which reports file system disk space usage (see man
df for more info). You should at least know the -h flag, which prints a
human-readable result.  If you ever encounter this issue, you need to type this
command in your terminal:

```bash
systemctl --user stop xdg-document-portal.service
```
Since the latter only is a **temporary fix**, I encourage to also type this:

```bash
systemctl --user disable xdg-document-portal.service
```

If you want to know more about systemd, click on [this
link](https://wiki.archlinux.org/title/Systemd)

## Trackpad stops working

Since it frequently happened after sleep mode with Arch Linux and it has been
happening again with Ubuntu (strangely it never happened with Gentoo), here is
the fix I have been using. You only need **2 commands**:

```bash
sudo modprobe -r psmouse #kill mouse kernel module
sudo modprobe psmouse #restart mouse kernel module
```

Other solution:

+ Use my *script* called **mouse** which does exactly that.
+ If you frequently use my script, I recommend you create a CRON job (with root
  privileges) to call it every now and then (perhaps once every 5 minutes).
  This way you never have to worry about that anymore. To set up said cron job,
  do not hesitate to use the [Cron Guru web app](https://www.creativebloq.com/features/10-best-static-site-generators).

## Fix Brave black screen

You need to start the brave browser with this flag:
```bash
brave --disable-gpu
```
## Xbacklight No Outputs Have Backlight Property

This means no directory is set for xbacklight. To find the directory for your
xbacklight settings, run the following commands:

```bash
sudo find /sys/ -type f -iname '*brightness*'
```

You should obtain a similar result:
```bash
/sys/devices/pci0000:00/0000:00:02.0/drm/card0/card0-eDP-1/intel_backlight/brightness
```

Now, you only need to creare a symlink:
```bash
ln -s /sys/devices/pci0000:00/0000:00:02.0/drm/card0/card0-eDP-1/intel_backlight/ /sys/class/backlight
```

**In case the above solution did not work:**

1. Create the file xorg.conf:

```bash
sudo vim /etc/X11/xorg.conf
```

2. Add the following lines:

```bash
Section "Device"
Identifier  "Card0"
Driver      "intel"
Option      "Backlight"  "intel_backlight"
EndSection
```

## Copying Content On A Website With Disabled Text Selection

+ Disable JS from the browser
+ Copy desired content directly into the source code (just open dev tools, inspect and paste)
+ Disable CSS user-select property
