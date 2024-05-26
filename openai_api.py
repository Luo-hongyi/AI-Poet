import openai
from loguru import logger
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def get_completion(prompt, model="gpt-3.5-turbo", temperature=0.5):
    try:
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,  # 使用 messages 而不是 prompt
            temperature=temperature
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        logger.error(f"Error in get_completion: {e}")
        return "Sorry, I encountered an error while processing your request."

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0.5):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,  # 使用 messages 而不是 prompt
            temperature=temperature
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        logger.error(f"Error in get_completion_from_messages: {e}")
        return "Sorry, I encountered an error while processing your request."
