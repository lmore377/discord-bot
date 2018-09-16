# Discord-Word-Audio-Bot

Use this bot when you want to play a sound when a word is found in a message 

Requirements: 
pip install discord.py discord.py[voice] PyNaCl
Download opus codec: http://opus-codec.org/downloads/

Usage:

python3 bot.py -s [file] -id [channel id] -t [text] -c [codec]

"file" can be any .wav file placed in sounds
"channel_id" should be the ID of the sound channel you want the bot to play in
"text" is the text that the bot should look for
"codec" should be the location of the opus lib (Windows example: C:\codec\libopus-0.dll)(Linux example: /usr/local/lib/libopus.so)
