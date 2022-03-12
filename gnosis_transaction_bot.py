import os

import discord
import asyncio
import requests

from dotenv import load_dotenv

load_dotenv()

mainnet_addresses = {
    'dev': '0xB65cef03b9B89f99517643226d76e286ee999e77',
    'techops': '0x86cbD0ce0c087b482782c181dA8d191De18C8275',
    'treasury_vault': '0xD0A7A8B98957b9CD3cFB9c0425AbE44551158e9e',
    'treasury_ops': '0x042B32Ac6b453485e357938bdC38e0340d4b9276',
    'fin_ops': '0xD4868d98849a58F743787c77738D808376210292',
    'politician': '0x6F76C6A1059093E21D8B1C13C4e20D8335e2909F ',
    'ibbtc': '0xB76782B51BFf9C27bA69C77027e20Abd92Bcf3a8  ',
    'recovered': '0x9faA327AAF1b564B569Cb0Bc0FDAA87052e8d92c   ',
}


def get_transaction(address):
    response = requests.get(f'https://api.gnosis.io/v1/transaction/{address}')
    return response.json()


class GnosisBot(discord.Client):
    def __init__(self):
        super().__init__()
        self.gnosis_task = self.loop.create_task(self.gnosis_transaction_loop())

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        if message.content.startswith('!gnosis'):
            return

        if message.content.startswith('!env'):
            env = os.getenv('RANDOM_DOG_API')
            await message.channel.send(env)

    async def gnosis_transaction_loop(self):
        await self.wait_until_ready()
        counter = 0
        channel = self.get_channel(882799504775086130)
        while not self.is_closed():
            counter += 1
            await channel.send(f'Running gnosis transaction bot {counter}')
            await asyncio.sleep(10)


client = GnosisBot()
client.run(os.getenv('BOT_TOKEN'))
