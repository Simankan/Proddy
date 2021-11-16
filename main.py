import discord
from discord.ext import commands
import datetime
import asyncio
import os
from keep_alive import keep_alive

client = commands.Bot(command_prefix = '$')

#### TEXT variables used in Welcome & About functions ####
help_text = "Hello! My name is **Proddy** I have 3 core features:\n**1. Introduction message**: This feature allows the user to personalize an introduction message to new users.\t```Use the command below and replace [user] with the target user and [message] with your message. There are two version of message command you can use.\n\t$message [user]\n\t$message_custom [user] [message]\n\tI.E. $message @uriel\n\tI.E. $message @uriel hello, my name is Uriel. Welcome to the team!```\n**2. Polling/voting**: This feature allows the users to create polls and vote.\t```Use the command below and replace [choice#] with your choices, 5 choices max. If you only want to use 1 choice, use dashes for the rest of the choices.After inputting all 5 choices/dashes, input the time, in seconds, you want the poll to run for.\n\t$poll [choice1] [choice2] [choice3] [choice4] [choice5] [time] [prompt]\n\tI.E. $poll 1pm 2pm - - - 60 What time would you like?```\n**3. Reminder**: This feature allows the users to create a reminder and would alert the users upon the desired time.\t```Use the commmand below and replace [time] and [task] with your inputs. [time] must in the format of a number follow by the either second (s), minute (m), hour (h), or day (d)\n\t$remind [time] [task]\n\tI.E. $remind 10m take out trash```"
welcome_text = ' to Team 6 DL5!\nWe are so excited to have you with us and look forward to working with you!\nYour server role will be assigned automatically. Please let anyone know if you have any questions.'

# helper function to convert inpuuted time into standardized input
def convert(time):
  pos = ['s', 'm', 'h', 'd']

  time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600*24}

  unit = time[-1]

  if unit not in pos:
    return -1
  try:
    val = int(time[:-1])
  except:
    return -2
    
  return val * time_dict[unit]

# prints login message when Proddy first joins a server
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

# command that displays the features and commands of Proddy Bot
@client.command() 
async def about(ctx):
  if(ctx.author == client.user):
    return
  
  await ctx.channel.send(help_text.format(client))

# weclome commands and sends the targeted user a welcome message
@client.command()
async def message(ctx, user:discord.User, *, message=None):
  msg = 'Welcome, ' + ctx.author.mention + welcome_text
  await ctx.send('Successful.')
  await user.send(f'{msg}')

# command that sends the targeted user a custome welcome message
@client.command()
async def message_custom(ctx, user:discord.User, *, message):
  await ctx.send('Successful.')
  await user.send(f'{message}')
  
# command that starts a poll with input choices and specified time duration
@client.command()
async def poll(ctx, c1, c2, c3, c4, c5, time, *, topic):
  choices = [c1, c2, c3, c4 ,c5]

# Initilizes embeded message
  embed = discord.Embed(title = topic, description = f":one: {choices[0]}\n:two: {choices[1]}\n:three: {choices[2]}\n:four: {choices[3]}\n:five: {choices[4]}\n", color = ctx.author.color, timestamp = datetime.datetime.utcnow())
  embed.set_footer(text = f"Poll started by {ctx.author.name}")
  embed.set_thumbnail(url = ctx.author.avatar_url)
  message = await ctx.send(embed = embed)
  # End embeded initialization

  # Put click-able reactions on message
  await message.add_reaction("1️⃣")
  await message.add_reaction("2️⃣")
  await message.add_reaction("3️⃣")
  await message.add_reaction("4️⃣")
  await message.add_reaction("5️⃣")
  # End reactions

  converted_time = convert(time) # Call to convert to standardize time 
  if converted_time < 0:
    await ctx.send("You didn't enter the time in correctly")
    return
  
  for i in range(converted_time): # Timer
    await asyncio.sleep(1)
    embed.set_footer(text = f"Time remaining: {converted_time-i}\nPoll started by {ctx.author.name}")
    await message.edit(embed = embed)

  newmessage = await ctx.fetch_message(message.id)

  tiedResult = ["-", "-", "-", "-", "-"]
  highestVote = 0;
  counter = [0, 0, 0, 0, 0]
  for x in range(len(newmessage.reactions)):
    if(choices[x] == "-"): # Ignore dashes
       continue
    
    counter[x] = len(await newmessage.reactions[x].users().flatten())
    if(counter[x] > highestVote):
      highestVote = counter[x]
  
  for x in range(len(newmessage.reactions)):
    if(counter[x] == highestVote):
      tiedResult[x] = choices[x]
  
  if(len(tiedResult) == 0):
    result = choices[counter.index(highestVote)]
  else:
    tempMultiResults = ["", "", "", "", ""]
    for x in range(5):
      if(counter[x] == highestVote): # Handle ties
        tempMultiResults[x] = choices[x]

    result = ""

    for x in range(len(tempMultiResults)): # Ties
      result += tempMultiResults[x] + " "
  
  embed = discord.Embed(title = topic, description = f"Result: {result}", color = ctx.author.color, timestamp = datetime.datetime.utcnow())
  embed.set_footer(text = f"{choices}")

  await newmessage.edit(embed = embed)


# command that takes in time and task and reminds user after the time is up 
@client.command()
async def remind(ctx,time, * ,task):
  converted_time = convert(time) # Call to convert to standardize time 
  if converted_time < 0:
    await ctx.send("You didn't enter the time in correctly")
    return

  message = await ctx.reply(f"Started reminder for **{task}** and will last **{time}**.")
  await asyncio.sleep(converted_time)

  try:
     await ctx.author.send(f"Reminder for **{task}**")
  except:
     await ctx.reply(f"Reminder for **{task}**")

  await message.edit(content="Reminded!")


keep_alive()
my_secret = os.environ['BotToken']
client.run(my_secret)
