#Import Libs
import discord
import asyncio
import time
from discord.ext.commands import Bot
from discord.ext import commands
import argparse


token = 'NDkwNzg4MjQ4Mjg1NzQxMDU2.Dn-d7w.Nevhj3nNUpWB6GaOt-wDlEGLo6U' #You can replace the token if you want
prefix = ('!')

parser = argparse.ArgumentParser(description='Read README.md for instructions')
parser.add_argument('-s', action="store", dest='sound', default=0)
parser.add_argument('-id', action="store", dest='chid', default=0)
parser.add_argument('-t', action="store", dest='text', default=0)
parser.add_argument('-c', action="store", dest='opus', default=0)
args = parser.parse_args()

#Load OPUS
discord.opus.load_opus(args.opus) 
if(discord.opus.is_loaded()):
    print("Opus loaded successfully!")
else:
    print("Opus failed to load. You shouldn't even see this message cause python will assault your eyes with error messages if opus doesnt load")


client = commands.Bot(command_prefix=prefix)
#--------------------------------------------------------------------------
@client.event
async def on_message(message):

     if args.text in (message.content):

         channel = client.get_channel(args.chid)
         voice = await client.join_voice_channel(channel)
                
         player = voice.create_ffmpeg_player("sounds/%s"%args.sound) # file path to sound file
         player.start()
         while(player.is_playing()):
             time.sleep(1)
         await voice.disconnect()


client.run(token)
