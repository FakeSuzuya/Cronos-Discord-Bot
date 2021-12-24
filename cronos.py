#SCRIPT MADE BY 2$.py#6495
#If u share this tools on ur discord or another please credit me :) Its free :)

import os, json, sys, time

################################################{IMPORT}################################################################

from utils.utils import clear, close, get_emoji, get_prefix
    
################################################{FONCTION IMPORTATIOn}################################################################
try:
    import discord
    from discord.ext import commands
except:
    os.system("pip install discord.py")
    clear()
try:
    from colorama import init, Fore
except:
    os.system("pip install colorama")
    clear()
try:
    from pystyle import Add, Center, Anime, Colors, Colorate, Write, System #pip install pystyle
except:
    os.system("pip install pystyle")
   
emoji = get_emoji()      
################################################{MODULE IMPORTATION}################################################################

with open("config.json","r") as config:
    configs = json.load(config)

with open("lang.json",'r') as lang:
    language = json.load(lang)

with open("./database/botstaff.json","r") as staff:
    admin = json.load(staff)
    
if configs["token"] == "YOUR_TOKEN":
    print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] {language[configs['lang']]['tokenerror']}")
    close()
    
if configs["prefix"] == "YOUR_PREFIX":
    print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] {language[configs['lang']]['prefixerror']}")
    close()
    
################################################{CONFIG LOAD}#######################################################################

intents = discord.Intents().all()

bot = commands.Bot(command_prefix=configs['prefix'], intents = intents) 
bot.remove_command("help")
###############################################{BOT SETUP}#########################################################################

for file in os.listdir("commands"):
    if file.endswith(".py"):
        name = file[:-3]
        try:
            bot.load_extension(f"commands.{name}")
        except:
            print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] {name} {language[configs['lang']]['commandnotload']}")
            pass
       
@bot.command(hidden=True)
async def load(ctx, module : str):
    if ctx.author.id not in admin["useradmin"]:
        z = await ctx.send(f"{ctx.author.mention}\n{emoji['zeus']} - **Tu n'es pas un admin du bot !**")
        return
    try:
        bot.load_extension(f"commands.{module}")
        await ctx.send(f"{ctx.author.mention}\n{emoji['zeus']} - **Le module ||{module}|| a été chargé !**")
    except Exception as e:

        await ctx.send(f"{ctx.author.mention}\n{emoji['zeus']} - **Le module ||{module}|| est déjà chargé / déchargé !!**")

@bot.command(hidden=True)
async def unload(ctx, module : str):
    if ctx.author.id not in admin["useradmin"]:
        z = await ctx.send(f"{ctx.author.mention}\n{emoji['zeus']} - **Tu n'es pas un admin du bot !**")
        return
    try:
        bot.unload_extension(f"commands.{module}")
        await ctx.send(f"{ctx.author.mention}\n{emoji['zeus']} - **Le module ||{module}|| a été déchargé !**")
    except Exception as e:

        await ctx.send(f"{ctx.author.mention}\n{emoji['zeus']} - **Le module ||{module}|| est déjà chargé / déchargé !!**")

@bot.command(name='reload', hidden=True)
async def _reload(ctx, module : str):
    if ctx.author.id not in admin["useradmin"]:
        z = await ctx.send(f"{ctx.author.mention}\n{emoji['zeus']} - **Tu n'es pas un admin du bot !**")
        return
    try:
        bot.unload_extension(f"commands.{module}")
        bot.load_extension(f"commands.{module}")
        await ctx.send(f"{ctx.author.mention}\n{emoji['zeus']} - **Le module ||{module}|| a été rechargé !**")
    except Exception as e:
        await ctx.send(f"{ctx.author.mention}\n{emoji['zeus']} - **Le module ||{module}|| est déjà chargé / déchargé !!**")
 
###############################################{LOAD COMMANDS}#####################################################################
try:
    bot.run(configs["token"])
except:
    print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] {language[configs['lang']]['errorconnectbot']}")
    close()