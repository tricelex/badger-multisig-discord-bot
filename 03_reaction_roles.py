import os

import discord

from dotenv import load_dotenv

load_dotenv()


# https://discord.com/channels/882799429600559135/882799430108086356/951801923554664479

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_message_id = 951801923554664479

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('Hello!')

        if message.content.startswith('!goodbye'):
            await message.channel.send('Goodbye!')

        if message.content.startswith('!info'):
            await message.channel.send('I am a bot written in Python.')

    async def on_raw_reaction_add(self, payload):
        """
        Give a role based on a reaction emoji.
        """
        if payload.message_id != self.target_message_id:
            return

        guild = self.get_guild(payload.guild_id)

        if payload.emoji.name == '🇳🇬':
            role = discord.utils.get(guild.roles, name='OG')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '🔥':
            role = discord.utils.get(guild.roles, name='pm')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '💯':
            role = discord.utils.get(guild.roles, name='dev')
            await payload.member.add_roles(role)

    async def on_raw_reaction_remove(self, payload):
        """
        Remove a role based on a reaction emoji.
        """
        if payload.message_id != self.target_message_id:
            return
        guild = self.get_guild(payload.guild_id)

        if guild is None:
            # Check if we're still in the guild and it's cached.
            print('Guild is None')
            return

        member = guild.get_member(payload.user_id)
        if member is None:
            # Make sure the member still exists and is valid.
            print('member is None')
            return

        if payload.emoji.name == '🇳🇬':
            role = discord.utils.get(guild.roles, name='OG')
            await member.remove_roles(role)
        elif payload.emoji.name == '🔥':
            role = discord.utils.get(guild.roles, name='pm')
            await member.remove_roles(role)
        elif payload.emoji.name == '💯':
            role = discord.utils.get(guild.roles, name='dev')
            await member.remove_roles(role)


client = MyClient(intents=discord.Intents.all())
client.run(os.getenv('BOT_TOKEN'))
