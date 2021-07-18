import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('Meow')

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('$acknowledge'):
    await message.channel.send('Purr')
  if message.content.startswith('$meow'):
    await message.channel.send(file=discord.File('elliot/2.JPG'))

client.run(os.environ['TOKEN'])