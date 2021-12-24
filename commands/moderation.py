import nmap
import discord
from discord.ext import commands
import os
import json
import requests
from utils.utils import get_emoji
emoji = get_emoji()


    
class BotAdmin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

        
    @commands.command()
    async def adminadd(self, ctx, member : discord.Member):
        configs = ""
        with open("./database/botstaff.json","r") as config:
            configs = json.load(config)
            if member.id in configs["useradmin"]:
                z = await ctx.send(f"{ctx.author.mention}\n{emoji['zeus']} - **Cet utilisateur est déjà un admin du bot !**")
                return
            if ctx.author.id not in configs['useradmin']:
                z = await ctx.send(f"{ctx.author.mention}\n{emoji['zeus']} - **Tu n'es pas un admin du bot !**")
                return
        with open("./database/botstaff.json","w+") as config:
            configs["useradmin"].append(member.id)
            json.dump(configs, config)
            z = await ctx.send(f"{ctx.author.mention}\n{emoji['zeus']} - ||{member.name}|| **ajouté à la liste des admins du bot !**")
        
        
    @commands.command()
    async def adminremove(self, ctx, member : discord.Member):
        configs = ""
        with open("./database/botstaff.json","r") as config:
            configs = json.load(config)
            if member.id not in configs["useradmin"]:
                z = await ctx.send(f"{ctx.author.mention}\n{emoji['zeus']} - **Cet utilisateur n'est pas un admin du bot !**")
                return
            if ctx.author.id not in configs['useradmin']:
                z = await ctx.send(f"{ctx.author.mention}\n{emoji['zeus']} - **Tu n'es pas un admin du bot !**")
                return
        with open("./database/botstaff.json","w+") as config:
            configs["useradmin"].remove(member.id)
            json.dump(configs, config)
            z = await ctx.send(f"{ctx.author.mention}\n{emoji['zeus']} - ||{member.name}|| **supprimé de la liste des admins du bot !**")
            
    @commands.command()
    async def admin(self, ctx):
        embed = discord.Embed(title="**Cronos Admin !**", description = "*Le staff peut agir sur le bot* !",color = discord.Colour.from_rgb(255, 255, 255))
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_footer(text="Bot by 2$.py#6495")
        with open("./database/botstaff.json","r") as config:
            configs = json.load(config)
            x = 1
            for i in configs['useradmin']:
                embed.add_field(name=f"Admin #{x}",value=f"<@{i}>")
                x += 1
        await ctx.send(embed=embed)
        
        
    @commands.command()
    async def bl(self, ctx, member : discord.Member):
        configs = ""
        with open("./database/botstaff.json","r") as config:
            configs = json.load(config)
            if member.id in configs["blacklist"]:
                z = await ctx.send(f"{ctx.author.mention}\n{emoji['zeus']} - **Cet utilisateur est déjà un admin du bot !**")
                return
            if ctx.author.id not in configs['useradmin']:
                z = await ctx.send(f"{ctx.author.mention}\n{emoji['zeus']} - **Tu n'es pas un admin du bot !**")
                return
        with open("./database/botstaff.json","w+") as config:
            configs["blacklist"].append(member.id)
            json.dump(configs, config)
            z = await ctx.send(f"{ctx.author.mention}\n{emoji['zeus']} - ||{member.name}|| **ajouté à la liste des blacklist du bot !**")
        
        
    @commands.command()
    async def blremove(self, ctx, member : discord.Member):
        configs = ""
        with open("./database/botstaff.json","r") as config:
            configs = json.load(config)
            if member.id not in configs["blacklist"]:
                z = await ctx.send(f"{ctx.author.mention}\n{emoji['zeus']} - **Cet utilisateur n'est pas blacklist du bot !**")
                return
            if ctx.author.id not in configs['useradmin']:
                z = await ctx.send(f"{ctx.author.mention}\n{emoji['zeus']} - **Tu n'es pas un admin du bot !**")
                return
        with open("./database/botstaff.json","w+") as config:
            configs["blacklist"].remove(member.id)
            json.dump(configs, config)
            z = await ctx.send(f"{ctx.author.mention}\n{emoji['zeus']} - ||{member.name}|| **supprimé de la liste des blacklist du bot !**")
def setup(bot):
    bot.add_cog(BotAdmin(bot))