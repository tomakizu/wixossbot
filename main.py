import discord
import mysql.connector
import os
import random
from datetime import datetime
from discord.ext import tasks
from dotenv import load_dotenv

load_dotenv()
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    query_daily_event.start()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!flip') or message.content.startswith('！flip'):
        title = random.choice(['你係先攻', '你係後攻'])
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

@tasks.loop(minutes=1)
async def query_daily_event():
    current_date = datetime.now().strftime('%Y-%m-%d')
    current_time = datetime.now().strftime('%H:%M')

    # only send message at 8am
    if current_time != '08:00':
        return
    
    # connect to database
    database = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_SCHEMA')
    )

    cursor = database.cursor()
    cursor.execute('SELECT activity.activity_time, activity_type.type_name, card_shop.shop_name, card_shop.shop_address \
                   FROM activity \
                   INNER JOIN activity_type ON activity.activity_type_id = activity_type.id \
                   INNER JOIN card_shop ON activity.card_shop_id = card_shop.id \
                   WHERE activity_date = %s ORDER BY activity_time ASC', (current_date, ))
    result = cursor.fetchall()
    cursor.close()
    database.close()

    if len(result) == 0:
        await client.get_channel(int(os.getenv('ANNOUNCEMENT_CHANNEL_ID'))).send(str(current_date) + ' 是日活動: 無')
        return
    
    text = str(current_date) + ' 是日活動: \n\n'
    for row in result:
        activity_time = str(row[0]).split(':')[0] + ':' + str(row[0]).split(':')[1]
        text += str(activity_time) + ' ' + str(row[1]) + '\n' + str(row[2]) + '\n' + str(row[3]) + '\n\n'

    await client.get_channel(int(os.getenv('ANNOUNCEMENT_CHANNEL_ID'))).send(text)

client.run(os.getenv('TOKEN'))