import nmap
import discord
from discord.ext import commands
import os
import json
import requests
from utils.utils import get_emoji
emoji = get_emoji()

class Webhook(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def webh00kdel(self, ctx, webhookurl):
        try:
            resp = requests.get(webhookurl)
            if 'Unknown Webhook' not in resp.text:  
                await ctx.send(f"{ctx.author.mention}\n{emoji['zeus']} - **Webhook détruit !**")        
                requests.delete(webhookurl)
            else:
                await ctx.send(f"{ctx.author.mention}\n{emoji['zeus']} - **Webhook introuvable !**")   
        except:
            pass 
        
    @commands.command()
    async def webh00kinfo(self,ctx, webhookurl):
        resp = requests.get(webhookurl)
        webinfo = resp.json()
        if 'Unknown Webhook' not in resp.text:  
            embed = discord.Embed(title = "Webhook Info",description=f"**__Requested by :__** {ctx.author.mention}\n\n**__Webhook URL :__** ```{webhookurl}```", color =discord.Colour.from_rgb(255, 255, 255))
            embed.add_field(name = "**Name :**",value = webinfo['name'], inline=False)
            embed.add_field(name = "**Avatar :**",value = webinfo['avatar'], inline=False)
            embed.add_field(name = "**Token :**",value = f"``{webinfo['token']}``", inline=False)
            embed.add_field(name = "**Guild ID :**",value = f"``{webinfo['guild_id']}``", inline=False)
            embed.add_field(name = "**Channel ID :**",value = f"``{webinfo['channel_id']}``", inline=False)
            await ctx.send(embed=embed)                   
        else:
            await ctx.send(f"{ctx.author.mention}\n{emoji['zeus']} - **Webhook introuvable !**")   
        
                    
        
        
    
        
def setup(bot):
    bot.add_cog(Webhook(bot))