import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# List of terms to detect and delete
brainrot_terms = ["skibidi", "sigma"]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if any(term in message.content.lower() for term in brainrot_terms):
        await message.delete()
        print(f'Deleted message from {message.author}: {message.content}')
    
    await bot.process_commands(message)

# Replace 'YOUR_BOT_TOKEN' with your actual bot token in an environment variable
bot.run(os.getenv('DISCORD_BOT_TOKEN'))
