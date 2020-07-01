import discord,asyncio
client = discord.Client()

@client.event
async def on_ready():
    print('Security bot is ready.')


@client.event
async def on_member_join(member):
    channel = client.get_channel(715044978933629059)
    banlist = open('./banlist.txt','r')
    banopen = banlist.read()
    embed = discord.Embed(description=f'{member.mention} has joined the server, they have appeared in `banlist.txt`.')
    if str(member.id) in banopen:
        banlist.close()
        message = await channel.send(embed=embed)
        await asyncio.sleep(30)
        await message.delete()

client.run('NzI3NDUwMDk1Nzg3OTY2NTM1.XvsA2A.vRI7_rygr4Z4fqEyayzyOaCGB5k')