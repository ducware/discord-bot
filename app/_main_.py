import discord
from discord.ext import commands
import os
import asyncio
import json

from _rename_ import rename_command
from _tts_ import tts_command
from _utils_ import load_data, save_data, load_name, increment_user_score, get_leaderboard
from _dick_ import dick_command
from _leaderboard_ import leaderboard_command
from _help_ import help_command

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True
intents.voice_states = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Function to load Opus library
if not discord.opus.is_loaded():
  discord.opus.load_opus('libopus.so.0')

user_data = load_data()

# Register commands
bot.add_command(rename_command(bot, user_data, save_data))
bot.add_command(tts_command(bot, load_name))
bot.add_command(dick_command(bot, load_name))
bot.add_command(leaderboard_command(bot, get_leaderboard))
bot.add_command(help_command(bot))


@bot.event
async def on_ready():
  print(f'Bot is ready. Logged in as {bot.user}')


@bot.event
async def on_command(ctx):
  increment_user_score(ctx.author.name)


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
