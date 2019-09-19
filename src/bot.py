# ID 602598158593425408
# TOKEN HIDDEN
# PERMISSIONS 76800

import discord
from discord.ext import commands

bot =commands.Bot(command_prefix="?")

@bot.event
async def on_ready():
    print("Everything's all ready to go~")

@bot.command()
async def foo(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def abi(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/424538115814719498/602610187160911874/IMG-20190717-WA0032.jpg')

@bot.command()
async def finest(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/424538115814719498/602610907113193514/9d16983944d174da69c6280dac8076b1.png')

@bot.command()
async def jane(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/424538115814719498/602612471450042368/ff4d36ee58d165c2f9d429411e4ff51a.png')

@bot.command()
async def stobbs5(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/424538115814719498/602612826581762058/b3f.png')

@bot.command()
async def ping(ctx):
    '''
    Displays the latency of the bot to the discord server in seconds
    '''

    # Get the latency of the bot
    print("triggered")
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)


bot.run("HIDDEN")
