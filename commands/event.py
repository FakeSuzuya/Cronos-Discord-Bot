import discord, os
from discord.ext import commands
from colorama import init, Fore
init()
import json
import shutil

with open("config.json","r") as config:
    configs = json.load(config)

with open("lang.json",'r') as lang:
    language = json.load(lang)
 
with open("./database/botstaff.json","r") as config:
    staff = json.load(config)    
class Event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        configs = ""
        members = 0
        for guild in self.bot.guilds:
            for member in guild.members:
                members += 1
        os.system("clear")
        print(f"{Fore.RED}========================================================{Fore.WHITE}".center(shutil.get_terminal_size().columns))
        print(f">>>> Bot connecté à {Fore.YELLOW}{self.bot.user}{Fore.WHITE} !".center(shutil.get_terminal_size().columns))
        print(f">>>> You have {Fore.YELLOW}{members}{Fore.WHITE} members !".center(shutil.get_terminal_size().columns))
        print(f">>>> You are on {Fore.YELLOW}{len(self.bot.guilds)}{Fore.WHITE} discord servers !".center(shutil.get_terminal_size().columns))
        print(f"{Fore.RED}========================================================{Fore.WHITE}".center(shutil.get_terminal_size().columns))
        with open("config.json","r") as config:
            configs = json.load(config)
        await self.bot.change_presence(activity=discord.Game(name=f"Prefix : {configs['prefix']}"))



def setup(bot):
    bot.add_cog(Event(bot))