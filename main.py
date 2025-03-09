import discord
from discord.ext import commands
import asyncio
import random

token = "TOKEN" #THAY TOKEN VÀO (TOKEN CỦA ACC ĐÉO PHẢI CỦA BOT)

bot = commands.Bot(command_prefix='>>', help_command=None, self_bot=True)

# Điền ID user vào để dùng pall
PREDEFINED_MEMBER_IDS = [
    
]

kiss_gifs = [
    "https://media.discordapp.net/attachments/1234435780424761355/1328612566510862367/5hnMXYc.gif?ex=67875660&is=678604e0&hm=0322cd3e202c4459210f1f1d58ce2f27437545f5c312d628284afead221ee16a&=",
    "https://cdn.discordapp.com/attachments/1234435780424761355/1328612567098331146/5x8GZ1f.gif?ex=67875660&is=678604e0&hm=7eff70c277b9888a2d0a6eab99a5555dfdc989d2571f94798862f18f108adf4b&",
    "https://cdn.discordapp.com/attachments/1234435780424761355/1328612568297898096/8HBpNon.gif?ex=67875660&is=678604e0&hm=665f0a5c6fa3b34d62ef04b616f4438745a6ad5102c95ec2ba5eebc896674ac6&",
    "https://cdn.discordapp.com/attachments/1234435780424761355/1328612569279238246/E7CrQXD.gif?ex=67875660&is=678604e0&hm=a46633bbf420520bbad89a5e260a06bc4077dda81b2ee857bdf797d08f979989&",
    "https://cdn.discordapp.com/attachments/1234435780424761355/1328612570873069599/miWzkgu.gif?ex=67875661&is=678604e1&hm=f431150f1b73f432aaa6ed3b5871f9e2fe996c4eda542764a4f73216666ee3ea&"
]

hug_gifs = [
    "https://cdn.discordapp.com/attachments/1234435780424761355/1328612567555244104/7iJ3fQP.gif?ex=67875660&is=678604e0&hm=f547ac8a65cada9ec29b8823016ea7da03f7768d5e1bf13a134cc4ea5e095879&",
    "https://cdn.discordapp.com/attachments/1234435780424761355/1328612568859672657/DXGIwwq.gif?ex=67875660&is=678604e0&hm=32c3ba263dd51def3a3ee9581f62d4f749ce392d243b889b476171271c2c623f&",
    "https://cdn.discordapp.com/attachments/1234435780424761355/1328612569782419457/KYazsrf.gif?ex=67875661&is=678604e1&hm=1b3bd8caaa5f68dc11e5df0bf93254959d30d21a843fa310c9ee8c73aad01e63&",
    "https://cdn.discordapp.com/attachments/1234435780424761355/1328612570223083580/LTv4iQH.gif?ex=67875661&is=678604e1&hm=7192a5f816476eb3c27e83014879eb9e11a4ddc08f66825f22f0c85b47c698cf&",
    "https://cdn.discordapp.com/attachments/1234435780424761355/1328612571716259870/yjGwHpV.gif?ex=67875661&is=678604e1&hm=e9e924137889b480e76861c59216112fe9509339eebf9c0da776cf16960c1379&"
]

images = {
    "ferr": "https://cdn.discordapp.com/attachments/1234435780424761355/1328613588931317780/7fhkVHp.png?ex=67875754&is=678605d4&hm=8d7c3873029b435e24315518ff5379bb4b551eda1f3435876b5034820d6ee1f1&",
    "phambi": "https://media.discordapp.net/attachments/1251234606624276501/1328399466041970834/023V7O9.png?ex=67868fe9&is=67853e69&hm=663d1ac18b2cf2149fa6c5244230327d55878a757fed6f3c4ca2ddefc6fe3139&=&format=webp&quality=lossless&width=559&height=559",
    "ben": "https://cdn.discordapp.com/attachments/1321146582564995232/1328400650966405162/show1.mp4?ex=67869103&is=67853f83&hm=2023b83203802f1c0890b9417685bdae62fd60e72b75253903959891e107c895&"
}

memes = {
    "gaugau": "https://cdn.discordapp.com/attachments/1251234606624276501/1328401519514751088/2024-10-11-06-40-19_1.jpg?ex=678691d2&is=67854052&hm=ccf430aa10da5d832f67ef5f1d56f2f38f3b329d8b179398d10d548ea78d3393&",
    "loli": "https://media.discordapp.net/attachments/1251234606624276501/1328402602190307348/FB_IMG_1713669234818.jpg?ex=678692d4&is=67854154&hm=1fe3ba44a14a1b1459b467a219b0b0ed6d798479d17f1c9c8ed4ee077bc15de5&=&format=webp",
    "kobietnoigi": "https://cdn.discordapp.com/attachments/1251234606624276501/1328402716170649762/FB_IMG_1711885704359.jpg?ex=678692f0&is=67854170&hm=5157ce298583166fc13dc48c11e6f9b928e881b3ecac339308d4c9bf8f5670f6&",
    "liemkhiet": "https://cdn.discordapp.com/attachments/1251234606624276501/1328402647622881320/quality_restoration_202404051513006811.jpg?ex=678692df&is=6785415f&hm=c040d49f56b07a192891fb5bf2f2d5656caa2d1d82db3b4c8b359d6def6aa45e&",
    "cammom": "https://cdn.discordapp.com/attachments/1251234606624276501/1328402521714065522/FB_IMG_1713927026305.jpg?ex=678692c1&is=67854141&hm=de2290475e0aaf759b19c0057fbbe586c11c9c330e840c597d72c0ef5910a9be&",
    "vandekynang": "https://cdn.discordapp.com/attachments/1251234606624276501/1328402414981873798/images.png?ex=678692a8&is=67854128&hm=4601828c4d39b77fdc7a095c4ef496426ae63a19a20a88de80a3346e01262f89&",
    "trongtruonghop": "https://cdn.discordapp.com/attachments/1251234606624276501/1328402379342741514/y2mate.com_-_Trong_truong_hop_nhom_nay_bi_ieu_tra_boi_cac_co_quan_truc_thuoc_bo_cong_an_meme_360p.mp4?ex=6786929f&is=6785411f&hm=420dfc7fe884031389b00c4c762b407e68cd84e419b0ad6ce04356d303ff79d6&",
    "deohai": "https://cdn.discordapp.com/attachments/1251234606624276501/1328402260551667722/VIDEO_DOWNLOAD_1718552805846_1724134162585-1.mp4?ex=67869283&is=67854103&hm=6526776216156ca2e216d27b55a75f8c1f32f58e5b7ae38fd3dd726d305d9d44&",
    "dislike": "https://cdn.discordapp.com/attachments/1251234606624276501/1328402140632187004/sddefault.jpg?ex=67869266&is=678540e6&hm=7e318c8c5f580fb42b0935b72fbc4725cdfb4732419de6e52f8d24c9b4131ca0&",
    "like": "https://cdn.discordapp.com/attachments/1251234606624276501/1328402096495792249/hqdefault.jpg?ex=6786925c&is=678540dc&hm=4ab49c69aa44af2507674efeef7b73a2141b92de4558d9ecfd841817f366ef43&",
    "ughh": "https://cdn.discordapp.com/attachments/1251234606624276501/1328402035451891854/image0.gif?ex=6786924d&is=678540cd&hm=73ef83e5017703a3f1326ee24ed0611108d9b652540ac9b679133eb6047d7824&",
    "backi": "https://cdn.discordapp.com/attachments/1251234606624276501/1328402007672885301/Snaptik.app_7095596052492963099.mp4?ex=67869247&is=678540c7&hm=c7cd1f184e6d91274541606ba3fd45e87cbdf12d5a2ebb920e9f6e52e78eda26&",
    "loitoi": "https://cdn.discordapp.com/attachments/1251234606624276501/1328401944427106344/57434EAD-58DF-41B6-BBA9-0AA2C33BDB06.mov?ex=67869238&is=678540b8&hm=f77beb390e69b0428db26921775743f5ba0d550b60f4ed9841f4881b262fc12b&"
}

qr = {
    "mb": "https://cdn.discordapp.com/attachments/1234435780424761355/1328763019072770169/1717992266759_1.jpg?ex=6787e27e&is=678690fe&hm=6ee8f1ba588d6573791c261d11e231d71c94426557224e7a6c85eb3a1992ab60&",
    "momo": "https://cdn.discordapp.com/attachments/1234435780424761355/1328763019421024297/Screenshot_20240610-110457_1.png?ex=6787e27f&is=678690ff&hm=f7d304cf8c7fa57ee528a8b162f5b8631c3ba8aa3cb576fd66f8687f926001fb&",
    "zlpay": "https://cdn.discordapp.com/attachments/1234435780424761355/1328763019760767048/Picsart_24-10-31_15-05-37-992.jpg?ex=6787e27f&is=678690ff&hm=dc9effe3191e5f28d127ad211b5ee08d71f4ab53de91d425d9ae601eef04dda1&"
}

@bot.event
async def on_ready():
    print(f"Selfbot is ready")

@bot.command()
async def help(ctx):
    message = """```
ping - check ping of bot
pall - sent a message and delete so fast (custom in source code)
info - info of developer
edev - discord server of developer
spam <amount> <content> - spam message
purge <amont> - delete your message
afk <reason>
unafk
kiss <user> - kiss a user
hug <user> - hug a user
show <name image in source code> - show a image
meme <name meme in source code> - show a meme
maqr <name maqr in source code> - show a maqr
msr <content> - spam forever
mst - stop msr
    ```"""
    await ctx.send(message)
    await ctx.message.delete()

@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000) 
    await ctx.send(f'Latency is {latency}ms.')
    
@bot.command()
async def pall(ctx):
    mentions = " ".join(f"<@{user_id}>" for user_id in PREDEFINED_MEMBER_IDS)

    message = await ctx.send(mentions)
    await message.delete()
    await ctx.message.delete()
        
@bot.command()
async def info(ctx):
    message = """# <a:fumospin:1291683859175444501> XUAN QUANG <a:fumospin:1291683859175444501>
> **Facebook:** https://facebook.com/enou456
> **Tiktok:** https://tiktok.com/@enou456
> **Gitlab:** https://gitlab.com/edev-xquang
> **Bento (Bio):** https://bento.me/enou456"""
    await ctx.send(message)
    await ctx.message.delete()

@bot.command()
async def edev(ctx):
    message = """# <a:fumospin:1291683859175444501> XUAN QUANG <a:fumospin:1291683859175444501>
> **Self bot Dev by Xuan Quang**
> **Indie Discord bot Developer**
> discord.gg/enou"""
    await ctx.send(message)
    await ctx.message.delete()

@bot.command()
async def spam(ctx, amount: int, *, message: str):
    for _ in range(amount):
        await ctx.send(message)
        
@bot.command()
async def purge(ctx, amount: int):
    async for msg in ctx.channel.history(limit=amount):
        if msg.author == bot.user:
            await msg.delete()
            
afk_users = {}

@bot.command()
async def afk(ctx, *, reason="I'm busy"):
    global afk_users
    afk_users[ctx.author.id] = reason
    await ctx.send(f"AFK: {reason}")
    
@bot.command()
async def unafk(ctx):
    global afk_users
    if ctx.author.id in afk_users:
        del afk_users[ctx.author.id]
        await ctx.send(f"Welcome back.")
    else:
        await ctx.send(f"You don't afk")
    
@bot.event
async def on_message(message):
    global afk_users

    if message.author.bot:
        return

    for user_id in message.mentions:
        if user_id in afk_users:
            reason = afk_users[user_id]
            user = await bot.fetch_user(user_id)
            await message.channel.send(f"# {reason}")

    if message.reference:
        replied_message = await message.channel.fetch_message(message.reference.message_id)
        if replied_message.author.id in afk_users:
            reason = afk_users[replied_message.author.id]
            await message.channel.send(f"# {reason}")

    await bot.process_commands(message)
    
@bot.command()
async def kiss(ctx, member: discord.Member):
    gif_url = random.choice(kiss_gifs)
    await ctx.send(f"tặng bé một nụ hôn {member.mention}! 💋\n{gif_url}")
    await ctx.message.delete()
    
@bot.command()
async def hug(ctx, member: discord.Member):
    gif_url = random.choice(hug_gifs)
    await ctx.send(f"tặng bé một cái ôm nè {member.mention}! \n{gif_url}")
    await ctx.message.delete()
    
@bot.command()
async def show(ctx, image_name: str):
    if image_name in images:
        image_url = images[image_name]
        await ctx.send(f"{image_url}")
    else:
        await ctx.send("Đéo thấy ảnh")
    await ctx.message.delete()
        
@bot.command()
async def meme(ctx, meme_name: str):
    if meme_name in memes:
        meme_url = memes[meme_name]
        await ctx.send(f"{meme_url}")
    else:
        await ctx.send("Đéo thấy ảnh")
    await ctx.message.delete()
    
@bot.command()
async def maqr(ctx, qr_name: str):
    if qr_name in qr:
        qr_url = qr[qr_name]
        await ctx.send(f"{qr_url}")
    else:
        await ctx.send("Đéo thấy ảnh")
    await ctx.message.delete()

sending_messages = False

@bot.command()
async def msr(ctx, *, content):
    global sending_messages
    if sending_messages:
        return
    sending_messages = True
    while sending_messages:
        await ctx.send(content)
        await asyncio.sleep(2)
        
@bot.command()
async def mst(ctx):
    global sending_messages
    if not sending_messages:
        return
    sending_messages = False
    
bot.run(token)
