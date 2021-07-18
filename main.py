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
  if message.content.startswith('$hello'):
    await message.channel.send('Meow!')

client.run(os.environ['TOKEN'])