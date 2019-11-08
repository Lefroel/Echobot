import discord as ds
from discord.ext import commands


TOKEN = 'NjQyMTkyMjQ5NTYzOTA2MDUw.XcV05g.6Uqk-PWNpddZ4dvD3eqVATpdAs0'
prefix = 'e!'

bot = commands.Bot(command_prefix=prefix)

@bot.command(pass_context=True) #allow to return arguments
async def test(ctx, arg): #make async function of bot
    await ctx.send(arg) #returning argument


async def help(ctx):
    await ctx.send(bot.commands)


bot.run(TOKEN)