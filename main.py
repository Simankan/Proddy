import discord
import os

client = discord.Client()

help_text = "Hello! My name is Proddy I have 3 core features:\n```1. Reminder \n2. Polling/voting\n3. Introduction message```"
#
#
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event 
async def on_message(message):
  if(message.author == client.user):
    return

  if(message.content.startswith('$hello')):
    await message.channel.send("Hello, ".format(client) + message.author.mention + "!")

  if(message.content.startswith('$help')):
    await message.channel.send(help_text.format(client))

my_secret = os.environ['BotToken']
client.run(my_secret)
