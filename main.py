import discord
import os
import random
from discord.ext import tasks
from dotenv import load_dotenv

load_dotenv()
client = discord.Client()

def get_bada_text():
    return '巴打 我留意左你好耐\n你真係好幽默\n我自問都算個ok幽默既人 但係你幽默感比我真係高十幾二十倍\n錯 應該係100倍先岩\n估唔到我係呢個post竟然見識到你既威力\n我真係笑到爆左肚 依家一路打字一路撿返d腸呀內臟呀腎呀\n塞返落個肚到\n你有冇諗過未來幾個月去紅館開棟篤笑?'


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    keep_alive.start()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if '新手' in message.content and discord.utils.get(message.guild.roles, name='唔係新手') in message.author.roles:
        await message.reply(get_bada_text())

    if message.content.startswith('!flip') or message.content.startswith('！flip'):
        title = random.choice(['你係先攻', '你係後攻'])
        
        if str(message.author.id) == os.getenv('SUZU_DISCORD_ID'):
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

    if message.content.startswith('!marksix') or message.content.startswith('！marksix'):
        num_count = 0
        num_list = []
        while num_count < 6:
            num = random.randint(1, 49)
            if num not in num_list:
                num_list.append(num)
                num_count += 1
        # sort the list
        num_list.sort()
        await message.reply(embed=discord.Embed(title=', '.join(str(num) for num in num_list), description='嗱幫你揀咗喇，唔好反口啊。', color=discord.Color.blue()))

@tasks.loop(hours=1)
async def keep_alive():
    pass

client.run(os.getenv('TOKEN'))