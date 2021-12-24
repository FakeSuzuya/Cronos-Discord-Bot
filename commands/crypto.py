import nmap
import discord
from discord.ext import commands
import os
import json
import requests
from utils.utils import get_emoji
from discord_slash import ButtonStyle, SlashCommand
from discord_slash.utils.manage_components import *
from discord.ext import commands
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
emoji = get_emoji()

class Cryptoinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def cryptoinfo(self, ctx, crypto, types = "usd"):
        price = cg.get_price(ids=crypto, vs_currencies=types)
        monnaie = ""
        if types == "usd":
            monnaie = "$"
        if types == "eur":
            monnaie = "€"
        else:
            monnaie = f"{types}"
        await ctx.send(f"{ctx.author.mention}\n{emoji['zeus']} - **Valeur d'un {crypto} :** ``{price[str(crypto)][str(types)]}`` **{monnaie}**")
        
def setup(bot):
    bot.add_cog(Cryptoinfo(bot))