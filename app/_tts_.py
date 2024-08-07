import discord
from discord.ext import commands
from gtts import gTTS
import os


def tts_command(bot, load_name):

  @commands.command()
  async def s(ctx, *, text: str):
    await ctx.message.delete()  # Delete the user's command message
    if ctx.author.voice is None:
      await ctx.send("You are not connected to a voice channel.")
      return

    channel = ctx.author.voice.channel

    if not channel.permissions_for(ctx.guild.me).connect:
      await ctx.send(
          "I do not have permission to connect to the voice channel.")
      return

    if not channel.permissions_for(ctx.guild.me).speak:
      await ctx.send("I do not have permission to speak in the voice channel.")
      return

    try:
      voice_client = await channel.connect()
    except discord.ClientException:
      voice_client = ctx.guild.voice_client
    except discord.InvalidVoiceChannel:
      await ctx.send("This is not a valid voice channel.")
      return
    except Exception as e:
      await ctx.send(f"An error occurred: {e}")
      return

    # Get the name from the JSON data or use the display name if not added
    user_name = load_name(ctx.author.name) or ctx.author.display_name
    text_with_username = f"{user_name} {text}"
    text_to_display = f"{user_name} đã sủa: **{text}**"

    tts = gTTS(text_with_username, lang='vi')
    tts.save("tts.mp3")

    if not voice_client.is_playing():
      voice_client.play(discord.FFmpegPCMAudio("tts.mp3"),
                        after=lambda e: os.remove("tts.mp3"))
      await ctx.send(text_to_display)
    else:
      await ctx.send("Already playing audio. Please wait.")

  return s
