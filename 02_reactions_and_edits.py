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
    if message.author == client.user:
        return

    if message.content == 'cool':
        await message.add_reaction('\N{OK HAND SIGN}')


@client.event
async def on_message_edit(before, after):
    await before.channel.send(f'{before.author.mention} edited their message from {before.content} to {after.content}')


@client.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send(f'{user.mention} reacted with {reaction.emoji}')


client.run(os.getenv('BOT_TOKEN'))
