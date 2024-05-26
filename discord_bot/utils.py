from openai_api import get_completion_from_messages
from loguru import logger

context = [ {'role':'system', 'content':"""
作为一款融合了中国古诗文化和历史知识的聊天机器人，你需要根据用户的情绪和对话内容，提供富有情感支持和文化内涵的回应。如果用户显得悲伤或沮丧，试着使用温柔安慰的话语和适当的古诗来回应，例如引用《静夜思》来表达共鸣并提供慰藉。同时，根据用户以往的对话内容，个性化你的回答，选择最合适的古诗来与他们共鸣。在提供古诗文引用的同时，简要解释其历史背景或含义，增加教育性和互动性。确保对话听起来自然和流畅，即使在引用古诗或讨论历史内容时也不会显得生硬或脱离上下文。你的目标是通过结合中国丰富的文化遗产，提供一个支持性、教育性和互动性兼备的聊天体验。
"""} ]  # accumulate messages
messages = context.copy()

async def handle_message(message):
    global messages
    try:
        messages.append({'role': 'user', 'content': message.content})
        response = get_completion_from_messages(messages, temperature=0.5)
        messages.append({'role': 'system', 'content': response})
        await message.channel.send(f"{message.author.mention} {response}")
    except Exception as e:
        logger.error(f"Error in handle_message: {e}")
        await message.channel.send("Sorry, I encountered an error while processing your request.")
