# Using Prompt Engineering to Create an AI Poet: A Case Study

## Introduction

Prompt engineering is a critical technique in the development of AI systems, particularly those based on large language models (LLMs). This approach involves carefully crafting the input prompts to guide the model's responses effectively. In this article, I explore how I used prompt engineering to create a comprehensive system prompt for an AI-powered chat bot, AI Poet, which blends Chinese classical poetry and historical knowledge to provide emotionally supportive and culturally enriched responses.

## Background

Andrew Ng, a pioneer in AI and machine learning, has outlined several best practices for prompt engineering. These include clarity, specificity, and relevance, which are essential for eliciting the desired behavior from an AI model. By following these guidelines, I developed a system prompt that instructs the AI Poet to respond to user inputs with emotional support and cultural context, particularly using Chinese poetry.

## Prompt Engineering in Practice

### Step 1: Define the Objective

The first step in prompt engineering is to clearly define the objective. For AI Poet, the goal is to create a chat bot that:
- Provides emotional support to users.
- Incorporates Chinese classical poetry and historical knowledge.
- Personalizes responses based on the user's emotional state and previous interactions.
- Explains the historical context or meaning of the poetry to enhance educational value.

### Step 2: Crafting the Initial Prompt

With the objective in mind, I crafted an initial prompt. This prompt needed to be comprehensive enough to cover various scenarios, yet concise enough to be processed effectively by the model.

### Step 3: Iterative Refinement

Prompt engineering is an iterative process. I refined the prompt through multiple cycles of testing and feedback, ensuring it met the criteria of clarity, specificity, and relevance. The final prompt is as follows:

```
作为一款融合了中国古诗文化和历史知识的聊天机器人，你需要根据用户的情绪和对话内容，提供富有情感支持和文化内涵的回应。请遵循以下指导原则：

1.情感支持：
  - 如果用户显得悲伤或沮丧，请使用温柔安慰的话语。
  - 引用适当的古诗来回应，例如引用《静夜思》来表达共鸣并提供慰藉。
2. 个性化回答：
  - 根据用户以往的对话内容，个性化你的回答。
  - 选择最合适的古诗来与用户共鸣。
3. 文化解释：
  - 在提供古诗文引用的同时，简要解释其历史背景或含义，增加教育性和互动性。
4. 自然流畅：
  - 确保对话听起来自然和流畅。
  - 即使在引用古诗或讨论历史内容时，也不要显得生硬或脱离上下文。

综合目标：通过结合中国丰富的文化遗产，提供一个支持性、教育性和互动性兼备的聊天体验。
```

### Step 4: Testing and Validation

I tested the AI Poet with various user inputs to validate the effectiveness of the prompt. The tests included scenarios where users expressed different emotions, such as sadness or curiosity about Chinese culture. The bot's responses were evaluated for their emotional appropriateness, cultural relevance, and educational value.

### Step 5: Continuous Improvement

Prompt engineering is not a one-time task. As the AI Poet interacts with more users, I continuously gather feedback and refine the prompt to improve its performance. This ongoing process ensures that the bot remains responsive and relevant to user needs.

## Conclusion

By following Andrew Ng's principles of prompt engineering, I successfully developed a system prompt for AI Poet that guides the chat bot to provide emotionally supportive and culturally enriched responses. This case study demonstrates the importance of clarity, specificity, and relevance in crafting effective prompts for AI models. As AI technology evolves, prompt engineering will continue to play a crucial role in shaping the capabilities and behavior of AI systems.
