import discord
from discord import app_commands
import os
from dotenv import load_dotenv
import music

intents = discord.Intents.all()
intents.members = True
load_dotenv()
DISCORD_TOKEN = os.getenv("discord_token")

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f"We have logged in as {self.user}.")

client = aclient()
tree = app_commands.CommandTree(client)
guild = client.guilds

@tree.command(name = 'who', description='Who is Doggo?', guilds=guild)
async def self(interactions: discord.Interaction):
    await interactions.response.send_message("Hi: " + interactions.user.mention + "! My name is Doggo! (Working Title) I am currently in development and will serve as a playground to its developer")

@tree.command(name = 'hi', description='Checks if the bot responds and says hi', guilds=guild)
async def hi(interactions: discord.Interaction):
    await interactions.response.send_message("Hi: " + interactions.user.mention)

# @tree.command(name = "test", description= "testing", guilds=guild)
# async def self(interactions: discord.Interaction, name:str):
#     await interactions.response.send_message(f"Hello {name}")

# @tree.command(name='join', description='Tells the bot to join the voice channel', guilds=guild)
# async def join(ctx):
#     await music.join(ctx)

# @tree.command(name='leave', description='To make the bot leave the voice channel', guilds=guild)
# async def leave(ctx):
#     await music.leave(ctx)

# # TODO: add queue
# @tree.command(name='play_song', help='To play song')
# async def play(ctx, url):
#     await music.play(ctx, url)

# @tree.command(name='pause', help='This command pauses the song')
# async def pause(ctx):
#     await music.pause(ctx)
    
# @tree.command(name='resume', help='Resumes the song')
# async def resume(ctx):
#     await music.resume(ctx)

# @tree.command(name='stop', help='Stops the song')
# async def stop(ctx):
#     await music.stop(ctx)

client.run(DISCORD_TOKEN)