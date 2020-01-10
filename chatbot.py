# Works with Python 3

import discord
from discord.ext import commands, tasks
import os
import asyncio
import random
from itertools import cycle

# Your bot's prefix.

client = commands.Bot(command_prefix='!')

# Creates an arraylist containing phrases you'd like the bot to cycle through.

status = cycle(['DM me!', 'Wanna talk?', 'Lets chat', 'Why wont you DM me?', 'Cmon, talk to me...'])

# Do not add apostrophe's to the arraylist.

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.event
async def on_ready():
    print("Bot was deployed sucessfully !")
    while True:
        await client.change_presence(game=Game(name='DM me!'))
        await asyncio.sleep(3)
        await client.change_presence(game=Game(name='Wanna talk?'))
        await asyncio.sleep(3)
        await client.change_presence(game=Game(name='Lets chat', type = 3))
        await asyncio.sleep(3)
        await client.change_presence(game=Game(name='Why wont you DM me?', type = 2))
        await asyncio.sleep(3)

@client.event
async def on_message(message):
    message.content = message.content.lower()
    author = '{0.author.mention}'.format(message)

    # Stops the bot from talking to itself.

    if message.author == client.user:
        return

# Add/edit your responses here.

    if message.content.startswith('hello'):
        msg = 'Hello, how are you? {0.author.mention}'.format(message)
        await message.author.send(msg)

    if message.content.startswith('hey'):
        msg = ''
        randomlist = ['Hello! {0.author.mention}'.format(message),'Oh, hey!','Hello {0.author.mention}'.format(message),'How are you doing?','Heyy..','Hey, is there anything you would like to talk about? {0.author.mention}'.format(message),'Hiya!']
        await message.author.send(msg + (random.choice(randomlist)))

@client.event
async def on_ready():
    print('Bot running as...')
    print(client.user.name)
    print(client.user.id)
    print('------')
    change_status.start()

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

client.run(" Paste your token between these speech marks.")
