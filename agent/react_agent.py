import ollama
import json


class ReactAgent:

    def __init__(self, model="qwen3.5:9b"):

        self.model = model


    def create_prompt(self, state):

        return f"""
You are an autonomous economic player.

Your goal:
Maximize your net worth.

You can use these actions:

1. invest
2. save
3. learn_skill
4. do_nothing


Current state:

{json.dumps(state, indent=2)}


Think about the best action.

Return ONLY JSON:

{{
    "thought": "...",
    "action": "...",
    "parameters": {{}}
}}

"""


    def decide(self, state):

        prompt = self.create_prompt(state)


        response = ollama.chat(
        model=self.model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        options={
            "temperature": 0.2
        }
    )


        content = response["message"]["content"]


        return content