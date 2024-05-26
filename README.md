# AI Poet

## Overview

AI Poet is a Python-based project designed to create an AI-driven Discord chat bot. This bot leverages large language models (LLM) to understand and respond to user inputs in real time. By incorporating elements of Chinese classical poetry, the bot aims to provide users with psychological comfort and advice through the art of prompt engineering.

## Features

- **AI-Driven Discord Chat Bot**: Developed an advanced chat bot for Discord that interacts with users seamlessly.
- **Integration with Large Language Models (LLM)**: Utilized state-of-the-art language models to enhance the bot's understanding and responsiveness.
- **Prompt Engineering**: Applied prompt engineering techniques to embed historical and cultural elements of Chinese poetry, offering users thoughtful and comforting responses.

## Installation

To get started with AI Poet, follow these steps:

1. **Clone the repository**:

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your OpenAI API key**:
    - Create a `.env` file in the project root directory and add your OpenAI API key:
    ```plaintext
    DISCORD_TOKEN=your_discord_token
    OPENAI_API_KEY=your_openai_api_key
    ```

## Usage

Run the AI Poet bot with the following command:

```bash
python bot.py
```
