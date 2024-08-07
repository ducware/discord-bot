import discord
from discord.ext import commands


def rename_command(bot, user_data, save_data):

  @commands.command()
  async def r(ctx, *, name: str):
    # Check if the user is trying to tag someone else
    if ctx.message.mentions:
      await ctx.send("Đổi tên cái con cặc")
      return

    await ctx.message.delete()

    # Update the user's own name in the user_data dictionary
    user_data["name"][ctx.author.name] = name

    # Save the updated user data
    save_data(user_data)

    # Notify the user about the name change
    await ctx.send(f"Đổi tên {ctx.author.mention} thành {name}")

  return r
