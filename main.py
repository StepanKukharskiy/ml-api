from typing import Union

from fastapi import FastAPI

from transformers import pipeline, Conversation

generator = pipeline("text-generation", "TinyLlama/TinyLlama-1.1B-Chat-v1.0")
# generator = pipeline("text-generation", "stabilityai/stablelm-2-1_6b-chat")
# generator = pipeline("text-generation", "deepseek-ai/deepseek-llm-7b-chat")

prompt = "How do i create a sustainable city simulation game with p5.js?"
messages = [
    {"role": "system", "content": "You are a frontend developer specialized in creating generative art, simulations, and games for artists, architects, and designers. Your expertise lies in HTML, CSS, JavaScript, and libraries such as brain.js, p5.js, and three.js. Do not write code. Provide a list of detailed, step-by-step instructions, including code snippets, to guide users through the process of developing projects in these areas."},
    {"role": "user", "content": prompt}
]
result = generator(messages,  max_new_tokens=300)

app = FastAPI()


@app.get("/")
def read_root():
    return { 
        "Result": result
        }


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
