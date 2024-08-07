import discord
from discord.ext import commands


def help_command(bot):

    @commands.command()
    async def h(ctx):
        await ctx.message.delete()  # Delete the user's command message
        help_message = """
        **Help - List of commands:**
        **!h** - Display this help message.
        **!r <name>** - Change your nickname to <name>.
        **!l** - Display the leaderboard.
        **!tts <message>** - Convert text to speech and play it in a voice channel.
        **!dick <user>** - Check your dick long.
        """
        await ctx.send(help_message)

    return h
