import discord
import os
import random
from discord.ext import tasks
from dotenv import load_dotenv

load_dotenv()
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    keep_alive.start()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!flip'):
        await message.reply(embed=discord.Embed(title=random.choice(['你係先攻', '你係後攻']), description='OPEN!', color=discord.Color.blue()))

@tasks.loop(hours=1)
async def keep_alive():
    pass

client.run(os.getenv('TOKEN'))