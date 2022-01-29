import discord
import os
from dotenv import load_dotenv
import random

bot = discord.Bot()

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

testing_servers = [684237072827154435]

@bot.event
async def on_ready():
    print(f"{bot.user} Has logged on")
    for server in bot.guilds:
        print(server)
        
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    elif message.content[0] != "$":
        return
    
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f"{username}: {user_message} ({channel})")
    
    if user_message.lower() == "$random":
        response = f"This is your random number, {random.randint(1, 1000)}"
        await message.channel.send(response)
        return
    elif user_message.lower() == "$hello": 
        await message.channel.send(f"Hello, {username}")
        return


@bot.slash_command(guild_ids=testing_servers)
async def hello(ctx):
    await ctx.respond("Hello!")
    return

    
@bot.slash_command(guild_ids=testing_servers)
async def no(ctx):
    await ctx.respond("No, lol")
    
bot.run(TOKEN)