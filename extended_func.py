async def purge(interactions, amnt=None):
    if amnt == None:
        await interactions.channel.purge(limit = 1000000)
    else:
        try:
            int(amnt)
        except: # error handler
            await interactions.resopnse.send_message("Please enter a valid integer amount!")
        else:
            await interactions.channel.purge(limit=amnt)
