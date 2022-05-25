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

    if message.content.startswith('!flip') or message.content.startswith('！flip'):
        title = random.choice(['你係先攻', '你係後攻'])
        
        if message.author.id == os.getenv('SUZU_DISCORD_ID'):
            description = '鈴姐咁勁，點同你打deck'
        else:
            description = 'OPEN!'
        
        await message.reply(embed=discord.Embed(title=title, description=description, color=discord.Color.blue()))

    if message.content.startswith('!choose') or message.content.startswith('！choose'):
        string  = message.content.split('choose ')[1]
        choices = string.split(' ')
        if len(choices) > 1:
            await message.reply(embed=discord.Embed(title='「' + random.choice(choices) + '」', description='嗱幫你揀咗喇，唔好反口啊。', color=discord.Color.green()))
        else:
            await message.reply(embed=discord.Embed(title='點揀啊', description='下次比夠2個以上選擇我先好叫我揀', color=discord.Color.red()))

@tasks.loop(hours=1)
async def keep_alive():
    pass

client.run(os.getenv('TOKEN'))