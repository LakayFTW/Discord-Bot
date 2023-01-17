async def join(interactions):
    if not interactions.user.voice.channel:
        await interactions.response.send_message("{} is not connected to a voice channel".format(interactions.user.mention))
        return
    else:
        channel = interactions.user.voice.channel
    await channel.connect()
    await interactions.response.send_message("Joined voice channel")

async def leave(interactions):
    voice_client = interactions.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
        await interactions.response.send_message("left the voice channel")
    else:
        await interactions.response.send_message("The bot is not connected to a voice channel.")