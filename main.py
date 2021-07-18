import discord
import os
import random

def get_image():
  picture = random.randint(1, 8)
  return picture

client = discord.Client()

@client.event
async def on_ready():
  print('Meow')

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('$pet'):
    await message.channel.send('Purr')
  if message.content.startswith('$meow'):
    jpg = 'elliot/' + str(get_image()) + '.JPG'
    await message.channel.send(file=discord.File(jpg))

client.run(os.environ['TOKEN'])