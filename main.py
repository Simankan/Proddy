import discord
from discord.ext import commands
import datetime
import asyncio
import os

client = commands.Bot(command_prefix = '$')

help_text = "Hello! My name is Proddy I have 3 core features:\n```1. Reminder \n2. Polling/voting\n3. Introduction message```"
welcome_text = ' to Team 6 DL5!\nWe are so excited to have you with us and look forward to working with you!\nYour server role will be assigned automatically. Please let anyone know if you have any questions.'
#
#
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
  role = discord.utils.get(member.server.roles, id='Leader')
  await client.add_roles(member, role)

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

@client.command()
async def poll(ctx, c1, c2, c3, c4, c5, *, topic):
  choices = [c1, c2, c3, c4 ,c5]
  # Reorders and groups #### NOT NEEDED ANYMORE BUT POSSIBILITY TO READD ####
  #
  # options = ""
  # c = 0
  # for x in range(5):
  #   if(choices[x] != "-"):
  #     if(c==0):
  #       options += f":one: {choices[x]}\n"
  #     elif(c==1):
  #       options += f":two: {choices[x]}\n"
  #     elif(c==2):
  #       options += f":three: {choices[x]}\n"
  #     elif(c==3):
  #       options += f":four: {choices[x]}\n"
  #     elif(c==4):
  #       options += f":five: {choices[x]}\n"
  #     else:
  #       c -= 1
  #   c += 1

  embed = discord.Embed(title = topic, description = f":one: {choices[0]}\n:two: {choices[1]}\n:three: {choices[2]}\n:four: {choices[3]}\n:five: {choices[4]}\n", color = ctx.author.color, timestamp = datetime.datetime.utcnow())
  embed.set_footer(text = f"Poll started by {ctx.author.name}")
  embed.set_thumbnail(url = ctx.author.avatar_url)
  message = await ctx.send(embed = embed)

  #if(c1 != "-"):
  await message.add_reaction("1️⃣")
  #if(c2 != "-"):
  await message.add_reaction("2️⃣")
  #if(c3 != "-"):
  await message.add_reaction("3️⃣")
  #if(c4 != "-"):
  await message.add_reaction("4️⃣")
 # if(c5 != "-"):
  await message.add_reaction("5️⃣")
  
  await asyncio.sleep(4) # 10 second timer

  newmessage = await ctx.fetch_message(message.id)
  # countArray = [0, 0, 0, 0, 0]

  # for x in range(5):
  #   countArray[x] = len(await newmessage.reactions[x].users().flatten())

  # result = "N/A"
  # mostVoted = 0
  # for x in range(5):
  #   if(choices[x] == "-"):
  #     continue

  #   if(countArray[x] > mostVoted):
  #     result = choices[x]
  
  # ---------------------------------------------------------------------------------------------------
  # THIS PART IS RESPONSIBLE FOR CREATING ANOTHER PULL IF THERE IS A TIE
  tiedResult = ["-", "-", "-", "-", "-"]
  highestVote = 0;
  counter = [0, 0, 0, 0, 0]
  for x in range(len(newmessage.reactions)):
    if(choices[x] == "-"):
       continue
    
    counter[x] = len(await newmessage.reactions[x].users().flatten())
    if(counter[x] > highestVote):
      highestVote = counter[x]
  
  for x in range(len(newmessage.reactions)):
    if(counter[x] == highestVote):
      tiedResult[x] = choices[x]
  
  if(len(tiedResult) == 0):
    # await poll(ctx, tiedResult[0], tiedResult[1], tiedResult[2], tiedResult[3], tiedResult[4], topic)
    result = choices[counter.index(highestVote)]
  else:
    tempMultiResults = ["", "", "", "", ""]
    for x in range(5):
      if(counter[x] == highestVote):
        tempMultiResults[x] = choices[x]

    result = ""

    for x in range(len(tempMultiResults)):
      result += tempMultiResults[x] + " "
  # ---------------------------------------------------------------------------------------------------
  
  embed = discord.Embed(title = topic, description = f"Result: {result}", color = ctx.author.color, timestamp = datetime.datetime.utcnow())
  embed.set_footer(text = f"{choices}")

  await newmessage.edit(embed = embed)

  

my_secret = os.environ['BotToken']
client.run(my_secret)
