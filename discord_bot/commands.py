from discord.ext import commands
import discord
from loguru import logger
from openai_api import get_completion

# Define the command prefix and intents
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='ping')
async def ping(ctx):
    """Returns Pong!"""
    await ctx.send('Pong!')

@bot.command(name='commands')
async def commands_list(ctx):
    """Provides a list of available commands and their descriptions."""
    help_text = """
    **Available Commands:**
    `!ping` - Returns Pong!
    `!commands` - Provides this help message.
    `!info` - Displays information about the bot.
    `!quote` - Generates a quote based on a given topic.
    `!poem` - Generates a Chinese poem based on the user's input.
    `!history` - Provides a brief historical fact.
    """
    await ctx.send(help_text)

@bot.command(name='info')
async def info(ctx):
    """Displays information about the bot."""
    info_text = "I am a chatbot that integrates Chinese poetry and historical knowledge to provide emotionally supportive and culturally rich responses."
    await ctx.send(info_text)

@bot.command(name='quote')
async def quote(ctx, *, topic: str):
    """Generates a quote based on a given topic."""
    try:
        prompt = f"Provide a motivational quote about {topic}."
        response = get_completion(prompt)
        await ctx.send(response)
    except Exception as e:
        logger.error(f"Error in !quote command: {e}")
        await ctx.send("Sorry, I encountered an error while generating the quote.")

@bot.command(name='poem')
async def poem(ctx, *, subject: str):
    """Generates a Chinese poem based on the user's input."""
    try:
        prompt = f"Create a Chinese poem about {subject}."
        response = get_completion(prompt)
        await ctx.send(response)
    except Exception as e:
        logger.error(f"Error in !poem command: {e}")
        await ctx.send("Sorry, I encountered an error while generating the poem.")

@bot.command(name='history')
async def history(ctx):
    """Provides a brief historical fact."""
    try:
        prompt = "Provide a brief historical fact about Chinese history."
        response = get_completion(prompt)
        await ctx.send(response)
    except Exception as e:
        logger.error(f"Error in !history command: {e}")
        await ctx.send("Sorry, I encountered an error while fetching the historical fact.")
