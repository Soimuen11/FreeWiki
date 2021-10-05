---
layout: default
title: My Scripts
---

You may find all my scripts in my
[Dotfiles](https://github.com/Soimuen11/Dotfiles) github repository. Just go
into **.local/scripts**. You will only find the *finished* ones here.

* [Game Launcher](#game-launcher)
* [Mystery Number Quest](#mystery-number-quest)
* [Battery Info](#battery-info)
* [Moc Controller](#moc-controller)
* [Quote Generator](#quote-generator)
* [Mouse](#mouse)
* [Bash Mailsync](#mailsync)
* [Perl Mailsync](#perl-mailsync)
* [Follow Calendar](#follow-calendar)
* [Wallpaper Randomizer](#wallpaper-randomizer)

## Game Launcher

If you wish to quickly launch your emulator games, this is the script for you.
Do install the dependencies before running it:

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

## Mystery Number Quest
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
# When starting the game. Like so:
#
#  ./mystery --easy 
#
# You may also choose normal, hard, extreme, hardcore and insane.
# Default range
RANGE=100
case $1 in
	--easy) RANGE=10;;
	--normal) RANGE=100;;
	--hard) RANGE=1000;;
	--extreme) RANGE=10000;;
	--hardcore) RANGE=100000;;
	--insane) RANGE=1000000;;
esac

echo "the number you are looking for is b/w 1 & $RANGE"

mystery=$((1 + RANDOM % $RANGE))
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
echo "you needed $(( $counter - 1)) shots"
exit 0
```

## Battery Info

Dependencies:
	+ acpi
	+ aplay / espeak (if you uncomment the lines where they are mentioned)

```bash
#!/bin/bash
# Add it as a cron job
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

## Moc Controller

Dependencies:
	+ Moc
	+ Dmenu

```bash
#!/bin/bash

# Potential Future Features:
# 1. Polybar module to control moc
# 2. AwesomeWM bar module

# Available moc actions
OPTIONS=(
	"Toggle Pause"
	"Previous"
	"Next"
	"Start"
	"Stop"
	"Info"
)

# Looping through array of moc actions
# && saving value of chosen option into $OPTION
OPTION=$(for i in "${OPTIONS[@]}"
do
	echo $i
done | dmenu -p "Moc Controller")

case "$OPTION" in
	Toggle\ Pause) mocp --toggle-pause;;
	Previous) mocp --previous;;
	Next) mocp --next;;
	Start) mocp --play;;
	Stop) mocp --stop;;
	Info) notify-send "Current Title" "$(mocp -i | grep File)";;
esac
```

## Quote Generator

For this script to work properly, you need 2 files:
1. The first is for the actual script (generator.sh)
2. The second contains all the quotes (quotes)
You may then create a symlink for it or simply source it from your
.bashrc or .zshrc (if you wish to see a quote every time you open
terminal)

```bash
#!/bin/bash
# Get nb of lines in file containing quotes
NB_LINES=$(cat /home/$USER/.local/scripts/quote_generator/quotes | wc -l)
RANDOM_NB=$(( $RANDOM % $NB_LINES ))
# Pick one line in file containing quotes
cat ~/.local/scripts/quote_generator/quotes | head -$RANDOM_NB | tail -1
```

Here is a list of quotes you can put in a file named **quotes**:
```
“Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.” ― Albert Einstein
“Be the change that you wish to see in the world.” ― Mahatma Gandhi
“Without music, life would be a mistake.” ― Friedrich Nietzsche, Twilight of the Idols
“Go to heaven for the climate and hell for the company.” ― Benjamin Franklin Wade
“A day without laughter is a day wasted.” ― Nicolas Chamfort
“Have you ever noticed how ‘What the hell’ is always the right decision to make?” ― Terry Johnson, Insignificance
“You talk when you cease to be at peace with your thoughts.” ― Kahlil Gibran, The Prophet
“May you live every day of your life.” ― Jonathan Swift
“Man is the only creature who refuses to be what he is.” ― Albert Camus
“We have to dare to be ourselves, however frightening or strange that self may prove to be.” ― May Sarton
“If a cluttered desk is a sign of a cluttered mind, of what, then, is an empty desk a sign?” ― Laurence J. Peter
“There is nothing either good or bad, but thinking makes it so.” ― William Shakespear, Hamlet
“Never let your sense of morals prevent you from doing what is right.” ― Isaac Asimov, Foundation
“Wise men speak because they have something to say; fools because they have to say something.” ― Plato
“You do not write your life with words...You write it with actions. What you think is not important. It is only important what you do.” ― Patrick Ness, A Monster Calls
“Trust yourself. You know more than you think you do.” ― Benjamin Spock
“Without deviation from the norm, progress is not possible.” ― Frank Zappa
“Think left and think right and think low and think high. Oh, the things you can think up if only you try!” ― Dr. Seuss
“Do not fear to be eccentric in opinion, for every opinion now accepted was once eccentric.” ― Bertrand Russell
“A woman has to live her life, or live to repent not having lived it.” ― D.H. Lawrence, Lady Chatterley's Lover
“Be yourself; everyone else is already taken.” ― Oscar Wilde
“No one can make you feel inferior without your consent.” ― Eleanor Roosevelt, This is My Story
“Live as if you were to die tomorrow. Learn as if you were to live forever.” ― Mahatma Gandhi
“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.” ― Marilyn Monroe
“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.” ― Albert Einstein
“We accept the love we think we deserve.” ― Stephen Chbosky, The Perks of Being a Wallflower
“Fairy tales are more than true: not because they tell us that dragons exist, but because they tell us that dragons can be beaten.” ― Neil Gaiman, Coraline
“Yesterday is history, tomorrow is a mystery, today is a gift of God, which is why we call it the present.” ― Bill Keane
“It is never too late to be what you might have been.” ― George Eliot
“There is no greater agony than bearing an untold story inside you.” ― Maya Angelou, I Know Why the Caged Bird Sings
“Everything you can imagine is real.” ― Pablo Picasso
“You can never get a cup of tea large enough or a book long enough to suit me.” ― C.S. Lewis
“To the well-organized mind, death is but the next great adventure.” ― J.K. Rowling, Harry Potter and the Sorcerer's Stone
“Life isn't about finding yourself. Life is about creating yourself.” ― George Bernard Shaw
“Do what you can, with what you have, where you are.” ― Theodore Roosevelt
“When one door of happiness closes, another opens; but often we look so long at the closed door that we do not see the one which has been opened for us.” ― Helen Keller
“Success is not final, failure is not fatal: it is the courage to continue that counts.” ― Winston S. Churchill
“So, this is my life. And I want you to know that I am both happy and sad and I'm still trying to figure out how that could be.” ― Stephen Chbosky, The Perks of Being a Wallflower
“You may say I'm a dreamer, but I'm not the only one. I hope someday you'll join us. And the world will live as one.” ― John Lennon
“I can't give you a sure-fire formula for success, but I can give you a formula for failure: try to please everybody all the time.” ― Herbert Bayard Swope
“If at first you don't succeed, try, try again. Then quit. No use being a damn fool about it.” ― W.C. Fields
“Try not to become a man of success. Rather become a man of value.” ― Albert Einstein
“It is better to fail in originality than to succeed in imitation.” ― Herman Melville
“Success is getting what you want, happiness is wanting what you get” ― W. P. Kinsella
“Letting go means to come to the realization that some people are a part of your history, but not a part of your destiny.” ― Steve Maraboli
“Failure is the condiment that gives success its flavor.” ― Truman Capote
“Have no fear of perfection - you'll never reach it.” ― Salvador Dali
“The worst part of success is trying to find someone who is happy for you.” ― Bette Midler
“Success is stumbling from failure to failure with no loss of enthusiasm.” ― Winston S. Churchill
“Success is not how high you have climbed, but how you make a positive difference to the world.” ― Roy T. Bennett, The Light in the Heart
“Don't spend time beating on a wall, hoping to transform it into a door. ” ― Coco Chanel
“Cry. Forgive. Learn. Move on. Let your tears water the seeds of your future happiness.” ― Steve Maraboli
“I'm a success today because I had a friend who believed in me and I didn't have the heart to let him down.” ― Abraham Lincoln
“Let the improvement of yourself keep you so busy that you have no time to criticize others.” ― Roy T. Bennett, The Light in the Heart
“The way to get started is to quit talking and begin doing.” ― Walt Disney
“Sometimes it takes a good fall to really know where you stand” ― Hayley Williams
“Our greatest glory is not in never falling, but in rising every time we fall.” ― Dr. Goldsmith
“All you need in this life is ignorance and confidence; then success is sure. ” ― Mark Twain
“Sometimes life knocks you on your ass... get up, get up, get up!!! Happiness is not the absence of problems, it's the ability to deal with them.” ― Steve Maraboli
“It had long since come to my attention that people of accomplishment rarely sat back and let things happen to them. They went out and happened to things.” ― Leonardo da Vinci
```

## Mouse

```bash
#!/bin/bash
sudo modprobe -r psmouse
sudo modprobe psmouse

# Doesn't work on Gentoo
# Works perfectly on Arch Linux && Ubuntu
```

## Mailsync

Once you have set up offlineimap, notmuch (& optionally msmtp and neomutt ) I
advise you to create a CRON job to regularly run this script, every 15 minutes
for instance.

**Disclaimer** : The script works but it is not flawless. I am still trying to fix the error which it throws back when executed from a terminal:
"Attempted assignment to a non-variable". If you know how to fix this, do
feel free to contact me with the solution so that I can make it public.

+ Example CRON Job:

```bash
*/15 * * * * /bin/bash /home/$USER/$SCRIPT_LOCATION/mailsync.sh
```
+ The script:

```bash
#!/usr/bin/bash
## Watch for new mail in inboxes declared in ACCOUNTS array
## Replace the $ACCOUNT_NAME variables with the names of your accounts (in
## .Mail directory) 

ACCOUNTS=(
		/home/$USER/.Mail/$ACCOUNT_NAME/Inbox/new
		/home/$USER/.Mail/$GMAIL_ACCOUNT_NAME/INBOX/new
		/home/$USER/.Mail/$ACCOUNT_NAME/Inbox/new
)

## Sync mailboxes with server
## And filter them with notmuch
/usr/bin/offlineimap -u quiet && notmuch new

## Check for NEW email
declare -i TOTAL=0
for i in "${ACCOUNTS[@]}"
do
	declare -i NEW_MAILS=$(ls $i | wc -l)
	$(( "$TOTAL"="$TOTAL"+"$NEW_MAILS" ))
done

## Notify user if there's new mail, else do nothing
if [[ $TOTAL -gt 0 ]]
then
	/usr/bin/notify-send "Email Synched:" "You have $TOTAL new email(s)"
else
	:
fi
```

## Perl Mailsync

Since doing arithmetic operations in Bash is not the most convenient way, I
decided to change strategy and rewrite my script in Perl. I also decided to
have this script run at boot (because I like to know if I have got new mail as
soon as I turn my pc. As a final piece of advice, I would recommend you to make
a symbolic link for this script, this way you can directly call it with one
command whenever and wherever you are in your file system.

To make a symbolic link:

```bash
# I would recommend to put the bin file in ~/.local/bin
# And have the actual script in ~/.local/repos
# Create these directories if they do not exist
ln -s ~/$SCRIPT_LOCATION/mailsync.pl ~/.local/bin/mailsync
```

```perl
#!/usr/bin/perl
use warnings;
use strict;

# Set up $USER environment variable and mailboxes to check
my $USER = $ENV {'USER'};
my @accounts = ( "yahoo_account1", "yahoo_account2", "gmail_account", );

# Synchronize emails && filter them
system("/usr/bin/offlineimap -u quiet && notmuch new");

# Initialize mail count
my $total_mails = 0;
my $new_mails = 0;

# For each account, add new mails to total
foreach my $account (@accounts){
	if ($account eq "gmail") {
		$new_mails = `ls /home/$USER/.Mail/$account/INBOX/new | wc -l`;
	} else {
		$new_mails = `ls /home/$USER/.Mail/$account/Inbox/new | wc -l`;
	}
	$total_mails += $new_mails;
	# Tell me in which mailbox I have mail and how many
	if ($new_mails > 0){
		system("/usr/bin/notify-send '$account' 'You have $new_mails new emails'");
	}
}

# If total new mail is superior than 0, notify me
if ($total_mails > 0){
	system("/usr/bin/notify-send 'Email Synched' 'You have $total_mails new emails'");
}
```

## Follow Calendar

+ This script is quite simple but it has several dependencies which require
  some setting up, such as **msmtp** or **offlineimap**. Imap is not mandatory, since
  you really only need to be able to **send** emails from the command line.
  Then, a regular email client could be enough. If you wish to do this 100%
  like me, you will also have to set up **neomutt**.
  
+ Disclaimer: If this script is fully functional, I am still testing and
  optimizing it. I consider that it does not entirely satisfy my needs so you
  can expect it to change (sooner or later).

+ Dependencies:
	1. Calcurse
	2. Msmtp
	3. Offlineimap
	4. Notify-send
	5. Cron

+ The script below should run at least once a day, preferably in the morning
  (so that you can anticipate the various tasks and appointments listed in your
  calendar)

```bash
#!/bin/bash

## Set sender and recipient
## They can both be the same
FROM="YOUR_EMAIL"
TO="RECIPIENT_EMAIL"

## Tell me about todos && appointments from today 
## && for the next 7 days
EVENTS=$(calcurse --query --from yesterday --days 7)

## Set up a mail file called events.mail
echo "To: $TO" >> events.mail 
echo "From: $FROM" >> events.mail 
echo "Subject: Hello $USER: Events Of The Day" >> events.mail
echo "$EVENTS" >> events.mail

## Send the email
cat events.mail | msmtp -a default $TO

## Delete the mail file you used 
## for the content of the email
rm events.mail
```

+ In case this would not be enough, I also recommend to have a CRON job to run
  once every one hour to tell you which event comes next:
  
```bash
@hourly /usr/bin/notify-send "Next Appointment:" "$(/usr/bin/calcurse --next)"
```

## Wallpaper Randomizer

```bash
#!/bin/bash

# Set directories in which script will look for wallpapers
declare -a WALLPAPER_DIRS=(
	"custom-wallpapers"
	"Desktop-Wallpaper"
	"Fate-Stay-Night-Wallpapers"
	"Hollow-Knight-Wallpapers"
)

# Set random number so that script won't always look in the same directory
# Divide $RANDOM by size of WALLPAPER_DIRS array
RANDOM_NUM="$(( $RANDOM % ${#WALLPAPER_DIRS[@]} ))"

# Set wallpaper with feh
feh --bg-scale --randomize $HOME/Immagini/${WALLPAPER_DIRS[$RANDOM_NUM]}/*
```
