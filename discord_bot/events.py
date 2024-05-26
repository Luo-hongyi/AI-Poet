import discord
from discord_bot.utils import handle_message
from loguru import logger

async def on_ready():
    logger.info(f'We have logged in as {bot.user}')

async def on_message(message):
    if message.author == message.guild.me:
        return
    try:
        await handle_message(message)
    except Exception as e:
        logger.error(f"Error in on_message: {e}")
        await message.channel.send("Sorry, I encountered an error while processing your request.")
