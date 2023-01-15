import asyncio
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import youtube_dl

load_dotenv()

DISCORD_TOKEN = os.getenv("discord_token")
print(DISCORD_TOKEN)


# youtube_dl.utils.bug_reports_message = lambda: ''
ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}
ffmpeg_options = {
    'options': '-vn'
}
ytdl = youtube_dl.YoutubeDL(ytdl_format_options)
class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""
    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix="!",intents=intents)

@bot.command(name='who', help='Who is Doggo?')
async def who(ctx):
    await ctx.send("Hi: " + ctx.author.mention + "! My name is Doggo! (Working Title) I am currently in development and will server as a playground to its developer")

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
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()

@bot.command(name='leave', help='To make the bot leave the voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")

@bot.command(name='play_song', help='To play song')
async def play(ctx,url):
    try :
        if ctx.author.voice:
            await ctx.message.author.voice.channel.connect()
        server = ctx.message.guild
        voice_channel = server.voice_client
        async with ctx.typing():
            filename = await YTDLSource.from_url(url, loop=bot.loop)
            voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
        # await ctx.send('**Now playing:** {}'.format(filename))
    except:
        await ctx.send("The bot is not connected to a voice channel.")

@bot.command(name='pause', help='This command pauses the song')
async def pause(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        voice_client.pause()
    else:
        await ctx.send("The bot is not playing anything at the moment.")
    
@bot.command(name='resume', help='Resumes the song')
async def resume(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_paused():
        voice_client.resume()
    else:
        await ctx.send("The bot was not playing anything before this. Use play_song command")#

@bot.command(name='stop', help='Stops the song')
async def stop(ctx):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        voice_client.stop()
    else:
        await ctx.send("The bot is not playing anything at the moment.")

bot.run(DISCORD_TOKEN)