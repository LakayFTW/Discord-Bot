import discord
from discord import app_commands
import os
from dotenv import load_dotenv
import music
import basic_func
import test

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

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("/who"))

@tree.command(name = 'who', description='Who is Doggo?', guilds=guild)
async def self(interactions: discord.Interaction):
    await interactions.response.send_message("Hi: " + interactions.user.mention + "! My name is Doggo! (Working Title) I am currently in development and will serve as a playground to its developer")

@tree.command(name = 'hi', description='Checks if the bot responds and says hi', guilds=guild)
async def self(interactions: discord.Interaction):
    await interactions.response.send_message("Hi: " + interactions.user.mention)

@tree.command(name='join', description='Tells the bot to join the voice channel', guilds=guild)
async def self(interactions: discord.Interaction):
    await basic_func.join(interactions)

@tree.command(name='leave', description='To make the bot leave the voice channel', guilds=guild)
async def self(interactions: discord.Interaction):
    await basic_func.leave(interactions)

@tree.command(name='play', description='To play song', guilds=guild)
async def self(interactions: discord.Interaction, url:str):
    await music.play(interactions, url)

@tree.command(name='pause', description='This command pauses the song', guilds=guild)
async def self(interactions: discord.Interaction):
    await music.pause(interactions)
    
@tree.command(name='resume', description='Resumes the song', guilds=guild)
async def self(interactions: discord.Interaction):
    await music.resume(interactions)

@tree.command(name='stop', description='Stops the song', guilds=guild)
async def self(interactions: discord.Interaction):
    await music.leave(interactions)

@tree.command(name='skip', description='Skips the current song', guilds=guild)
async def self(interactions: discord.Interaction):
    await music.skip(interactions)

@tree.command(name='queue', description='Shows the current song queue', guilds=guild)
async def self(interactions: discord.Interaction):
    await music.queue(interactions)

@tree.command(name='clear', description='Clears the current song queue', guilds=guild)
async def self(interactions: discord.Interaction):
    await music.clear(interactions)

client.run(DISCORD_TOKEN)