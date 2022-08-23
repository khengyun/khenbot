import os
import discord
from discord.ext import commands
import os
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
                           description="Sử dụng : kg>lệnh<",
                           color=discord.Color.green())

        em.add_field(name="👉 Lệnh xem ảnh theo yêu cầu 👌 ",
                     value="Lệnh: pic (tên ảnh)\nVd: kgpic mèo")

        em.add_field(name="👉 Lệnh xem ảnh gái🤪👌", value="Lệnh: kgg18 ")
        em.add_field(name="👉 Lệnh xem clip gái🤪👌", value="Lệnh: kgc18")

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
            value="🤘 Facebook : @niraoito \n " + f' stay in {len(client.guilds)} server' + " \n🤘Discord :<@!486547289683525652> ")

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
async def clear(ctx, amount=2):
    try:
        if str(ctx.message.author.id) == ("486547289683525652"):
            await ctx.channel.purge(limit=amount)
        if str(ctx.message.author.id) == ("442669164549898240"):
            await ctx.channel.purge(limit=amount)
        if str(ctx.message.author.id) == ("407781109590392832"):
            await ctx.channel.purge(limit=amount)
    except:
        await ctx.send(
            "Lệnh này hiện tại chỉ dành cho \n<@!486547289683525652>\n<@!442669164549898240>\n<@!407781109590392832>"
        )


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

    await ctx.send(file=discord.File("tiktok/" + str(ran) + ".mp4"))


@client.command(aliases=["c18"])
async def showclip(ctx):
    if ctx.channel.is_nsfw():
        clear(ctx, amount=2)
        ran = random.randint(1, 21)
        await ctx.send(file=discord.File("c18/" + str(ran) + ".mp4"))
    else:
        msg = f"{ctx.author.mention}  Chú ý :Chỉ sử dụng lệnh này trong phòng NSFW"
        await ctx.send(msg)


player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
                     [2, 5, 8], [0, 4, 8], [2, 4, 6]]


@client.command()
async def caro(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [
            ":white_large_square:", ":white_large_square:",
            ":white_large_square:", ":white_large_square:",
            ":white_large_square:", ":white_large_square:",
            ":white_large_square:", ":white_large_square:",
            ":white_large_square:"
        ]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("Đây là lượt của <@" + str(player1.id) + ">")
        elif num == 2:
            turn = player2
            await ctx.send("Đây là lượt của <@" + str(player2.id) + ">")
    else:
        await ctx.send(
            "Có 1 trận đấu đang diễn ra , đợi nó kết thúc trước khi bắt đầu trận mới!!!"
        )


@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:":
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " đã thắng!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("!!!Hòa rồi !!!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send(
                    "Đảm bảo chọn một số nguyên từ 1 đến 9 (bao gồm) và một ô chưa được đánh dấu."
                )
        else:
            await ctx.send("không phải lượt của bạn.")
    else:
        await ctx.send("Làm ơn sử dụng lệnh kgcaro để bắt đầu trận mới")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[
                condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True


@caro.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Hãy mention 2 người chơi để bắt đầu ván đấu.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send(
            "Hãy chắc chắn rằng bạn đã mention hoặc ping 2 người chơi!!!")


@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Làm ơn hãy chọn điểm mà bạn muốn đánh dấu")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Chắc chắn rằng bạn đã chọn 1 số nguyên tố")


@client.command()
async def guess(ctx):

    await ctx.send("đoán số từ 1 đến 10")

    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    choice = random.choice(numbers)

    answer = await client.wait_for("message")

    try:
        if answer.content == choice:
            await ctx.send("Đoán đúng rồi đấy haha")
        else:
            await ctx.send(f"Sai rồi số được chọn là {choice}")
    except:
        pass


keep_alive()

client.run(TOKEN)
