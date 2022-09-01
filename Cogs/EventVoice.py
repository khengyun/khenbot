import asyncio
import discord
from discord.ext import commands


class EventVoice(commands.Cog):
    def __init__(self, client):
        self.client  = client
    #   MAKE MORE VOICE 
    @commands.Cog.listener()
    async def on_voice_state_update(self,member,before,after):

        if not before.channel and after.channel :
            for guild in self.client.guilds:
                category = discord.utils.get(guild.categories, name="person voice")
                if category is None:
                    category = await guild.create_category('person voice') 
            for check_channel in self.client.guilds:
                check_channel = discord.utils.get(guild.voice_channels, name=f"{member.display_name} Channel") 
                if check_channel is not None:
                    new_voice_channel = check_channel
                else:
                    new_voice_channel = await guild.create_voice_channel(name=f"{member.display_name} Channel",category=category, user_limit= None,position=0)

            await member.move_to(new_voice_channel)
            channel = discord.utils.get(self.client.get_all_channels(), name="notification")
            await channel.send(f'{member.name} has joined ')
            # await channel.send(f'{channel4} has joined the vc')

        if before.channel is not None and after.channel is None : 
            mem=0
            channel = self.client.get_channel(before.channel.id)
            print(channel.category.name)
            for member in channel.members :
                mem+=1
            print("this mem: " + str(mem))
            check_channel = discord.utils.get(self.client.get_all_channels(), name=f"take_your_voice")
            voice_channel = discord.utils.get(self.client.get_all_channels(), name=f"voice")
            if  mem == 0 and check_channel != channel :
                await before.channel.delete()    
            
            await channel.category.delete() 
            channel = discord.utils.get(self.client.get_all_channels(), name="notification")
            await channel.send(f'{member.name} has left')
            print(dir(member))
        else:
            ...

    

    

async def setup(client):
    await client.add_cog(EventVoice(client))
