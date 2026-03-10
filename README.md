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