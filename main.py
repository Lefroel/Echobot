import discord as ds
from discord.ext import commands


TOKEN = 'NjQyMzY4MjgxNTI0ODMwMjA4.XcWBkg.swy0HvSg1yqN2GYMxw5_TZKfYXI'
PREFIX = 'e! '
client = ds.Client()
bot = commands.Bot(command_prefix=PREFIX)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    #game = ds.Game("Trying be useful")
    #await client.change_presence(status=ds.Status.idle, activity=game)


@bot.command(pass_context=True) #allow to return arguments
async def test(ctx, arg): #make async function of bot
    await ctx.send(arg) #returning argument


async def help(ctx):
    await ctx.send(bot.commands)


bot.run(TOKEN)