import random
from discord.ext import commands
from setuptools import Command

class _8ballEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        
        @bot.command(aliases=['8ball'])
        async def _8ball(ctx, message):
            # 8ball responses
            responses = [
                "It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful.",
                ]
            # picks a random response from the list and sends to user
            random.shuffle(responses)
            randomitem = responses[random.randrange(0, len(responses))]
            await ctx.send(randomitem)
        
def setup(bot):
    bot.add_cog(_8ballEvent(bot))