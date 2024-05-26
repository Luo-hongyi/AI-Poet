from loguru import logger

# Configure logger
logger.add("logs/bot.log", rotation="1 day", retention="10 days")

# Import commonly used modules or variables
from .commands import bot

__all__ = ["bot"]
