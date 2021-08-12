# The Free Wiki

Starting June 4th 2020, this wiki will be a collection of all the issues I,
Phil Wayne, have faced and will face on my Linux machine. It remains
incomplete, since I have encountered many an issue, yet it shall grow over
time, from this day forth. Since this file is destined to be read by the
masses, I shall strive to be as clear as possible.

## MAIN CATEGORIES

Find me here: https://soimuen11.github.io/FreeWiki/

1. Annoying errors
2. Tips, tricks & helpful programs
3. Curl tricks
4. Gaming on Linux
5. Ffmpeg
6. Other

## ANNOYING ERRORS:

### df:/run/user/1000 permission denied

If you ever encounter this issue, you need to type this command in your
terminal :

+ systemctl --user stop xdg-document-portal.service

Since the latter only is a temporary fix, I encourage to also type this :

+ systemctl --user disable xdg-document-portal.service

### Trackpad stops working

You only need 2 commands :

1. sudo modprobe -r psmouse (kill mouse kernel module)
2. sudo modprobe psmouse (restart mouse kernel module)

Other solution :
+ Use my script called "mouse" which does exactly that.
+ If you frequently use my script, I recommend you create a CRON job to call it
  every now and then (perhaps once every 5 minutes). This way you never have
  to worry about that anymore.

## CURL TRICKS

### Get your IP address

+ curl ifconfig.co
+ curl ifconfig.co/city
+ curl ifconfig.co/country

### News

+ curl getnews.tech

### Weather

+ curl wttr.in

## TIPS, TRICKS & HELPFUL PROGRAMS

### Mounting Android phones in Linux

1. Install simple-mtpfs (from the AUR if you are running Arch Linux)
2. Create Android/ directory in your home/
3. Run : simple-mtpfs -o enable-move --device 1 Android/ 
(1 being the device ID)
4. Unmount with : fusermount -u Android/

Other solution:

+ Use bluetooth

### Installing Android in Vbox

+ Change motherboard to PS/2 Mouse in System tab
+ Change Processors to 2+
+ Change Display to 3d and VboxSVGA

### Video / Audio Editing Software

+ Kdenlive / Olive
+ Ffmpeg
+ OBS
+ Audacity / Sox

### Displaying keystrokes during screencast

Install this program (with sudo privileges):

+ screenkey
+ For Arch users: pacman -S screenkey OR yay -S screenkey
+ For Ubuntu users: apt install screenkey


### Easily Styling Termite Terminal

Termite is a terminal emulator which I would most definitely recommend. To
configure colors and fonts quickly and nicely, I recommend this program which
you can find on github:

+ termite-style (see on github)
+ https://github.com/adi1090x/termite-style

For arch users, I believe it is also directly available in the AUR.

### Downloading Videos From YouTube

One program to rule them all:
+ youtube-dl
I have never fully experienced it but some people have recommended it to me:
+ youtube-view to watch yt videos directly in terminal
(you need an API to use youtube-view)

### Concatenating Pdfs On Arch Linux

+ yay -S pdf-append

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

+ Examples :

	- grep "something" file
	- grep "^s" file -> any line starting wit lowercase s in given file

### A Chaotic List Of Useful Programs

+ neofetch
+ image viewer = sxiv
+ pdf viewer = zathura
(don't forget to download sth to read pdfs along with zathura)
+ neomutt: cli-based email client
+ ffmpeg
+ vlc / cvlc / nvlc (vlc with ncurses interface)
+ vlc can play the radio directly from terminal too)
+ cli-visualizer : visualize music
+ ntfs-3g

### Networking

1. nmtui (this is the one you want)
	+ on archlinux, run : pacman -S networkmanager
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

### Create Your Own Wiki

+ Mediawiki (create a wikipedia-like wiki)
+ Wordpress
+ Code from scratch in html/css/js
+ With github: create a new repository, initialize it with a file named
  README.md, go to github pages, pick a theme and publish it.

### Monitor Your System

+ cron / anacron
+ dstat / htop / Perf / aide
+ sendmail / mailx / msmtp (after a cron job)

### Partition Disk From A Bash Script

+ sfdisk

### Edit Subtitles

+ Aegisub: Allows you to edit existing ones but also to create your own
  subtitles

### Pentesting programs & websites

1. For Analyzing 

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

2. Password Attacks

+ Medusa
+ John

3. Sniffing

+ Wireshark
+ Tcpdump / windump (for windows)
+ Steel Central Packet Analyzer
+ Capsa Network Analyzer
+ Omnipeek Network Analyzer
+ Observer Network Analyzer
+ Sniff-O-Matic

4. Other

+ xtightvncviewer
+ dig
+ nslookup
+ peach fuzzer = fuzzing technique
+ wafw00f : check if there's a firewall on target domain
+ rlogin
+ burpsuite

### Xorg Programs

+ xev: print content of X events
+ xrandr / arandr: set size, orientation or reflection of the outputs for a screen.
+ setxkbmap: set up your keyboard

### Write On Screen

+ banner
+ figlet

### Formatting A Flashdrive

+ check filesystem
fsck -N /dev/sd?

+ Format with vFat File System
sudo mkfs.vfat /dev/sdc1

+ Format with NTFS File System
sudo mkfs.ntfs /dev/sdc1

+ Format with EXT4 File System
sudo mkfs.ext4 /dev/sdc1

### Removing Sensitive Data From Git Repo

+ https://help.github.com/en/github/authenticating-to-github/removing-sensitive-data-from-a-repository

### Great LS commands

+ lsusb: list usb devices
+ lscpu: display information about cpu architecture
+ lspci: list all pci devices
+ lsblk: list block devices

### Customizing Bash

https://wiki.archlinux.org/index.php/Bash/Prompt_customization

### Learning AWK

https://www.tutorialspoint.com/awk/awk_basic_examples.htm

### VPS [Virtual Private Server]

+ Linode : OpenSource & cheapest option I have found
+ AWS
+ Google
+ Digital Ocean
+ Vultr

### Buying Domain Name

+ Epik (cheapest option I have found)
+ Wordpress (I wouldn't recommend it)

### Copying text from vim to an external program

"+y

### vim r!

:r! ls -> write the result of the command ls in a file directly from vim

### vim powerline

+ See archwiki "powerline"
+ https://www.tecmint.com/powerline-adds-powerful-statuslines-and-prompts-to-vim-and-bash/
+ https://powerline.readthedocs.io/en/master/usage/wm-widgets.html

### VIFM matrix color scheme

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

### Fuzzy Finders

+ Find can be a slow command
 + Use broot instead
 + Fzf also is very popular and can be used together with bfs.

### Modifying images

+ ImageMagick (cli tool). imagemagick.org is its official site. They also have a github page.
+ Canva.com: very quick and effective for youtube thumbnails. The problem is: it is web-based.
+ Gimp: Free software, equivalent to photoshop. The problem is: it is very complex.
+ Inkscape

### Customizing dwm

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

### Configuring Neomutt

+ git clone luke smith's mutt wizard OR download it from the AUR

### hdparm

hdparm is a command line utility to set and view hardware parameters of hard
disk drives. It can also be used as a simple benchmarking tool:
+ https://wiki.archlinux.org/index.php/Hdparm#Putting_a_drive_to_sleep_directly_after_boot

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
+ clone this repository : https://github.com/ChrisTitusTech/firewallsetup.git

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
last : shows a listing of last logged in users

### Pacman

+ pacman -S : install a program
+ pacman -Ss : search for a program
+ pacman -Syu : update + upgrade the system
+ pacman -Syyuu 
+ pacman -Q
+ pacman -Qte
+ pacman -R OR pacman -Rns : This removes a program and all its dependencies / config files
+ pacman -Rdd $ program : This removes only the program without its dependencies
+ pacman -Rc $program : This removes all the packages which depend on a program

### Software To Make You Own Music

+ Rosegarden
+ Audacity
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

+ SC-IM: https://github.com/andmarti1424/sc-im
Install it on Arch Linux: yay -Ss sc-im

### Restarting Display Manager

+ sudo systemctl restart [dislay-manager-name]

### Set Keyboard Without Ibus

Forever:

1. create a file : /etc/X11/xorg.conf.d/10-keyboard.conf
2. add lines I added in my current 10-keyboard.conf

Temporarily:

+ setxkbmap us
+ setxkbmap us -variant intl

### Bc

Bc is a built-in POSIX CLI calculator (for bash).

### Autojump

A shell program to cd faster, a bit like broot or fzf (though not a fuzzy finder).

### Browser Recommendations

1. Iridium (best one regarding privacy)
2. Brave (for its relative security builtin js/ad-blocker & its speed) with the vimium plugin 
3. Qutebrowser (if you love vim, you will love it)
4. Firefox (with the pentadactyl plugin)

### Getting RSS Links

FROM WEBSITES:
+ Add /feed/ at the end of the url address

FROM YOUTUBE CHANNEL:
+ Press ctrl+u to go to the page sources & search for the channelId
+ Then copy-paste this url: https://www.youtube.com/feeds/videos.xml?channel_id=YOURCHANNELIDHERE
+ Add the channelId where it belongs

INSTALL NEWSBOAT:
+ sudo apt install newsboat (debian-based distros)
+ sudo pacman -S newsboat (arch-based distros)

## GAMING ON LINUX

Nothing is less true than "you cannot play on Linux". Try out these one of
these 3 programs and you will not be disappointed. I highly recommend Steam. It
has entertained me for many an hour.

+ Wine
+ PlayOnLinux
+ Steam

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

create a list of files in a FILE
ex : filename
	file "file1_path"
	file2 "file1_path"
	file3 "file1_path"
run : ffmpeg -f concat -safe 0 -i /home/soimuen/Downloads/FILENAME -c copy output.webm

### Cutting Videos
ffmpeg -ss 00:01:00 -i input.mp4 -to 00:02:00 -c copy output.mp4

### Burning Subs To Video

NOTE: This solution "burns the subtitles" into the video, so that every viewer of the video will be forced to see them.

Use the libass library (make sure your ffmpeg install has the library in the configuration --enable-libass).

First convert the subtitles to .ass format:

ffmpeg -i subtitles.srt subtitles.ass
Then add them using a video filter:

ffmpeg -i mymovie.mp4 -vf ass=subtitles.ass mysubtitledmovie.mp4

### Sources

https://www.howtogeek.com/446706/how-to-create-a-screencast-on-linux/
ffmpeg.org
stackexchange
https://ostechnix.com/20-ffmpeg-commands-beginners/
https://wiki.archlinux.org/index.php/FFmpeg#Recording_webcam

## OTHER

### Windows (OS) list of commands
https://www.lifewire.com/list-of-command-prompt-commands-4092302

### Learning AWS
https://www.tutorialspoint.com/amazon_web_services/amazon_web_services_cloud_computing.htm
