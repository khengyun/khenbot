
from asyncio import events
import asyncio
from hashlib import new
import os
import discord
from discord.ext import commands
from discord.utils import get
import dotenv
from keep_alive import keep_alive
import time
import aiohttp
import random
import subprocess

# keep_alive()
#! Import this

dotenv.load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.all()

client = commands.Bot(command_prefix=">", intents=intents,help_command=None)

async def load_extensions():
    for filename in os.listdir("./Cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await client.load_extension(f"Cogs.{filename[:-3]}")


async def main():
    # if you need to, initialize other things, such as aiohttp
    # await client.load_extension('Cogs.EventVoice')  # change to whatever you need
    await load_extensions()
    await  client.start(TOKEN)



if __name__ == '__main__':
    asyncio.run(main())
    
    
