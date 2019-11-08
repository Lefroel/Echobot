import discord as ds
from discord.ext import commands


TOKEN = 'NjQyMzY4MjgxNTI0ODMwMjA4.XcV6Mg.ZddoK-vqRIsy4msH7ZmMvu3x1so'
prefix = 'e! '

bot = commands.Bot(command_prefix=prefix)

@bot.command(pass_context=True) #allow to return arguments
async def test(ctx, arg): #make async function of bot
    await ctx.send(arg) #returning argument


async def help(ctx):
    await ctx.send(bot.commands)


bot.run(TOKEN)