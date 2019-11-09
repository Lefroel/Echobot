#import discord as ds
import json
from discord.ext import commands
from random import randint


class Poke(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def poke(self, ctx):
        """Poke Mimir."""
        await ctx.send("get off, kid")
        # with open('poke.json') as json_file:
        #     phrases = json.load(json_file)
        #     random = randint(0, len(phrases['poke']) - 1)
        #     await ctx.say(str(phrases['poke'][random]))


def setup(bot):
    #bot.add_command('poke')
    bot.add_cog(Poke(bot))
    print("Loaded poke command.")


def teardown(bot):
    #bot.remove_command('poke')
    bot.remove_cog(Poke(bot))
    print("Unloaded poke command")