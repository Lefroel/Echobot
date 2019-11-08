import discord as ds
from discord.ext import commands


TOKEN = 'NjQyMTkyMjQ5NTYzOTA2MDUw.XcV0SA.EehXyZwaHBDjfWCET2AbcN8LiHU'
prefix = '!'

bot = commands.Bot(command_prefix=prefix)

@bot.command(pass_context=True) #allow to return arguments
async def test(ctx, arg): #make async function of bot
    await ctx.send(arg) #returning argument


bot.run(TOKEN)