import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import music

load_dotenv()

DISCORD_TOKEN = os.getenv("discord_token")

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix="!",intents=intents)

# Startup Information
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("!who"))

@bot.command(name='who', help='Who is Doggo?')
async def who(ctx):
    await ctx.send("Hi: " + ctx.author.mention + "! My name is Doggo! (Working Title) I am currently in development and will serve as a playground to its developer")

@bot.command(name='hi', help='Checks if the bot responds and says hi')
async def hi(ctx):
    await ctx.send("Hi: " + ctx.author.mention)

# @bot.command()
# async def enter(ctx):
#     if ctx.author.voice:
#         await ctx.message.author.voice.channel.connect()

# @bot.command()
# async def leave(ctx):
#     if ctx.voice_client:
#         await ctx.guild.voice_client.disconnect()

@bot.command(name='join', help='Tells the bot to join the voice channel')
async def join(ctx):
    await music.join(ctx)

@bot.command(name='leave', help='To make the bot leave the voice channel')
async def leave(ctx):
    await music.leave(ctx)

# TODO: add queue
@bot.command(name='play_song', help='To play song')
async def play(ctx, url):
    await music.play(ctx, url, bot)

@bot.command(name='pause', help='This command pauses the song')
async def pause(ctx):
    await music.pause(ctx)
    
@bot.command(name='resume', help='Resumes the song')
async def resume(ctx):
    await music.resume(ctx)

@bot.command(name='stop', help='Stops the song')
async def stop(ctx):
    await music.stop(ctx)

bot.run(DISCORD_TOKEN)