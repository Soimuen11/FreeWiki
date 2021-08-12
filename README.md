# MY PERSONAL WIKI

Starting today, June 4th 2020, this file is a collection of all the issues I
have faced and will face on my Linux machine. It is still incomplete, since I
have encountered many many issues, but it shall grow over time from this day
forth. I also have decided to explain more, since this file is destined to be
read by a lot of people.

## df : /run/user/1000 permission denied

If you ever encounter this issue, you need to type this command in your
terminal :

+ systemctl --user stop xdg-document-portal.service

Since the latter only is a temporary fix, I encourage to also type this :

+ systemctl --user disable xdg-document-portal.service

## How to mount android phones in Linux

1. Install simple-mtpfs (from the AUR if you are running Arch Linux)
2. Create Android/ directory in your home/
3. Run : simple-mtpfs -o enable-move --device 1 Android/ 
(1 being the device ID)
4. Unmount with : fusermount -u Android/

## If your mouse / trackpad stops working

You need to commands :

1. sudo modprobe -r psmouse (kill mouse kernel module)
2. sudo modprobe psmouse (restart mouse kernel module)

Other solution :
+ use my script called "mouse" which does exactly that.

## Display keystrokes during screencast

Install this program :
+ screenkey
+ For Arch users : pacman -S screenkey OR yay -S screenkey

## Emulating console games

Many emulators exist. Here are the ones I use and consider as "the best" :

emulatorgames.net -> download roms

1. Nintendo DS (nds) -> desmume
2. GameBoy Advanced (gba) -> vbam
3. PlayStation Portable (psp) -> ppsspp
4. Wii-U -> decaf OR cemu+wine
5. PC -> wine + playonlinux
6. Wii + Gamecube -> dolphin
7. Nintendo 64 -> Mupen64plus

## Easily style Termite

Termite is a terminal emulator which I would most definitely recommend. To
configure colors and fonts quickly and nicely, I recommend this program which
you can find on github :

+ termite-style (see on github)
+ https://github.com/adi1090x/termite-style

For arch users, I believe it is also directly available in the AUR.

## Download videos from youtube

This one program, I cannot live without :

+ youtube-dl

I have never fully experienced it but some people have recommended it to me :

+ youtube-view to watch yt videos directly in terminal
(you need an API to use youtube-view)

## Games on Linux

Nothing is less true than "you cannot play on Linux". Try out these one of
these 3 programs and you will not be disappointed. I highly recommend Steam. It
has entertained me for many an hour.

+ Wine
+ PlayOnLinux
+ Steam

All these programs are well documented in the Arch Wiki. Be careful and install
the proper fonts/dependencies for Steam! All three programs are directly
available with pacman or in the AUR.

## Concatenating pdfs

+ yay -S pdf-append

## Regular expressions basics

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

+ Examples :
	- grep "something" file
	- grep "^s" file -> any line starting wit lowercase s in given file

## Unordered Useful Programs

+ neofetch
+ image viewer = sxiv
+ pdf viewer = zathura
(don't forget to download sth to read pdfs along with zathura)
+ neomutt
+ ffmpeg
+ vlc / cvlc / nvlc (vlc with ncurses interface)
+ vlc can play the radio directly from terminal too)
+ cli-visualizer : visualize music
+ ntfs-3g

## Networking

1. nmtui (this is the one you want)
on archlinux, run : pacman -S networkmanager
2. nmcli dev wifi
3. nmcli dev wifi connect APname password
4. nmap +ip a+ nmap -sn 10.1.0.85/24
5. wireshark
6. nslookup
7. wifite2
8. ifconfig
9. ip a
10. lscpi
11. net-setup to set up connection from the Gentoo livecd.

## Formatting a flashdrive

+ check filesystem
fsck -N /dev/sd?

+ Format with vFat File System
sudo mkfs.vfat /dev/sdc1

+ Format with NTFS File System
sudo mkfs.ntfs /dev/sdc1

+ Format with EXT4 File System
sudo mkfs.ext4 /dev/sdc1

## Removing sensitive data from a git repo
+ https://help.github.com/en/github/authenticating-to-github/removing-sensitive-data-from-a-repository

## Great ls commands

+ lsusb
+ lscpu
+ lspci

## Windows (OS) list of commands
https://www.lifewire.com/list-of-command-prompt-commands-4092302

## Customize bash
https://wiki.archlinux.org/index.php/Bash/Prompt_customization

## Learn AWK
https://www.tutorialspoint.com/awk/awk_basic_examples.htm

## Learn AWS
https://www.tutorialspoint.com/amazon_web_services/amazon_web_services_cloud_computing.htm

## VPS [Virtual Private Server]

+ Linode : OpenSource & cheapest option I have found
+ AWS
+ Google
+ Digital Ocean
+ Vultr

## Buying a domain name

+ Epik (cheapest option I have found)
+ Wordpress (I wouldn't recommend it)

## Installing brave

### On Arch Linux

+ yay -S brave-bin

### On Gentoo

+ non lo so ancora

## copy text from vim to an external program

"+y

## Installing android in Vbox

+ Change motherboard to PS/2 Mouse in System tab
+ Change Processors to 2+
+ Change Display to 3d and VboxSVGA

## FFMPEG

### webcamming

ffmpeg -y -i /dev/video0 out.mkv

### determining available resolutions

xrandr

### find size and offset of particular window to capture

xwininfo

### find out which pulseaudio sound sources exist 

pactl list sources
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

### Extract audio from video
ffmpeg -i sample.avi -q:a 0 -map a sample.mp3

### Capture only video, no audio
ffmpeg -video_size 1366x768 -framerate 25 -f x11grab -i :0.0 output.mkv -vsync 1

### Directory
If you don't specify a directory to save the video, it will be saved in the directory ffmpeg was launched from.

### Converting files
ffmpeg -i output.mkv output.mp4
general formula : ffmpeg -i output.oldformat output.wantedformat

### Add background music
ffmpeg -i arch-install.mp4  -i archinstall-soundtrack.mp4 -c copy -map 0:v:0 -map 1:a:0 output2.mp4

### concatenating files
create a list of files in a FILE
ex : filename
	file "file1_path"
	file2 "file1_path"
	file3 "file1_path"
run : ffmpeg -f concat -safe 0 -i /home/soimuen/Downloads/FILENAME -c copy output.webm
### cutting videos
ffmpeg -ss 00:01:00 -i input.mp4 -to 00:02:00 -c copy output.mp4

### Burning subs to video
NOTE: This solution "burns the subtitles" into the video, so that every viewer of the video will be forced to see them.

Use the libass library (make sure your ffmpeg install has the library in the configuration --enable-libass).

First convert the subtitles to .ass format:

ffmpeg -i subtitles.srt subtitles.ass
Then add them using a video filter:

ffmpeg -i mymovie.mp4 -vf ass=subtitles.ass mysubtitledmovie.mp4

### Info source
https://www.howtogeek.com/446706/how-to-create-a-screencast-on-linux/
ffmpeg.org
stackexchange
https://ostechnix.com/20-ffmpeg-commands-beginners/
https://wiki.archlinux.org/index.php/FFmpeg#Recording_webcam

## Video / Audio Editing
+ kdenlive / Olive
+ ffmpeg
+ OBS
+ Audacity / Sox

## Fuzzy Finders
Find can be a slow command
 + Use broot instead
 + There's also fzf which is quite popular and can be used together with bfs.

## Modifying images
+ ImageMagick (cli tool); imagemagick.org -> official site; they also have a github page
+ canva.com -> very quick and effective for youtube thumbnails
+ gimp -> free software, equivalent to photoshop

## Customizing dwm
Look in :
/usr/share/doc/dwm/
You'll find a Readme and a license file.
Then create a config.h and config.mk in /usr/local

### Patching
1. clone the repository of the program you want to patch (eg: dmenu)
in .local/repos/
( 2. make)
3. cd into the repo && run : sudo make install
4. download the patches
5. run : patch -p1 < name-of-patch.diff
6. if something goes wrong, look into the patch file and modify your source files manually (config.h for dmenu and dwm)

NB : YOU NEED TO RECOMPILE (SUDO MAKE INSTALL) EVERY TIME YOU MAKE AN EDIT !

## Configuring neomutt
git clone luke smith's mutt wizard OR download it from the AUR

## hdparm
https://wiki.archlinux.org/index.php/Hdparm#Putting_a_drive_to_sleep_directly_after_boot

hdparm is a command line utility to set and view hardware parameters of hard disk drives. It can also be used as a simple benchmarking tool.

## Stream with CVLC command line mode
RUN :
+ vlc v4l2:// :v4l-vdev="/dev/video0" OR mpv /dev/video0
THEN start the video with :
+ ffmpeg -video_size 1366x768 -framerate 25 -f x11grab -i :0.0 -f pulse -ac 2 -i 1 output.mkv -async 1 -vsync 1

## Audio recording
+ PulseAudio
+ Alsa
+ Audacity
+ Sox (for terminal)

## Distros I want to look more into
+ CRUX
+ Gentoo
+ Source Mage
+ LFS
+ Slackware / openSuse
+ Void Linux

## Mother distros
1. Slackware
2. Debian
3. Ubuntu
4. Sorcerer
5. Crux (just before Arch)
6. Gentoo / Enoch
7. Redhat (Fedora, CentOS, others)

## Iptables Firewall Rules
A firewall is essentially a way to filter traffic.
What traffic do you want to allow / block ?

There are 3 different ways that data can be sent :
+ Input = whenever you are receiving data (eg from the internet)
+ Output = Whenever you are sending data out
+ Forward = You see that a lot on routers. When data passes through from one device to another.

In between brackets, you have the POLICY, which ACCEPTs everything by default.

### Commands
+ iptables -L (or --list) : List  current firewall rules
+ iptables -P POLICY DROP/ACCEPT : Change a (-P) policy from drop to accept, or vice versa.
example : iptables -P FORWARD DROP
If your computer is not set up as a router, you don't need FORWARD to accept everything, so you can set its policty to DROP.
+ iptables -A : Add or Append a rule to the bottom of the chain
+ iptables -I : Add or Append a rule to the top of the chain

### Make rules permanent
sudo iptables-save > /etc/iptables/iptables.rules

### Fast setup
clone this repository : https://github.com/ChrisTitusTech/firewallsetup.git

## Ranger
+ Rename several files in one go : select the files you wish to rename with the
  space bar. Then type :bulkrename. That will open your fave text-editor and
  then you can rename them as you wish.

## dmesg
used to control or examine the kernel ring buffer.

## systemd-analyze
analyze how much time it takes for each service to load (how long to completely boot your pc)
+ systemd-analyze
+ systemd-analyze critical-chain graphical.target
+ systemd-analyze blame

## Managing logs
last : shows a listing of last logged in users

## pacman
pacman -S : install a program
pacman -Ss : search for a program
pacman -Syu : update + upgrade the system
pacman -Syyuu 
pacman -Q
pacman -Qte
pacman -R OR pacman -Rns : This removes a program and all its dependencies / config files
pacman -Rdd $ program : This removes only the program without its dependencies
pacman -Rc $program : This removes all the packages which depend on a program

## Groff / Troff

## LVM

## Make You Own Music
+ Rosegarden
+ Audacity
+ LMMS : Linux Multimedia Studio

## Some nice ncurses programs
+ glances : written in Python
+ ncdu : ncurses disk usage
+ mc (midnight commander) : file-system manager
+ moc
+ bastet : a tetris for terminal
+ dialog / smenu
+ vifm

## Recovering deleted files
+ testdisk

## Spreadsheet program with vim bindings
SC-IM
https://github.com/andmarti1424/sc-im
yay -Ss sc-im

## restart display manager
sudo systemctl restart dislay-manager

## vim r!
:r! ls -> write the result of the command ls in a file directly from vim

## vim powerline
+ see archwiki "powerline"
+ https://www.tecmint.com/powerline-adds-powerful-statuslines-and-prompts-to-vim-and-bash/
+ https://powerline.readthedocs.io/en/master/usage/wm-widgets.html

## Set keyboard without ibus

###Forever :

1. create a file : /etc/X11/xorg.conf.d/10-keyboard.conf
2. add lines I added in my current 10-keyboard.conf

###Temporarily

+ setxkbmap us
+ setxkbmap us -variant intl

## bc
bc is a built-in POSIX CLI calculator

## Curl tricks

### Get your IP address
curl ifconfig.co
curl ifconfig.co/city
curl ifconfig.co/country

### News
curl getnews.tech

### Weather
curl wttr.in

## VIFM matrix color scheme

.config/vifm/colors/Default.vifm

" Matrix
" by Michael jubalh Vetter
" https://github.com/jubalh/vifm-colors

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

## autojump

A shell program to cd faster
Like broot or fzf (though not a fuzzy finder)

## Browsers I'd recommend

1. Iridium (best one regarding privacy)
2. Brave (for its builtin js/ad-blocker)
3. Qutebrowser
4. Firefox

## Getting RSS links

FOR WEBSITES:
+ Add /feed/ at the end of the url address

FOR YOUTUBE CHANNEL:
+ Press ctrl+u to go to the page sources & search for the channelId
+ Then copy-paste this url: https://www.youtube.com/feeds/videos.xml?channel_id=YOURCHANNELIDHERE
+ Add the channelId where it belongs

## Create your own wiki

+ mediawiki (create a wikipedia-like wiki)
+ wordpress
+ code from scratch in html/css/js

## Monitor Your System

+ Cron / Anacron
+ dstat / htop / Perf / aide
+ sendmail / mailx / msmtp (after a cron job)

## Partitioning from a bash script

+ sfdisk

## Edit subtitles
+ Aegisub

## Pentesting programs / websites

### Analyzing 

+ sherlock
+ whois
+ netcat
+ whatweb
+ dmitry
+ theHarvester
+ hping3
+ shodan.io
+ https://www.exploit-db.com/ | Google Hacking Database
+ linkedin.com -> social engineering
+ job boards (such as indeed.com)
+ https://lookup.icann.org/

### Password Attacks

+ Medusa
+ John

### Sniffing

+ Wireshark
+ Tcpdump / windump (for windows)
+ Steel Central Packet Analyzer
+ Capsa Network Analyzer
+ Omnipeek Network Analyzer
+ Observer Network Analyzer
+ Sniff-O-Matic

### Other
+ xtightvncviewer
+ dig
+ nslookup
+ peach fuzzer = fuzzing technique
+ wafw00f : check if there's a firewall on target domain
+ rlogin
+ burpsuite

## Xorg programs
+ xev
+ xrandr / arandr
+ setxkbmap

## Write on screen
+ banner
+ figlet
