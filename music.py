# Code Credits: github.com/pawel02 - Code got changed to my needs but is inspired by them

import discord
from youtube_dl import YoutubeDL

FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
YDL_OPTIONS = {'format': 'bestaudio/best', 'noplaylist': 'True'}
music_queue = []
is_playing = False
is_paused = False

async def play_next(interactions):
    global is_playing
    global is_paused
    if len(music_queue) > 0:
        voice = interactions.guild.voice_client
        is_playing = True

        # remove the first element cuz playing
        music_queue.pop(0)

        # get first url
        m_url = music_queue[0]
        # ** collects all keyword arguments in a dictionary
        voice.play(await discord.FFmpegOpusAudio.from_probe(
            m_url, **FFMPEG_OPTIONS), after=lambda e: play_next())
    else:
        is_playing = False
        await interactions.guild.voice_client.disconnect()
        await interactions.response.send_message("No more songs in queue! Disconnecting")

async def disc(interactions):
    interactions.guild.voice_client.disconnect()

async def play(interactions, args):
    global is_playing
    global is_paused
    url1 = args.split(" ")
    url2 = url1[0].replace("[","")
    url = url2.replace("]","")
    
    channel = interactions.user.voice.channel
    voice = interactions.guild.voice_client
    #if bot is already in a channel -> move
    if voice and voice.is_connected():
        await voice.move_to(channel)
    elif not channel:
        await interactions.response.send_message("You are not connected to a channel!", ephemeral=True)
    else:
        #if bot is not already in channel connect
        voice = await channel.connect()
    ydl = YoutubeDL(YDL_OPTIONS)
    with ydl:
        info = ydl.extract_info(url, download=False)
        I_URL = info['formats'][0]['url']
        # print(I_URL)
        source = await discord.FFmpegOpusAudio.from_probe(I_URL, **FFMPEG_OPTIONS)
        if is_playing == False:
            music_queue.append(I_URL)
            voice.play(source, after=lambda e: play_next(interactions))
            is_playing = True
        else:
            music_queue.append(I_URL)

async def pause(interactions):
    global is_playing
    global is_paused
    if is_playing:
        is_playing = False
        is_paused = True
        interactions.guild.voice_client.pause()
    elif is_paused:
        is_playing = True
        is_paused = False
        interactions.guild.voice_client.resume()


async def resume(interactions):
    global is_playing
    global is_paused
    if is_paused:
        is_playing = True
        is_paused = False
        interactions.guild.voice_client.resume()


async def skip(interactions):
    if interactions.guild.voice_client != None and interactions.guild.voice_client:
        interactions.guild.voice_client.stop()
        await play_next(interactions)


async def queue(interactions):
    retval = ""
    for i in range(0, len(music_queue)):
        # display a max of 5 songs in queue
        if (i > 4):
            break
        retval += music_queue[i] + "\n"
    if retval != "":
        await interactions.response.send_message(retval)
    else:
        await interactions.response.send_message("No music in queue")


async def clear(interactions):
    global is_playing
    global music_queue
    if interactions.guild.voice_client != None and is_playing:
        interactions.guild.voice_client.stop()
    music_queue = []
    await interactions.response.send_message("Music queue cleared")


async def leave(interactions):
    global is_playing
    global is_paused
    is_playing = False
    is_paused = False
    await interactions.guild.voice_client.disconnect()
