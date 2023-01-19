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
    await interactions.response.send_message("Hi: " + interactions.user.mention + "! My name is Doggo! (Working Title) I am currently in development and will serve as a playground to its developer", ephemeral=True)

@tree.command(name = 'hi', description='If you say Hi, Doggo say Hi', guilds=guild)
async def self(interactions: discord.Interaction):
    await interactions.response.send_message("Hi: " + interactions.user.mention, ephemeral=True)

@tree.command(name='join', description='Doggo will join voice channel', guilds=guild)
async def self(interactions: discord.Interaction):
    await basic_func.join(interactions)

@tree.command(name='leave', description='Doggo will leave voice channel', guilds=guild)
async def self(interactions: discord.Interaction):
    await basic_func.leave(interactions)

@tree.command(name='play', description='Give Doggo a YouTube url and Doggo will play music ', guilds=guild)
async def self(interactions: discord.Interaction, url:str):
    await music.play(interactions, url)

@tree.command(name='pause', description='Doggo will pause his music', guilds=guild)
async def self(interactions: discord.Interaction):
    await music.pause(interactions)
    
@tree.command(name='resume', description='Doggo will resume his music', guilds=guild)
async def self(interactions: discord.Interaction):
    await music.resume(interactions)

@tree.command(name='stop', description='Doggo stops play music', guilds=guild)
async def self(interactions: discord.Interaction):
    await music.leave(interactions)

@tree.command(name='skip', description='Doggo skips current song', guilds=guild)
async def self(interactions: discord.Interaction):
    await music.skip(interactions)

@tree.command(name='queue', description='Doggo shows current song queue', guilds=guild)
async def self(interactions: discord.Interaction):
    await music.queue(interactions)

@tree.command(name='clear', description='Doggo clears current song queue', guilds=guild)
async def self(interactions: discord.Interaction):
    await music.clear(interactions)

client.run(DISCORD_TOKEN)