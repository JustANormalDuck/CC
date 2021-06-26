import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        if message.content.startswith('Rock Paper Scissors Shoot!'):
            for emoji in ('🗿', '📄', '✂'):
                await message.add_reaction(emoji)

    if message.content.startswith('$RPS'):
        embed=discord.Embed(title="Hello!",description="Im a embed text!")
        await message.channel.send(embed=embed)

client.run('ODUyNjk5NzAxMzE2MDI2Mzk5.YMKoew.8Vwfepb-tKHrRKnrPwz6uLd9vaM')
