import nmap
import discord
from discord.ext import commands
import os
import json

nm = nmap.PortScanner()
nma = nmap.PortScannerAsync()


def callback_result(host, scan_result):
    print(host, scan_result)

class Scan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def scanip(self, ctx, ip):
        with open("./commands/scan.json", 'w') as file:
            x = nm.scan(ip, '22-4000')
            json.dump(x, file, indent = 4)
        await ctx.channel.send(file=discord.File('./commands/scan.json'))
        await ctx.channel.send(ctx.author.mention)
    

        
def setup(bot):
    bot.add_cog(Scan(bot))