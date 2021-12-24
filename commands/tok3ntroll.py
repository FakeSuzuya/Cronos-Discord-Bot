import nmap
import discord
from discord.ext import commands
import os
import json
import requests
from utils.utils import get_emoji, get_config
import string
import base64
import random
from random import randint
emoji = get_emoji()
configs = get_config()

class Faketok3n(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def tok3n(self, ctx, member : discord.Member):
        token = ''
        base64_string = "=="
        while(base64_string.find("==") != -1):
            sample_string = str(randint(000000000000000000, 999999999999999999))
            sample_string_bytes = sample_string.encode("ascii")
            base64_bytes = base64.b64encode(sample_string_bytes)
            base64_string = base64_bytes.decode("ascii")
        else:
            token = base64_string+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits)
                                                                                  for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
        configs = ""
        with open("./database/botstaff.json","r") as config:
            configs = json.load(config)
            if ctx.author.id not in configs["useradmin"]:
                z = await ctx.send(f"{ctx.author.mention}\n{emoji['zeus']} - **Cet utilisateur n'est pas un admin du bot !**")
                return
            embed = discord.Embed(title=f"**Tok3n de {member.name}**",description=f"||{token}||",color=discord.Colour.from_rgb(255, 255, 255))
            embed.set_thumbnail(url=member.avatar_url)
            await ctx.send(embed=embed)
        

        
    
        
def setup(bot):
    bot.add_cog(Faketok3n(bot))