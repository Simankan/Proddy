import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '$')

help_text = "Hello! My name is Proddy I have 3 core features:\n```1. Reminder \n2. Polling/voting\n3. Introduction message```"
welcome_text = ' to Team 6 DL5!\nWe are so excited to have you with us and look forward to working with you!\nYour server role will be assigned automatically. Please let anyone know if you have any questions.'
#
#
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

# @client.event
# async def on_member_join(member):
#   role = discord.utils.get(member.server.roles, id="Leader")
#   await member.add_roles(member, role)

@client.command() 
async def about(ctx):
  if(ctx.author == client.user):
    return
  
  await ctx.channel.send(help_text.format(client))

@client.command()
async def message(ctx, user:discord.User, *, message=None):
  msg = 'Welcome, ' + ctx.author.mention + welcome_text
  await ctx.send('Successful.')
  await user.send(f'{msg}')

@client.command()
async def message_custom(ctx, user:discord.User, *, message):
  await ctx.send('Successful.')
  await user.send(f'{message}')


my_secret = os.environ['BotToken']
client.run(my_secret)
