# LLM Engineer

## Initial Configurations 

- create a .env file paste your API keys from openAI or Gemini
- openAI will cost,Gemini is free 
- you can also use Ollama

### How to run Ollama
1. first install ollama on your machine 
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

- check version 

```bash
ollama --version
```

2. Download a Model
```bash 
ollama run llama3
```

3. Use ollama in Python 
- install open AI ollama is compatible with open AI 
```bash 
pip3 install openai
```

- Python code 
```py
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

response = client.chat.completions.create(
    model="llama3",
    messages=[
        {"role": "user", "content": "Explain AI in simple terms"}
    ]
)

print(response.choices[0].message.content)
```

## System Prompt vs User Prompt

In chat-based Large Language Models (LLMs) like ChatGPT or Llama, prompts are structured using different **roles**. The two most important roles are **System Prompt** and **User Prompt**.

---

### 1. System Prompt

A **System Prompt** defines the behavior, personality, and rules that the AI should follow during the conversation.

It tells the AI:
- Who it is
- How it should respond
- What style or format to use
- Any restrictions or guidelines

#### Example

- You are a helpful AI tutor who explains programming concepts in simple language.


This instruction controls how the AI will respond to user questions.

---

### 2. User Prompt

A **User Prompt** is the actual input or question provided by the user.

#### Example
- Explain what a Python list is.


The AI will respond to this question while following the behavior defined in the **System Prompt**.

---

### Example Together

#### System Prompt
- You are a senior software engineer who explains concepts to beginners.
#### User Prompt
- Explain what machine learning is.