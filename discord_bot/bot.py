from discord.ext import commands
import discord
from discord_bot.events import on_ready, on_message
from discord_bot.commands import bot
from loguru import logger

class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_listener(on_message)

# Initialize bot with command prefix and intents
intents = discord.Intents.all()
bot = MyBot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    logger.info(f'We have logged in as {bot.user}')

if __name__ == "__main__":
    logger.add("logs/bot.log", rotation="1 day", retention="10 days")
    bot.run(DISCORD_TOKEN)
