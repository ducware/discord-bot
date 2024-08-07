import discord
from discord.ext import commands
import random


def dick_command(bot, load_name):

  @commands.command()
  async def d(ctx, user: discord.Member = None):
    await ctx.message.delete()  # Delete the user's command message
    if user is None:
      num_equals = random.randint(1, 20)  # Random
      eggplant = '8' + '=' * num_equals + 'D'
      text = f'Cu của {ctx.author.mention}: '
      await ctx.send(text + f"**{eggplant}**")
    else:
      num_equals = random.randint(1, 20)  # Random
      eggplant = '8' + '=' * num_equals + 'D'
      user_name = load_name(user.name) or user.display_name
      text = f'Cu của {user.mention}: '
      await ctx.send(text + f"**{eggplant}**")

  return d
