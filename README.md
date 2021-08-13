# The Free Wiki

## About

Starting June 4th 2020, this wiki will be a collection of all the issues I,
Phil Wayne, have faced and will face on my Linux machine. It remains
incomplete, since I have encountered many an issue, yet it shall grow over
time, from this day forth. Since this file is destined to be read by the
masses, I shall strive to be as clear as possible. If you have any suggestions,
do not hesitate to contact me or make your own fork.

## Table Of Contents

Find me here: https://soimuen11.github.io/FreeWiki/

1. [Annoying errors](#annoying-errors)
2. [Tips, tricks & helpful programs](#tips-tricks-and-helpful-programs)
3. [Curl tricks](#curl-tricks)
4. [Gaming on Linux](#gaming-on-linux)
5. [Ffmpeg](#ffmpeg)
6. [Resources](#resources)

## ANNOYING ERRORS

### df:/run/user/1000 permission denied

Df is a very handy command which reports file system disk space usage (see man
df for more info). You should at least know the -h flag, which prints a
human-readable result.  If you ever encounter this issue, you need to type this
command in your terminal:

+ systemctl --user stop xdg-document-portal.service

Since the latter only is a **temporary fix**, I encourage to also type this:

+ systemctl --user disable xdg-document-portal.service

If you want to know more about systemd, click on [this
link](https://wiki.archlinux.org/title/Systemd)

### Trackpad stops working

Since it frequently happened after sleep mode with Arch Linux and it has been
happening again with Ubuntu (strangely it never happened with Gentoo), here is
the fix I have been using. You only need **2 commands**:

1. sudo modprobe -r psmouse (kill mouse kernel module)
2. sudo modprobe psmouse (restart mouse kernel module)

Other solution:

+ Use my *script* called **mouse** which does exactly that.
+ If you frequently use my script, I recommend you create a CRON job (with root
  privileges) to call it every now and then (perhaps once every 5 minutes).
  This way you never have to worry about that anymore. To set up said cron job,
  do not hesitate to use the [Cron Guru web app](https://www.creativebloq.com/features/10-best-static-site-generators).

## CURL TRICKS

### Get Your IP Address

+ curl ifconfig.co
+ curl ifconfig.co/city
+ curl ifconfig.co/country

### News

+ curl getnews.tech

### Weather

+ curl wttr.in

## TIPS, TRICKS AND HELPFUL PROGRAMS

### Mounting Android Phones In Linux

1. Install simple-mtpfs (from the AUR if you are running Arch Linux)
2. Create Android/ directory in your home/
3. Run : simple-mtpfs -o enable-move --device 1 Android/ 
(1 being the device ID)
4. Unmount with : fusermount -u Android/

Other solutions to transfer files:

+ Use bluetooth (particularly easy with **Gnome Control Center**)
+ For file transfer, you may also install **Termux**, an android terminal app which
  you may find in the **Play Store**. From there you can set up ssh on your phone.

### Installing Android in Vbox

+ [Download the ISO](https://www.android-x86.org)
+ Change motherboard to PS/2 Mouse in System tab
+ Change Processors to 2+
+ Change Display to 3d and VboxSVGA

### Video / Audio Editing Software

+ [Kdenlive](kdenlive.org)
+ [Olive](https://www.olivevideoeditor.org/)
+ [Ffmpeg](ffmpeg.org)
+ [OBS](https://obsproject.com/)
+ [Audacity](https://www.audacityteam.org/)
+ [Sox](http://sox.sourceforge.net/)

### Displaying keystrokes during screencast

Install this program (with sudo privileges):

+ [screenkey](https://gitlab.com/screenkey/screenkey)
+ For Arch users: pacman -S screenkey OR yay -S screenkey
+ For Ubuntu users: apt install screenkey

### Easily Styling Termite Terminal

[Termite](https://github.com/thestinger/termite/) is a terminal emulator which
I would most definitely recommend. To configure colors and fonts quickly and
nicely, I recommend this program which you can find on github:

+ [termite-style](https://github.com/adi1090x/termite-style)

For Arch users, I believe it is also directly available in the AUR (it was when
I wrote this section). When I last edited this section (on Aug 13, 2021), I
read that termite is now obsolete. Hence it might be wiser to make the switch
to alacritty, as the maintainer of the git repo indicated.

### Downloading Videos From YouTube

One program to rule them all:
+ [youtube-dl](https://github.com/ytdl-org/youtube-dl)
I have never fully experienced it but some people have recommended it to me:
+ [mps-youtube](https://github.com/mps-youtube/mps-youtube)

### Concatenating Pdfs

+ yay -S pdf-append (for Arch users)

### Regular Expressions Basics

+ . - any one character
+ \* - Match any number of previous (includin 0)
+ \+ - Match any number of previous
+ $ - End of the line
+ ^ - Beginning of the line
+ \S - any non-whitespace character
+ \s - any whitespace character
+ ? - optional
+ [a-z] - any lowercase letter
+ [A-Z] - any uppercase letter
+ [A-Za-z] - any letter
+ [0-9] - any number
+ \ escape something

+ Examples:

	- grep "something" file
	- grep "^s" file -> any line starting with lowercase "s" in given file

### A Chaotic List Of Useful Programs

+ [Neofetch](https://github.com/dylanaraps/neofetch)
+ [Sxiv](https://github.com/ont/sxiv): A suckless image viewer for X vith vim keybindings
+ [Zathura](https://github.com/pwmt/zathura): A document viewer
(don't forget to download sth to read pdfs along with zathura)
+ [Neomutt](https://neomutt.org/dev/documentation): cli-based email client
+ Ffmpeg
+ Vlc / cvlc / nvlc (vlc with ncurses interface)
+ Vlc can play the radio directly from terminal too)
+ Cli-visualizer : visualize music
+ Ntfs-3g

### Networking

1. nmtui
	+ On archlinux: pacman -S networkmanager
	+ On ubuntu: apt install network-manager
2. nmcli dev wifi
3. nmcli dev wifi connect APname password
4. nmap -A -T4 hostname
5. wireshark
6. nslookup
7. wifite2
8. ifconfig
9. ip a
10. lscpi
11. net-setup to set up connection from the Gentoo livecd.

### Create Your Own Wiki

+ [Mediawiki](https://www.mediawiki.org/wiki/MediaWiki)
+ Wordpress
+ Code from scratch with HTML, CSS & JS and then self-host it.
+ With GitHub: create a new repository, initialize it with a file named
  README.md, go to github pages, pick a theme and publish it.
+ [Other amazing tools to build a website from markdown](https://www.creativebloq.com/features/10-best-static-site-generators)

### Monitor Your System

+ cron / anacron
+ dstat / perf / aide
+ sendmail / mailx / msmtp
+ top / htop / bashtop
+ journalctl

### Partition Disk

+ sfdisk: from a bash script
+ fdisk
+ cfdisk: more readable output than fdisk

### Edit Subtitles

+ Aegisub: Allows you to edit existing ones but also to create your own
  subtitles

### Pentesting programs & websites

#### Analyzing 

+ [Sherlock](https://github.com/sherlock-project/sherlock)
+ [Whois](https://www.whois.com/whois)
+ [Whatweb](https://tools.kali.org/web-applications/whatweb)
+ [Dmitry](https://tools.kali.org/information-gathering/dmitry)
+ [Shodan.io](shodan.io)
+ [Google Hacking Database](https://www.exploit-db.com)
+ [Linkedin for social engineering](linkedin.com)
+ [Icann Lookup](https://lookup.icann.org/)
+ Job boards (such as indeed.com)
+ Netcat
+ TheHarvester
+ Hping3

#### Password Attacks

+ Medusa
+ John

#### Sniffing

+ Wireshark
+ Tcpdump / Windump (for Windows)
+ Steel Central Packet Analyzer
+ Capsa Network Analyzer
+ Omnipeek Network Analyzer
+ Observer Network Analyzer
+ Sniff-O-Matic

#### Other

+ Xtightvncviewer
+ Dig
+ Nslookup
+ Peach fuzzer = fuzzing technique
+ Wafw00f : check if there's a firewall on target domain
+ Rlogin
+ Burpsuite

### Xorg Programs

+ xev: print content of X events
+ xrandr / arandr: set size, orientation or reflection of the outputs for a screen.
+ setxkbmap: set up your keyboard

### Write On Screen

+ banner
+ figlet

### Formatting A Flashdrive

+ Check filesystem
fsck -N /dev/sd?

+ Format with vFat File System
sudo mkfs.vfat /dev/sdc1

+ Format with NTFS File System
sudo mkfs.ntfs /dev/sdc1

+ Format with EXT4 File System
sudo mkfs.ext4 /dev/sdc1

### Removing Sensitive Data From Git Repo

+ [Removing Data From GitHub](https://help.github.com/en/github/authenticating-to-github/removing-sensitive-data-from-a-repository)

### Great LS commands

+ lsusb: list usb devices
+ lscpu: display information about cpu architecture
+ lspci: list all pci devices
+ lsblk: list block devices

### Customizing Bash

+ [Archwiki link](https://wiki.archlinux.org/index.php/Bash/Prompt_customization)

### Learning AWK

+ [Tutorialspoint has a great tutorial](https://www.tutorialspoint.com/awk/awk_basic_examples.htm)

### VPS [Virtual Private Server]

+ [Linode](linode.com): Open-Source & cheapest option
+ [AWS](amazon.aws.com): Most popular option
+ [Google](cloud.google.com)
+ [Digital Ocean](https://www.digitalocean.com/)
+ [Vultr](vultr.com)

### Buying Domain Name

+ [Epik](epik.com)
+ [Wordpress.org](wordpress.org)
+ [Wordpress.com](wordpress.com)

### Copying text from vim to an external program

"+y

### Vim r!

:r! ls -> write the result of the command ls in a file directly from vim

### Vim powerline

+ See archwiki "powerline"
+ https://www.tecmint.com/powerline-adds-powerful-statuslines-and-prompts-to-vim-and-bash/
+ https://powerline.readthedocs.io/en/master/usage/wm-widgets.html

### VIFM Matrix Color Scheme

.config/vifm/colors/Default.vifm

" Matrix
" by Michael jubalh Vetter
" https://github.com/jubalh/vifm-colors

```
highlight clear

highlight Win             cterm=none ctermfg=green    ctermbg=black

highlight TopLine         cterm=none ctermfg=green       ctermbg=none
highlight TopLineSel      cterm=none ctermfg=green       ctermbg=none
highlight StatusLine      cterm=none ctermfg=green       ctermbg=none
highlight Border          cterm=none ctermfg=green       ctermbg=none

highlight Selected        cterm=bold ctermfg=red    ctermbg=default
highlight CurrLine        cterm=bold ctermfg=black    ctermbg=green

highlight WildMenu        cterm=underline,reverse ctermfg=white ctermbg=black
highlight CmdLine         cterm=none ctermfg=white ctermbg=black
highlight ErrorMsg        cterm=none ctermfg=red ctermbg=black

highlight Directory       cterm=none ctermfg=blue ctermbg=default
highlight Link            cterm=none ctermfg=yellow ctermbg=default
highlight BrokenLink      cterm=none ctermfg=red ctermbg=default
highlight Socket          cterm=none ctermfg=yellow ctermbg=default
highlight Device          cterm=none ctermfg=yellow ctermbg=default
highlight Fifo            cterm=none ctermfg=yellow ctermbg=default
highlight Executable      cterm=none ctermfg=green ctermbg=default
```

### Fuzzy Finders

+ Find can be a slow command
+ Use broot instead
+ Fzf also is very popular and can be used together with bfs.

### Modifying images

+ ImageMagick (cli tool). imagemagick.org is its official site. They also have a github page.
+ Canva.com: very quick and effective for youtube thumbnails. The problem is: it is web-based.
+ Gimp: Free software, equivalent to photoshop. The problem is: it is very complex.
+ Inkscape

### Patching (Suckless Software)

1. clone the repository of the program you want to patch (eg: dmenu)
in .local/repos/
2. cd into the repo && run : sudo make install
3. download the patches
4. run : patch -p1 < name-of-patch.diff
5. if something goes wrong, look into the patch file and modify your source files manually (config.h for dmenu and dwm)

**NB : YOU NEED TO RECOMPILE (SUDO MAKE INSTALL) EVERY TIME YOU MAKE AN EDIT !**

### Configuring Neomutt

+ git clone luke smith's mutt wizard OR download it from the AUR

### hdparm

hdparm is a command line utility to set and view hardware parameters of hard
disk drives. It can also be used as a simple benchmarking tool:
+ [Click here for more info](https://wiki.archlinux.org/index.php/Hdparm#Putting_a_drive_to_sleep_directly_after_boot)

### Streaming With CVLC Command Line Mode

In your terminal, run:
+ vlc v4l2:// :v4l-vdev="/dev/video0" OR mpv /dev/video0

Then start the video with :
+ ffmpeg -video_size 1366x768 -framerate 25 -f x11grab -i :0.0 -f pulse -ac 2 -i 1 output.mkv -async 1 -vsync 1

### Audio Management

+ PulseAudio / Pavucontrol / Pulsemixer
+ Alsa / Alsamixer

+ Audacity: To record audio.
+ Sox (for terminal): Same as audacity but is terminal-based.

### Distros One Should Be Curious About?

NB: source-based = you need to compile your programs when installing them = you
do not directly install binaries

+ CRUX (source-based)
+ Gentoo (source-based)
+ Source Mage (source-based)
+ LFS (Linux From Scratch = create your own distro)
+ Slackware / OpenSuse
+ Void Linux

### Mother distros

1. Slackware
2. Debian (comes with binaries)
3. Ubuntu (debian-based)
4. Sorcerer (source-based)
5. Crux (Arch's big daddy)
6. Gentoo / Enoch
7. Redhat (Fedora, CentOS, others)

### Iptables Firewall Rules

A firewall is essentially a way to filter traffic.  What traffic do you want to
allow / block ?

There are 3 different ways that data can be sent :
+ Input = whenever you are receiving data (eg from the internet)
+ Output = Whenever you are sending data out
+ Forward = You see that a lot on routers. When data passes through from one
  device to another.

In between brackets, you have the POLICY, which ACCEPTs everything by default.

Some useful Commands:

+ iptables -L (or --list) : List  current firewall rules
+ iptables -P POLICY DROP/ACCEPT : Change a (-P) policy from drop to accept, or vice versa.
example : iptables -P FORWARD DROP
If your computer is not set up as a router, you don't need FORWARD to accept everything, so you can set its policty to DROP.
+ iptables -A : Add or Append a rule to the bottom of the chain
+ iptables -I : Add or Append a rule to the top of the chain

Make rules permanent:
+ sudo iptables-save > /etc/iptables/iptables.rules

Fast setup:
I recommend Chris Titus' configuration, which you can find clicking on the link below.
+ [Click here & clone this repository](https://github.com/ChrisTitusTech/firewallsetup.git)

### Ranger (File Manager Program)

Rename several files in one go : select the files you wish to rename with the
space bar. Then type :bulkrename. That will open your fave text-editor and then
you can rename them as you wish.

### dmesg

Program to control or examine the kernel ring buffer.

### systemd-analyze

Analyze how much time it takes for each service to load (how long to completely boot your pc)
+ systemd-analyze
+ systemd-analyze critical-chain graphical.target
+ systemd-analyze blame

### Managing logs

last: shows a listing of last logged in users

### Pacman

+ pacman -S: install a program
+ pacman -Ss: search for a program
+ pacman -Syu: update + upgrade the system
+ pacman -Syyuu 
+ pacman -Q
+ pacman -Qte
+ pacman -R OR pacman -Rns: This removes a program and all its dependencies / config files
+ pacman -Rdd $ program: This removes only the program without its dependencies
+ pacman -Rc $program: This removes all the packages which depend on a program

### Software To Make You Own Music

+ [Rosegarden](https://rosegardenmusic.com/)
+ [Audacity](https://www.audacityteam.org/)
+ LMMS : Linux Multimedia Studio

### Nice Ncurses Programs

+ glances : written in Python
+ ncdu : ncurses disk usage
+ moc: listen to music from your terminal
+ cmus: equivalent to moc (I personally prefer moc)
+ bastet : a tetris for terminal
+ dialog / smenu (programs to interact with the user)
+ vifm (vim-like file manager)
+ mc (midnight commander) : file-system manager

### Recovering deleted files

+ testdisk

### Spreadsheet Program With Vim Bindings

+ [SC-IM](https://github.com/andmarti1424/sc-im)
+ Install it with the AUR on Arch Linux: yay -Ss sc-im

### Display Manager Setup

1. **Permanently** change DM:
	+ sudo systemctl disable [$CURRENT-DISPLAY-MANAGER]
	+ sudo systemctl enable [$NEW-DISPLAY-MANAGER]
2. **Temporarily** change DM:
	+ sudo systemctl stop [$CURRENT-DISPLAY-MANAGER]
	+ sudo systemctl start [$NEW-DISPLAY-MANAGER]
3. Restart DM: sudo systemctl restart [$DISLAY-MANAGER-NAME]

### Set Keyboard Without Ibus

Forever:

1. Create a file : /etc/X11/xorg.conf.d/10-keyboard.conf
2. Add lines I added in my current 10-keyboard.conf

Temporarily:

+ setxkbmap us
+ setxkbmap us -variant intl

### Bc

Bc is a built-in POSIX CLI calculator (for bash).

### Autojump

+ A shell program to cd faster, a bit like broot or fzf (though not a fuzzy finder).
+ Install it on Ubuntu: sudo apt install autojump

### Browser Recommendations

1. [Iridium is the best one regarding privacy](https://iridiumbrowser.de/)
2. [Brave & vimium plugin: for its relative security builtin js/ad-blocker & its speed](brave.com)
3. [Qutebrowser: if you love vim, you will love it](https://qutebrowser.org/)
4. [Firefox with the pentadactyl plugin](https://www.mozilla.org/it/firefox/new/?redirect_source=firefox-com)

### Getting RSS Links

FROM WEBSITES:
+ Add /feed/ at the end of the url address

FROM YOUTUBE CHANNEL:
+ Press ctrl+u to go to the page sources & search for the channelId
+ Then copy-paste this url: https://www.youtube.com/feeds/videos.xml?channel_id=YOURCHANNELIDHERE
+ Add the channelId where it belongs

[INSTALL NEWSBOAT:](https://github.com/newsboat/newsboat)
+ sudo apt install newsboat (debian-based distros)
+ sudo pacman -S newsboat (arch-based distros)

## GAMING ON LINUX

Nothing is less true than "you cannot play on Linux". Try out these one of
these 3 programs and you will not be disappointed. I highly recommend Steam. It
has entertained me for many an hour.

+ [Wine](https://www.winehq.org/)
+ [PlayOnLinux](https://www.playonlinux.com/en/)
+ [Steam](https://store.steampowered.com/)

All these programs are well documented in the Arch Wiki. Be careful and install
the proper fonts/dependencies for Steam! All three programs are directly
available with pacman or in the AUR.

+ Emulating console games

Many emulators exist. Here are the ones I use and consider as "the best":

1. Nintendo DS (nds) -> desmume
2. GameBoy Advanced (gba) -> vbam
3. PlayStation Portable (psp) -> ppsspp
4. Wii-U -> decaf OR cemu+wine
5. PC -> wine + playonlinux
6. Wii + Gamecube -> dolphin
7. Nintendo 64 -> Mupen64plus

Downloading the roms: emulatorgames.net -> download roms

## FFMPEG

### Webcamming

ffmpeg -y -i /dev/video0 out.mkv

### Determining Available Resolutions

+ xrandr

### Find Size And Offset Of Particular Window To Capture

+ xwininfo

### Find Out Which Pulseaudio Sound Sources Exist 

+ pactl list sources
to record, find the input source (not output)

### The entire ffmpeg command.

ffmpeg -video_size 1366x768 -framerate 25 -f x11grab -i :0.0 -f pulse -ac 2 -i 1 output.mkv -async 1 -vsync 1

+ video_size 1920×1080: Sets the size of the video capture. This is the value we used xrandr to find.
+ framerate 25: Sets the frames per second value.
+ f x11grab: Force the video format to a specific type. Here we’re setting the input format to the output of your X server.
+ i :0.0: This specifies the video input will come from the main screen.
+ f pulse: Sets the expected format to be PulseAudio.
+ ac 2: Set two audio channels
+ i 1: Take audio input from PulseAudio source #1. This is the value we used pactl to discover.
+ output.mkv: The name of the file we wish to create.
+ async 1: Set the audio sync method. This is a deprecated parameter, but we’re using it here to avoid error messages that can be ignored.
+ vsync 1: set the video sync method. This is a deprecated parameter, but we’re using it here to avoid error messages that can be ignored.

### Extract Audio From Video

ffmpeg -i sample.avi -q:a 0 -map a sample.mp3

### Capture only video, no audio
ffmpeg -video_size 1366x768 -framerate 25 -f x11grab -i :0.0 output.mkv -vsync 1

### Directory

If you don't specify a directory to save the video, it will be saved in the
directory ffmpeg was launched from.

### Converting files

ffmpeg -i output.mkv output.mp4
general formula : ffmpeg -i output.oldformat output.wantedformat

### Add background music
ffmpeg -i arch-install.mp4  -i archinstall-soundtrack.mp4 -c copy -map 0:v:0 -map 1:a:0 output2.mp4

### Concatenating Files

1. Create a list of files in a FILE
example: filename
	file "file1_path"
	file2 "file1_path"
	file3 "file1_path"
2. Run: ffmpeg -f concat -safe 0 -i /home/soimuen/Downloads/FILENAME -c copy output.webm

### Cutting Videos
ffmpeg -ss 00:01:00 -i input.mp4 -to 00:02:00 -c copy output.mp4

### Burning Subs To Video

**NOTE: This solution "burns the subtitles" into the video, so that every viewer of the video will be forced to see them.**

Use the libass library (make sure your ffmpeg install has the library in the configuration --enable-libass).

First convert the subtitles to .ass format:

+ ffmpeg -i subtitles.srt subtitles.ass
Then add them using a video filter:

+ ffmpeg -i mymovie.mp4 -vf ass=subtitles.ass mysubtitledmovie.mp4

### Sources

+ [An article from howtogeek.com](https://www.howtogeek.com/446706/how-to-create-a-screencast-on-linux/)
+ [Ffmpeg.org](ffmpeg.org)
+ [Stackexchange](stackexchange.com)
+ [Ffmpeg commands for beginners](https://ostechnix.com/20-ffmpeg-commands-beginners/)
+ [As usual, the archwiki](https://wiki.archlinux.org/index.php/FFmpeg#Recording_webcam)

## RESOURCES

### Quickly Access Documentation

+ Zeal
+ Man Pages
+ Info Pages
+ The --help flag shipping with (almost) every program

### Microsoft Windows

+ [List of CMD Commands](https://www.lifewire.com/list-of-command-prompt-commands-4092302)
+ [Top 20 Windows Tools To Know As Sysadmin](https://www.poweradmin.com/blog/top-20-windows-tools-every-sysadmin-should-know/)
+ [Administration Commands](https://geekflare.com/windows-administration-commands/)
+ [VLAN definition & advantages](https://www.guru99.com/vlan-definition-types-advantages.html)

### Learning AWS

+ [A tutorial from tutorials point](https://www.tutorialspoint.com/amazon_web_services/amazon_web_services_cloud_computing.htm)

### Linux Permissions

+ [Managing Permissions](https://docs.rackspace.com/support/how-to/basic-linux-directory-permissions-and-how-to-check-them)

### Free VS Open-Source Software

+ [A GNU.ORG Article](https://www.gnu.org/philosophy/open-source-misses-the-point.en.html)

### Cron Jobs

+ [Cron Guru](https://crontab.guru/)

### Other

+ [Tutorials Point](https://www.tutorialspoint.com/index.htm)
+ [w3schools](w3schools.com)
+ [javascript.info](javascript.info)
+ [Stack Overflow](https://stackoverflow.com/)
+ [openclassrooms](openclarooms.com)
+ [Udemy](https://www.udemy.com/)
+ [The Arch Wiki](archlinux.org)
+ [Gentoo Wiki](https://wiki.gentoo.org/wiki/Main_Page)
+ [The Ubuntu Wiki](https://wiki.ubuntu.com/)
+ [Hackthebox](https://hackthebox.eu)
+ [Tryhackme](https://tryhackme.com/)
+ [Italian HTML guide](https://www.html.it/guide/guida-html/)
+ [10 Tips to improve next coding project](https://www.freecodecamp.org/news/10-css-tricks-for-your-next-coding-project/)
+ [A game to learn flexbox](https://flexboxfroggy.com/)
+ [Nodeschool](https://nodeschool.io/)
