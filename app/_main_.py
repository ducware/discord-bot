import discord
from discord.ext import commands
import yt_dlp as youtube_dl
import asyncio
from gtts import gTTS
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True
intents.voice_states = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Function to load Opus library
if not discord.opus.is_loaded():
    discord.opus.load_opus('libopus.so.0')

@bot.command()
async def play(ctx, url: str):
    await ctx.message.delete()  # Delete the user's command message
    if ctx.author.voice is None:
        await ctx.send("You are not connected to a voice channel.")
        return

    channel = ctx.author.voice.channel

    if not channel.permissions_for(ctx.guild.me).connect:
        await ctx.send("I do not have permission to connect to the voice channel.")
        return

    if not channel.permissions_for(ctx.guild.me).speak:
        await ctx.send("I do not have permission to speak in the voice channel.")
        return

    try:
        voice_client = await channel.connect()
    except discord.ClientException:
        await ctx.send("I am already connected to a voice channel.")
        return
    except discord.errors.InvalidArgument:
        await ctx.send("This is not a valid voice channel.")
        return
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")
        return

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            if 'entries' in info:
                # if playlist, extract the first entry
                info = info['entries'][0]
            url2 = info['url']
            title = info.get('title', 'Unknown title')
            voice_client.play(discord.FFmpegPCMAudio(executable="ffmpeg", source=url2))
        await ctx.send(f'Now playing: {title}')
    except youtube_dl.utils.DownloadError as e:
        await ctx.send(f"Failed to download video: {e}")
    except discord.ClientException as e:
        await ctx.send(f"Failed to play audio: {e}")

@bot.command()
async def leave(ctx):
    await ctx.message.delete()  # Delete the user's command message
    voice_client = ctx.guild.voice_client
    if voice_client and voice_client.is_connected():
        await voice_client.disconnect()
        await ctx.send("Disconnected from the voice channel.")
    else:
        await ctx.send("I am not connected to any voice channel.")

@bot.command()
async def tts(ctx, *, text: str):
    await ctx.message.delete()  # Delete the user's command message
    if ctx.author.voice is None:
        await ctx.send("You are not connected to a voice channel.")
        return

    channel = ctx.author.voice.channel

    if not channel.permissions_for(ctx.guild.me).connect:
        await ctx.send("I do not have permission to connect to the voice channel.")
        return

    if not channel.permissions_for(ctx.guild.me).speak:
        await ctx.send("I do not have permission to speak in the voice channel.")
        return

    try:
        voice_client = await channel.connect()
    except discord.ClientException:
        voice_client = ctx.guild.voice_client
    except discord.errors.InvalidArgument:
        await ctx.send("This is not a valid voice channel.")
        return
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")
        return

    tts = gTTS(text, lang='vi')
    tts.save("tts.mp3")

    if not voice_client.is_playing():
        voice_client.play(discord.FFmpegPCMAudio("tts.mp3"), after=lambda e: os.remove("tts.mp3"))
        await ctx.send("Speaking...")
    else:
        await ctx.send("Already playing audio. Please wait.")

@bot.command()
async def sua(ctx, *, text: str):
    await ctx.message.delete()  # Delete the user's command message
    if ctx.author.voice is None:
        await ctx.send("You are not connected to a voice channel.")
        return

    channel = ctx.author.voice.channel

    if not channel.permissions_for(ctx.guild.me).connect:
        await ctx.send("I do not have permission to connect to the voice channel.")
        return

    if not channel.permissions_for(ctx.guild.me).speak:
        await ctx.send("I do not have permission to speak in the voice channel.")
        return

    try:
        voice_client = await channel.connect()
    except discord.ClientException:
        voice_client = ctx.guild.voice_client
    except discord.errors.InvalidArgument:
        await ctx.send("This is not a valid voice channel.")
        return
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")
        return

    # Prepend the user's name to the text
    text_with_username = f"{ctx.author.display_name} {text}"
    text_to_display = f"{ctx.author.display_name} đã sủa: **{text}**"

    tts = gTTS(text_with_username, lang='vi')
    tts.save("tts.mp3")

    if not voice_client.is_playing():
        voice_client.play(discord.FFmpegPCMAudio("tts.mp3"), after=lambda e: os.remove("tts.mp3"))
        await ctx.send(text_to_display)
    else:
        await ctx.send("Already playing audio. Please wait.")

@bot.command()
async def s(ctx, *, text: str):
    await ctx.message.delete()  # Delete the user's command message
    if ctx.author.voice is None:
        await ctx.send("You are not connected to a voice channel.")
        return

    channel = ctx.author.voice.channel

    if not channel.permissions_for(ctx.guild.me).connect:
        await ctx.send("I do not have permission to connect to the voice channel.")
        return

    if not channel.permissions_for(ctx.guild.me).speak:
        await ctx.send("I do not have permission to speak in the voice channel.")
        return

    try:
        voice_client = await channel.connect()
    except discord.ClientException:
        voice_client = ctx.guild.voice_client
    except discord.errors.InvalidArgument:
        await ctx.send("This is not a valid voice channel.")
        return
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")
        return

    # Prepend the user's name to the text
    text_with_username = f"{ctx.author.display_name} {text}"
    text_to_display = f"{ctx.author.display_name} đã sủa: **{text}**"

    tts = gTTS(text_with_username, lang='vi')
    tts.save("tts.mp3")

    if not voice_client.is_playing():
        voice_client.play(discord.FFmpegPCMAudio("tts.mp3"), after=lambda e: os.remove("tts.mp3"))
        await ctx.send(text_to_display)
    else:
        await ctx.send("Already playing audio. Please wait.")

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

@bot.event
async def on_disconnect():
    print("Bot has disconnected. Attempting to reconnect...")
    while not bot.is_closed():
        try:
            await bot.connect()
            break
        except Exception as e:
            print(f"Reconnection failed: {e}. Retrying in 5 seconds...")
            await asyncio.sleep(5)

bot.run(os.getenv('DISCORD_TOKEN'))
