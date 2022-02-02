import re
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random
from discord.utils import get
from numpy import true_divide

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
testing_servers = [684237072827154435, 920013664604553246]
server_ids = []
prefix = "$"
global cmdList 
cmdList = """
```
help Displays all commands
$random Gives you a random number
$hello Gives you a hello
$echo Echo
$8ball Ask the magic 8ball
$pen Displays your pen size
$spinbottle spin the bottle, who will it land on?
$avatar Displays the avatar of anyone mentioned
$throw throw something at someone
```
"""

bot = commands.Bot(command_prefix=prefix, intents = intents)
bot.remove_command("help")

# Welcome message for when the bot comes online      
@bot.event
async def on_ready():
    print(f"{bot.user} Has logged on")
    await bot.change_presence(activity=discord.Game("Foobar"))
    for server in bot.guilds:
        print(server)
        server_ids.append(server.id)
    print(server_ids)

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
    message = str(message)
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
async def pen(ctx, *arg):
    pickle = random.randint(1,12)
    await ctx.send(f"Your pen size is {pickle} inches")

@bot.command()
async def spinbottle(ctx):
    # Im not using list comprehension shut up
    memberlist = []
    guild = ctx.guild
    for member in guild.members:
        if member.bot:
            continue
        print(member)
        memberlist.append(member)
    user = random.choice(memberlist)
    await ctx.send(f"The bottle lands on {user.mention}")
    
@bot.command()
async def avatar(ctx, avamember : discord.Member=None):
    if avamember == None:
        avamember = ctx.author
    userAvatar = avamember.display_avatar
    Embed = discord.Embed(title=f"{avamember.name}'s Avatar")
    Embed.set_image(url = userAvatar)
    await ctx.send(embed = Embed)

@bot.command()
async def throw(ctx, member : discord.Member=None):
    if member == ctx.author:
        await ctx.send("You can't throw things at yourself :anger: ")
        return
    elif member == None:
        await ctx.send("You need a person to throw things at :anger: ")
        return
        
    trimMember = member.id
    responses = [
        f"You threw an :eggplant: at <@!{trimMember}>. Nice one",
        f"You threw a :blue_car: at <@!{trimMember}>. They're fucking dead :skull: ",
        f"You threw a :boot: at <@!{trimMember}>. How could you?!",
        f"You threw a :bagel: at <@!{trimMember}>. Not the plain bagel!",
        f"You threw a :8ball: at <@!{trimMember}>. 8Ball IS NOT PLEASED!",
        f"You threw a :violin: at <@!{trimMember}>. I guess you could say that was violent!",
        f"You threw a :salt: at <@!{trimMember}>. You must be pretty salty",
        f"You threw a :tada: at <@!{trimMember}>. Happy birthday!",
    ]
    random.shuffle(responses)
    throwItem = random.randrange(0, len(responses))
    await ctx.send(responses[throwItem])

@bot.command()
async def github():
    pass

@bot.command()
async def rps():
    pass

@bot.command()
async def baka():
    pass

@bot.command()
async def slap():
    pass

@bot.command(aliases=["16ball"])
async def _16ball():
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

@bot.slash_command(guild_ids=testing_servers, description="Displays your pen size")
async def pen(ctx):
    pickle = random.randint(1,12)
    await ctx.respond(f"Your pen size is {pickle} inches")
    
bot.run(TOKEN)