import os

import discord
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        return
    await message.channel.send('Hello World!')


client.run(os.getenv('BOT_TOKEN'))
