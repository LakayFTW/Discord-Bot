# Discord Bot Project

## Installation
### Python Requirements
- Python packages see requirements.txt

### youtube_dl - ffmpeg.exe
~~You will need an ffmpeg.exe in your environment or an path to the .exe~~
~~- ffmpeg.exe -> https://github.com/BtbN/FFmpeg-Builds/releases~~
- This is no longer needed on the slash-commands branch since the basic functionality of the music bot has been changed.

### Discord Bot Token
To start the bot you will need your bot token. You can find it at your "Discord Developer Portal" Dashboard </br>
Create an .env file
```
discord_token = "your_token"
```

## Functionality
At the moment the bot can:
- Explain `/who` the bot is
- say `/hi`
- `/join`  and `/leave` voice channels
- `/play`, `/pause`, `/resume`, `/stop`, `/skip` music
- show the `/queue` and `/clear` the queue 