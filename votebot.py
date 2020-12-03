# bot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
import random
import asyncio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')
bot.vote = 0.0

@bot.command()
#This is defining a '!vote x' command
async def vote(ctx, *, description):
    await ctx.send("Say a number 1-10")

    def check(m):
        if int(float(m.content)) > 0 and int(float(m.content)) < 11:
            bot.vote += float(m.content)
            if bot.vote % 1 == 0:
                bot.vote = int(bot.vote)
            return 1
        else: 
            return 0

    msg = await bot.wait_for("message", check=check)
    msg = await bot.wait_for("message", check=check)
    if bot.vote >=13:
        await ctx.send("The vote passed with " + str(bot.vote) + " points.")
        channel = bot.get_channel(783659976446967838)
        await channel.send(description)
    else:
        await ctx.send("The vote was " + str(bot.vote) + ", which was not enough to pass.")
        
    bot.vote = 0

bot.run(TOKEN)