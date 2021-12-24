import nmap
import discord
from discord.ext import commands
import os
import json
from web3 import Web3
import requests
from utils.utils import get_emoji
emoji = get_emoji()
import pyshorteners as sh

class Urlshort(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def shorturl(self, ctx, url):
        s = sh.Shortener()
        urlshort = s.tinyurl.short(url)
        await ctx.send(f"{ctx.author.mention}\n{emoji['zeus']} **Voici vôtre lien :** ||{urlshort}||")

                    
        
        
    
        
def setup(bot):
    bot.add_cog(Urlshort(bot))
    