---
layout: default
title: My Scripts
permalink: /scripts/
---
[My Scripts](#my-scripts)
	+ [Game launcher](#game-launcher)
	+ [Mystery Number Quest](#mystery.sh)
	+ [Battery Info](#batteryinfo)

## My Scripts

You may find my scripts in my Dotfiles github repository. Just go into
.local/scripts

### game launcher

If you wish to quickly launch your emulator games, this is the script for you. Do install the dependencies before running it:
+ dmenu
+ desmume (nds emulator)
+ ppsspp (psp emulator)
+ vbm (gba emulator)
+ dolphin (gamecube and wii emulator)

```bash
#!/bin/bash

# ask me if I want to play: psp / gamecube / gba / nds
LIBRARY=$(ls "/home/$USER/Games" | dmenu -p "Emulator:")

# show me the appropriate library of games after above choice
GAME=$(ls "/home/$USER/Games/$LIBRARY" | dmenu -p "Game To Launch:")
GAME_PATH="/home/$USER/Games/$LIBRARY"

case $LIBRARY in
	psp) PPSSPPQt "$GAME_PATH/$GAME";;
	GameCube) dolphin-emu "$GAME_PATH/$GAME";;
	gba) visualboyadvance-m "$GAME_PATH/$GAME";;
	nds) desmume "$GAME_PATH/$GAME";;
esac
```

### mystery.sh
```bash
#!/bin/bash
#  __  __                 _
# |  \/  |  _   _   ___  | |_    ___   _ __   _   _
# | |\/| | | | | | / __| | __|  / _ \ | '__| | | | |
# | |  | | | |_| | \__ \ | |_  |  __/ | |    | |_| |
# |_|  |_|  \__, | |___/  \__|  \___| |_|     \__, |
#           |___/                             |___/
#  _   _                       _
# | \ | |  _   _   _ __ ___   | |__     ___   _ __
# |  \| | | | | | | '_ ` _ \  | '_ \   / _ \ | '__|
# | |\  | | |_| | | | | | | | | |_) | |  __/ | |
# |_| \_|  \__,_| |_| |_| |_| |_.__/   \___| |_|
#
#   ___                         _
#  / _ \   _   _    ___   ___  | |_
# | | | | | | | |  / _ \ / __| | __|
# | |_| | | |_| | |  __/ \__ \ | |_
#  \__\_\  \__,_|  \___| |___/  \__|
#
# You can choose the level of difficulty as a parameter
# When starting the game. Like so :
#  ./mystery --easy
# You may also choose normal, hard, extreme, hardcore and insane.
# Default range
range=100
if [[ $1 = "--easy" ]]
	then range=10
elif [[ $1 = "--normal" ]]
	then range=100
elif [[ $1 = "--hard" ]]
	then range=1000
elif [[ $1 = "--extreme" ]]
	then range=10000
elif [[ $1 = "--hardcore" ]]
	then range=100000
elif [[ $1 = "--insane" ]]
	then range=1000000
fi
echo "the number you are looking for is b/w 1 & $range"

mystery=$((1 + RANDOM % $range))
counter=1

while [[ $number -ne $mystery ]]
do
read -p "Enter a number: " number
if [[ $number -gt $mystery ]]
	then echo "it is less"
elif [[ $number -lt $mystery ]]
	then echo "it is more"
fi
counter=$(($counter + 1))
done
echo "well done, you found me"
echo "you needed $counter shots"
exit 0
```

### batteryinfo

```bash
#!/bin/bash
# Add it as a cron job:
#*/1 * * * * export DISPLAY=:0.0 && bash /home/philwayne/Dotfiles/.local/scripts/batteryinfo/bat-alert.sh
ac_adapter=$(acpi -a | cut -d' ' -f3 | cut -d- -f1)
for battery in /sys/class/power_supply/BAT?
do
	capacity=$(cat "$battery"/capacity)
done
if [[ "$ac_adapter" = "off" ]] && [[ $capacity -lt 99 ]];
then
		# aplay r2d2-alarm.wav
		notify-send "Warning: Low Battery Power!" "$capacity"
		# espeak 'Warning: Low Battery Power!'
else
	:
fi
```