from ast import alias
import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        for guilds in self.client.guilds:
            print(guilds.members)
        print("========================")
    @commands.command(allias="halp")
    async def help(self,ctx):
            em = discord.Embed(title="Notification",
                            description="(～￣▽￣)～ " + f'{[guilds for guilds  in self.client.guilds]}'+" servers connected",
                            color=discord.Color.red())

            em.add_field(
                name="👑..........Khag..........👑  ",
                value="🤘 Facebook : [@niraoitoo](https://www.facebook.com/niraitoo) " + " \n🤘Discord :<@!486547289683525652> ")

            await ctx.send(embed=em)



async def setup(client):
    await client.add_cog(Help(client))
