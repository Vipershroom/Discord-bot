import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

testing_servers = [684237072827154435, 920013664604553246]
prefix = "$"
global cmdList 
cmdList = """
```
help Displays all commands
$random Gives you a random number
$hello Gives you a hello
$echo Echo
```
"""

bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")

# Welcome message for when the bot comes online      
@bot.event
async def on_ready():
    print(f"{bot.user} Has logged on")
    await bot.change_presence(activity=discord.Game("Foobar"))
    for server in bot.guilds:
        print(server)

# Filters out messages that don't start with the $ sign
@bot.event
async def on_message(message):
    try:
        if message.author == bot.user:
            return
        elif message.content[0] != "$":
            return
    except IndexError:
        return "Their was an error handling the message"
    
    # Initializes the user who sent the message along with grabbing message content
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f"{username}: {user_message} ({channel})")
    await bot.process_commands(message)
    
@bot.command(aliases=['help'])
async def helpcommand(ctx):
    response =  cmdList
    await ctx.send(response)
    
@bot.command()
async def echo(ctx, message):
    message = str(message)[2:-3]
    await ctx.send(message)
    
    
    
@bot.command(aliases=['random'])
async def randomnum(ctx):
    response = f"This is your random number, {random.randint(1, 1000)}"
    await ctx.send(response)
    
@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")
    
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
        
@bot.command()
async def spinbottle(ctx):
    pass

@_8ball.error
async def _8ball_error(ctx,error):
    await ctx.send("8Ball needs a question")
    
@echo.error
async def echo_error(ctx, error):
    await ctx.send("Nothing to echo :(")

# slash commands
@bot.slash_command(guild_ids=testing_servers, name="hello", description="Says hello")
async def hello(ctx):
    await ctx.respond("Hello!")
    return
 
@bot.slash_command(guild_ids=testing_servers, name="random", description="Generates a random number")
async def random_num(ctx):
    response = f"This is your random number, {random.randint(1, 1000)}"
    await ctx.respond(response)

@bot.slash_command(guild_ids=testing_servers, name="help", description="Displays all $ commands")
async def help(ctx):
    response = cmdList
    await ctx.respond(response)

@bot.slash_command(guild_ids=testing_servers, name="echo", description="Echos the displayed message")
async def echo(ctx, message):
    await ctx.respond(message)
    
@bot.slash_command(guild_ids=testing_servers, name="8ball", description="Ask the 8ball anything")
async def eightball(ctx, message):
        # 8ball responses
        msg = message
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
        await ctx.respond(randomitem)
    
bot.run(TOKEN)