import discord as ds
from discord.ext import commands


TOKEN = '642192249563906050'
prefix = '!'

bot = commands.Bot(command_prefix=prefix)

@bot.command(pass_context=True) #allow to return arguments
async def test(ctx, arg): #make async function of bot
    await ctx.send(arg) #returning argument

bot.run(TOKEN)