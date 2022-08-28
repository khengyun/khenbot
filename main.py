import os
import discord
from discord.ext import commands
from googleapiclient.discovery import build
from replit import db
from keep_alive import keep_alive
import time


from googletrans import Translator
from pytube import YouTube
import aiohttp
import random
import subprocess
#! Import this

TOKEN = os.environ['token']


intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="kg", intents=intents)

client.remove_command("help")
api_key = "AIzaSyDTZlrARJTPUQG4wBxzlhWiwb1-1iC0fk8"


@client.group(invoke_without_command=True)
async def help(ctx):
    if ctx:
        em = discord.Embed(title="☠☠☠☠☠LỆNH CÓ THỂ SỬ DỤNG ☠☠☠☠☠ ",
                           description="(～￣▽￣)～ " + f'{len(client.guilds)}'+" servers connected",
                           color=discord.Color.green())

        em.add_field(name="👉 Lệnh xem ảnh theo yêu cầu 👌 ",
                     value="Lệnh: pic (tên ảnh)\nVd: kgpic mèo")

        em.add_field(name="👉 Lệnh xem ảnh gái👌", value="Lệnh: kgg18 ")
        em.add_field(name="👉 Lệnh xem clip gái👌", value="Lệnh: kgc18")

        em.add_field(
            name="👉 Lệnh dịch thuật👌",
            value=
            "Lệnh: kgtrans <ngôn ngữ cần dịch sang> <text cần dịch>\n Vd: kgtrans en anh yêu em "
        )

        em.add_field(name="👉 Xem video tiktok 👌", value="Lệnh: kgtiktok")

        em.add_field(name="👉 Xem ảnh pet 👌", value="Lệnh: kgcat , kgdog")

        em.add_field(
            name="👉Lệnh xóa tin nhắn 🤧",
            value="Gõ kgclear >số lượng tin nhắn cần xóa< \n Vd :kgclear 100")

        em.add_field(
            name="👑..........Khag..........👑  ",
            value="🤘 Facebook : [@niraoitoo](https://www.facebook.com/niraitoo) " + " \n🤘Discord :<@!486547289683525652> ")

        await ctx.send(embed=em)
    else:
        await ctx.send(" Gõ kghelp để xem chi tiết lệnh có thể dùng được !!!")


@client.event
async def on_ready():
    print("!!! Bot join !!!\n")
    print("pip install googletrans==3.1.0a0")


@client.command()
async def dog(ctx):
    async with aiohttp.ClientSession() as session:
        request = await session.get('https://some-random-api.ml/img/dog')
        dogjson = await request.json()
        # This time we'll get the fact request as well!
        request2 = await session.get('https://some-random-api.ml/facts/dog')
        factjson = await request2.json()

    embed = discord.Embed(title="Doggo!!!!", color=discord.Color.purple())
    embed.set_image(url=dogjson['link'])

    translator = Translator()
    a = translator.translate(factjson['fact'], dest="vi")
    text = ("Sự thật thú vị : " + a.text)
    embed.set_footer(text=text)
    await ctx.send(embed=embed)


@client.command()
async def cat(ctx):
    async with aiohttp.ClientSession() as session:
        request = await session.get('https://some-random-api.ml/img/cat')
        dogjson = await request.json()
        # This time we'll get the fact request as well!
        request2 = await session.get('https://some-random-api.ml/facts/cat')
        factjson = await request2.json()

    embed = discord.Embed(title="Kitty!!!!", color=discord.Color.purple())
    embed.set_image(url=dogjson['link'])

    translator = Translator()
    a = translator.translate(factjson['fact'], dest="vi")
    text = ("Sự thật thú vị : " + a.text)
    embed.set_footer(text=text)

    await ctx.send(embed=embed)


@client.command()
async def clear(ctx, amount=3):
    # admin_user = []
    admin_user = ["486547289683525652"]
    try:
        if str(ctx.message.author.id)  in admin_user:
          await ctx.channel.purge(limit=amount)
        else:
          if amount>10:
            await ctx.send("Bị giới hạn ở 10.\nLiên hệ chi tiết Creator:<@!486547289683525652> ")
            
        #   await ctx.send(
        #     "Lệnh này hiện tại chỉ dành cho \nCreator:<@!486547289683525652>"
        # )

    except:
        await ctx.send("Đã xảy ra lỗi, thử lại sau!!!")
        

@client.command(aliases=["trans"])
async def translate(ctx, lang, *, args):
    translator = Translator()

    a = translator.translate(args, dest=lang)
    await ctx.send(a.text)


@client.command(aliases=["pic"])
async def showpic(ctx, *, search):
    ran = random.randint(0, 10)
    try:
        resource = build("customsearch", "v1", developerKey=api_key).cse()
        result = resource.list(q=f"{search}",
                               cx="0a1b9741666a22d3a",
                               searchType="image").execute()
        url = result["items"][ran]["link"]
        embed1 = discord.Embed(title=f"Ảnh của bạn ({search.title()})")
        embed1.set_image(url=url)
        await ctx.send(embed=embed1)
    except:
        pass


@client.command(aliases=["g18"])
async def showgirl(ctx):
    if ctx.channel.is_nsfw():
        ran = random.randint(1, 166)
        ran = random.randint(1, 166)
        await ctx.send(file=discord.File("g18/" + str(ran) + ".jpg"))
    else:
        msg = f"{ctx.author.mention} Chú ý :Chỉ sử dụng lệnh này trong phòng #nsfw"
        await ctx.send(msg)


@client.command(aliases=["b18"])
async def showboy(ctx):
    if ctx.channel.is_nsfw():
        ran = random.randint(1, 31)
        await ctx.send(file=discord.File("b18/" + str(ran) + ".jpg"))
    else:
        msg = f"{ctx.author.mention} Chú ý :Chỉ sử dụng lệnh này trong phòng NSFW"
        await ctx.send(msg)
        time.sleep(3)
        await ctx.channel.purge(2)


@client.command(aliases=["tiktok"])
async def tik(ctx):
    ran = random.randint(1, 19)

    # await ctx.send(file=discord.File("tiktok/" + str(ran) + ".mp4"))
    await ctx.send("Lệnh này đang thuộc giai đoạn beta")


@client.command(aliases=["c18"])
async def showclip(ctx):
    if ctx.channel.is_nsfw():
        clear(ctx, amount=2)
        ran = random.randint(1, 21)
        await ctx.send(file=discord.File("c18/" + str(ran) + ".mp4"))
    else:
        msg = f"{ctx.author.mention}  Chú ý :Chỉ sử dụng lệnh này trong phòng NSFW"
        await ctx.send(msg)





keep_alive()

client.run(TOKEN)
