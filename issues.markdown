## Issues

### SSH: could not open a connection to your authentication agent

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
terminal, you will have to re-enter your passphrase.

Option 2:
Run
```bash
ssh-agent
# Output:
SSH_AUTH_SOCK=/tmp/ssh-hZQhwQlxahPX/agent.1833; export SSH_AUTH_SOCK; 
SSH_AGENT_PID=1834; export SSH_AGENT_PID; 
echo Agent pid 496; 

# Copy and past the first 2 lines of output
SSH_AUTH_SOCK=/tmp/ssh-hZQhwQlxahPX/agent.1833; export SSH_AUTH_SOCK; 
SSH_AGENT_PID=1834; export SSH_AGENT_PID; 

# Finally, run:
ssh-add

# List your keys with
ssh-add -l
```

### df:/run/user/1000 permission denied

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

### Trackpad stops working

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

### Removing SSH passphrase

+ [Stackoverflow Response](https://stackoverflow.com/questions/112396/how-do-i-remove-the-passphrase-for-the-ssh-key-without-having-to-create-a-new-ke#112409)
+ [Set up passwordless login](https://linuxize.com/post/how-to-setup-passwordless-ssh-login/)
