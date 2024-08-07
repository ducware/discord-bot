import discord
from discord.ext import commands


def leaderboard_command(bot, get_leaderboard):

    @commands.command()
    async def l(ctx):
        await ctx.message.delete()  # Delete the user's command message
        leaderboard = get_leaderboard()
        if not leaderboard:
            await ctx.send("No one is on the leaderboard yet!")
            return

        leaderboard_message = "**Leaderboard:**\n"
        medals = ["🥇", "🥈", "🥉"]

        for index, (user, score) in enumerate(leaderboard):
            if index < 3:
                medal = medals[index]
            else:
                medal = "🤔"
            leaderboard_message += f"{medal} {user}: {score} points\n"

        await ctx.send(leaderboard_message)

    return l
