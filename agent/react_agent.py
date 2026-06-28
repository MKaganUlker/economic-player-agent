import json

import ollama

from config import Config


class ReactAgent:

    def __init__(self):
        self.model = Config.MODEL_NAME


    def create_prompt(self, state):

        return f"""
You are an autonomous economic player.

Your goal:
{Config.GOAL}

You can perform these actions:

1. invest
2. save
3. learn_skill
4. do_nothing


Current world state:

{json.dumps(state, indent=2)}


Analyze the situation.

Choose the best action to maximize long-term results.

Return ONLY valid JSON.

Format:

{{
    "thought": "short explanation",
    "action": "action_name",
    "parameters": {{
        "key": "value"
    }}
}}

Do not use markdown.
Do not add extra text.
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
                "temperature": Config.TEMPERATURE
            }
        )


        content = response["message"]["content"]


        return content