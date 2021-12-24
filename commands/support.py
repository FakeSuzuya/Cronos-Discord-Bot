import nmap
import discord
from discord.ext import commands
import os
import json
import requests
from utils.utils import get_emoji, get_config
from utils.config import emonline, emoffline
from discord_slash import ButtonStyle, SlashCommand
from discord_slash.utils.manage_components import *
from discord.ext import commands
emoji = get_emoji()
configs = get_config()
slash = ""

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        slash = SlashCommand(bot, SlashCommand)
     
    @commands.command()
    async def help(self, ctx):
        bot = self.bot
        imagembed = discord.Embed(color=discord.Colour.from_rgb(255, 255, 255))
        imagembed.set_image(url="https://i.ibb.co/TmHymb6/cronos.png")
        embed = discord.Embed(title="**Cronos Modules !**", description = f"{emoji['zeus']} Support [Join here](https://discord.gg/BSfsxrFBUT)\n**Prefix :** ``{configs['prefix']}``",color = discord.Colour.from_rgb(255, 255, 255))
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_footer(text="Dev by : 2$.py#6495")
        select = create_select(
            options=[
                create_select_option(f"{configs['prefix']}webh00kdel", value="1", emoji={"name": emonline[0],"id": emonline[1]}, description = "- Supprime un webh00k"),
                create_select_option(f"{configs['prefix']}webh00kspam", value="2", emoji={"name": emoffline[0],"id": emoffline[1]},description = "- Spam un webh00k"),
                create_select_option(f"{configs['prefix']}webh00kinfo", value="3", emoji={"name": emonline[0],"id": emonline[1]}, description = "- Information sur un webh00k"),
                create_select_option(f"{configs['prefix']}findwebh00k", value="4", emoji={"name": emoffline[0],"id": emoffline[1]}, description = "- Cherche un webh00k dans un fichier éxécutable"),
                create_select_option(f"{configs['prefix']}proxygen", value="5", emoji={"name": "working","id": "917505948543766659"}, description = "- Génère des proxys"),
                create_select_option(f"{configs['prefix']}ethwalletinfo", value="6", emoji={"name": emonline[0],"id": emonline[1]}, description = "- Information sur un wallet éthereum"),
                create_select_option(f"{configs['prefix']}d3stroytok3n", value="7", emoji={"name": emonline[0],"id": emonline[1]}, description ="- Détruit le c0mpte de quelq'un"),
                create_select_option(f"{configs['prefix']}nftgen", value="8", emoji={"name": emoffline[0],"id": emoffline[1]}, description ="- Génère un nft"),
                create_select_option(f"{configs['prefix']}cryptoinfo", value="9", emoji={"name": emonline[0],"id": emonline[1]}, description ="- Information sur une crypto"),
                create_select_option(f"{configs['prefix']}scanip", value="10", emoji={"name": emonline[0],"id": emonline[1]}, description = "- Scan une ip"),
                create_select_option(f"{configs['prefix']}maketok3ngrab", value="11", emoji={"name": emonline[0],"id": emonline[1]}, description = "- Crée un tok3n grab"),                  
                create_select_option(f"{configs['prefix']}shorturl",value="12",emoji={"name": emonline[0], "id": emonline[1]},description = "- Raccourcis votre url"),
                create_select_option(f"{configs['prefix']}botinfo",value="13",emoji={"name": emonline[0], "id": emonline[1]},description = "- Affiche les informations du bot"),
                create_select_option(f"{configs['prefix']}bug",value="14",emoji={"name": emonline[0], "id": emonline[1]},description = "- Permet de nous faire parvenir une erreur")
            ],

            placeholder="Liste des commandes...",
            min_values=1,
        max_values=1
        )
        x = fait_choix = await ctx.send(embed=imagembed, components=[create_actionrow(select)])

        def check(m):
            return m.author_id == ctx.author.id and m.origin_message.id == fait_choix.id

        choice_ctx = await wait_for_component(bot, components=select, check=check)

        if choice_ctx.values[0]== "1":
            await choice_ctx.send(f"{ctx.author.mention}\n**Usage :** ``{configs['prefix']}webh00kdel <webh00kurl>``")
            await x.delete(delay=0)
        if choice_ctx.values[0]== "2":
            await choice_ctx.send(f"{ctx.author.mention}\n**Usage :** ``{configs['prefix']}webh00kspam <message> <webh00kurl>``")
            await x.delete(delay=0)
        if choice_ctx.values[0]== "3":
            await choice_ctx.send(f"{ctx.author.mention}\n**Usage :** ``{configs['prefix']}webh00kinfo <webhookurl>``")
            await x.delete(delay=0)
        if choice_ctx.values[0]== "4":
            await choice_ctx.send(f"{ctx.author.mention}\n**Usage :** ``{configs['prefix']}findwebh00k <lien_du_fichier>``")
            await x.delete(delay=0)
        if choice_ctx.values[0]== "5":
            await choice_ctx.send(f"{ctx.author.mention}\n**Usage :** ``{configs['prefix']}proxygen <HTTP/HTTPS/SOCKS4/SOCKS5>``")
            await x.delete(delay=0)
        if choice_ctx.values[0]== "6":
            await choice_ctx.send(f"{ctx.author.mention}\n**Usage :** ``{configs['prefix']}ethwalletinfo <wallet_id>``")
            await x.delete(delay=0)
        if choice_ctx.values[0]== "7":
            await choice_ctx.send(f"{ctx.author.mention}\n**Usage :** ``{configs['prefix']}d3stroytok3n <tok3n>``")
            await x.delete(delay=0)
        if choice_ctx.values[0]== "8":
            await choice_ctx.send(f"{ctx.author.mention}\n**Usage :** ``{configs['prefix']}nftgen``")
            await x.delete(delay=0)
        if choice_ctx.values[0]== "9":
            await choice_ctx.send(f"{ctx.author.mention}\n**Usage :** ``{configs['prefix']}cryptoinfo <crypto_name>``")
            await x.delete(delay=0)
        if choice_ctx.values[0]== "10":
            await choice_ctx.send(f"{ctx.author.mention}\n**Usage :** ``{configs['prefix']}scanip <ip>``")
            await x.delete(delay=0)
        if choice_ctx.values[0]== "11":
            await choice_ctx.send(f"{ctx.author.mention}\n**Usage :** ``{configs['prefix']}maketok3ngrab <web00kurl>``")
            await x.delete(delay=0)
        if choice_ctx.values[0]== "12":
            await choice_ctx.send(f"{ctx.author.mention}\n**Usage :** ``{configs['prefix']}shorturl <url>``")
            await x.delete(delay=0)
        if choice_ctx.values[0]== "14":
            await choice_ctx.send(f"{ctx.author.mention}\n**Usage :** ``{configs['prefix']}bug <problem>``")
            await x.delete(delay=0)
        
    
                    
    @commands.command()
    async def botinfo(self, ctx):
        bot = self.bot
        members = 0
        for guild in bot.guilds:
            for member in guild.members:
                members += 1

        embed = discord.Embed(title="**Cronos Inforamtion !**", description = f"{emoji['zeus']} Support [Join here](https://discord.gg/BSfsxrFBUT)\n**Prefix :** ``{configs['prefix']}``",color = discord.Colour.from_rgb(255, 255, 255))
        embed.add_field(name="`Serveurs`",value = f"- {len(bot.guilds)} serveurs !",inline = False)
        embed.add_field(name="`Membre`",value = f"- {members} membres !",inline= False)
        embed.set_thumbnail(url=bot.user.avatar_url)
        embed.set_footer(text="Dev by : 2$.py#6495")
        await ctx.send(embed = embed)
         
    @commands.command()
    async def bug(self, ctx, *, problem):
        with open("./database/botstaff.json","r") as config:
            configs = json.load(config)
            if ctx.author.id in configs["blacklist"]:
                z = await ctx.send(f"{ctx.author.mention}\n{emoji['zeus']} - **Tu es blacklist du bot !**")
                return
        member = self.bot.get_user(755734583005282334)
        await member.send(f"{ctx.author.mention}\n**Bugs :** ``{problem}``")
        await ctx.send(f"{ctx.author.mention}\n{emoji['zeus']} - **Bug envoyé**")
def setup(bot):
    bot.add_cog(Help(bot))