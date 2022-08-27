import discord
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        print('message')

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        print('read hello')
print(TOKEN)
client.run(TOKEN)

