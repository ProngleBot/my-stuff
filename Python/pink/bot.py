import discord
from discord.ext import commands
TOKEN = 'Njg5ODg4NDczMTkyMjAyMzEw.Xo9MVg.9oyw12h1UXnpXjF3BGMbOQDBK1M'
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('hello')

@client.event
async def on_message(message):
    author = message.author
    content = message.content
    channel = message.channel
    print('{}:{}'.format(author,content))
    if message.content.startswith(".kek"):
        await channel.send('kek')
    if message.content.startswith('.say'):
        msg = message.content.split()
        output = ''
        for word in msg[1:]:
            output += word
            output += ' '
        await channel.send(output)

@client.event
async def on_message_delete(message):
    await message.channel.send('pfft you thought kek')
client.run(TOKEN)