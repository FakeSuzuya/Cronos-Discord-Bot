import nmap
import discord
from discord.ext import commands
import os
import json
import requests
from utils.utils import get_emoji
import subprocess
emoji = get_emoji()

class Proxy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def proxygen(self, ctx, protocol):
        protocol = protocol.lower()
        if protocol not in ["http","https","socks5","socks4"]:
            await ctx.send(f"{emoji['zeus']} - {ctx.author.mention} veuillez entrer un protocole valide ``http, https, socks4, socks5``")
            return
        await ctx.send(f"{emoji['zeus']} - {ctx.author.mention} lancement du proxy gen !")
        try:
            os.popen(f"python3 proxyscrap/proxyScraper.py -p {protocol}")
            os.popen(f"python3 proxyscrap/proxyChecker.py -t 20 -s google.com -l {protocol}.txt")
        except Exception as err:
            print(err)
            
        await ctx.channel.send(file=discord.File(f'{protocol}.txt'))
        await ctx.channel.send(ctx.author.mention)
            
        
def setup(bot):
    bot.add_cog(Proxy(bot))