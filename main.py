#import discord as ds
from discord.ext import commands

TOKEN = 'NjQyMzY4MjgxNTI0ODMwMjA4.XcYcww.9pLGfNsD3fR9CqGWly0nZHus7t0'
PREFIX = 'm!'
#client = ds.Client()
bot = commands.Bot(command_prefix=PREFIX)
bot.load_extension("poke")

bot.run(TOKEN)
