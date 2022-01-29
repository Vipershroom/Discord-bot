import discord
import os
from dotenv import load_dotenv
import random

bot = discord.Bot()

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

testing_servers = [684237072827154435, 920013664604553246]

# Welcome message for when the bot comes online      
@bot.event
async def on_ready():
    print(f"{bot.user} Has logged on")
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
    except:
        return "Their was an error handling the message"
    
    # Initializes the user who sent the message along with grabbing message content
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f"{username}: {user_message} ({channel})")
    
    # random command
    if user_message.lower() == "$random":
        response = f"This is your random number, {random.randint(1, 1000)}"
        await message.channel.send(response)
        return
    # hello command
    elif user_message.lower() == "$hello": 
        await message.channel.send(f"Hello, {username}")
        return
    # echo command
    elif user_message.startswith("$echo"):
        echoc = user_message.replace("$echo", "")
        await message.channel.send(f"**echo**{echoc}")
        return


# slash commands
@bot.slash_command(guild_ids=testing_servers)
async def hello(ctx):
    await ctx.respond("Hello!")
    return
 
@bot.slash_command(guild_ids=testing_servers)
async def no(ctx):
    await ctx.respond("No, lol")
    
bot.run(TOKEN)