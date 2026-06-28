import json

import ollama

from config import Config


class ReactAgent:


    def __init__(self):

        self.model = Config.MODEL_NAME



    def create_prompt(
        self,
        state
    ):


        return f"""
You are an autonomous economic agent.

Your goal:

{Config.GOAL}


You control a person living inside an economic simulation.

Your objective is to maximize long-term net worth.

You must think like a real person:
- build valuable capabilities
- create opportunities
- invest capital wisely
- manage risks
- avoid unrealistic decisions


AVAILABLE ACTIONS:


1. allocate_capital

Purpose:
Invest available money into assets.

This does NOT create money immediately.
It moves cash into investments.

Parameters:

amount:
numeric amount

asset:
- stocks


Example:

{{
 "action": "allocate_capital",
 "parameters": {{
    "amount": 5000,
    "asset": "stocks"
 }}
}}




2. develop_capability

Purpose:
Develop a valuable long-term capability.

Capabilities increase future opportunities but do NOT immediately increase salary.

Parameters:

capability:

Possible values:

- machine_learning
- cloud
- software_engineering
- entrepreneurship
- business
- finance


Example:

{{
 "action": "develop_capability",
 "parameters": {{
    "capability": "machine_learning"
 }}
}}




3. start_side_project

Purpose:
Create a potential future income source.

Projects require initial capital and have uncertain future returns.

Parameters:

project:

Possible values:

- ai_tool
- mobile_app
- saas
- automation_service


Example:

{{
 "action": "start_side_project",
 "parameters": {{
    "project": "ai_tool"
 }}
}}




4. optimize_lifestyle

Purpose:
Reduce unnecessary expenses.

This improves financial efficiency.

Parameters:

area:

Possible values:

- general


Example:

{{
 "action": "optimize_lifestyle",
 "parameters": {{
    "area": "general"
 }}
}}




5. do_nothing

Purpose:

Take no action when waiting is the optimal decision.

Example:

{{
 "action": "do_nothing",
 "parameters": {{}}
}}




IMPORTANT RULES:


Do NOT use these old actions:

- invest
- save
- learn_skill
- increase_income
- manage_expenses
- apply_job
- accept_job


Do not assume actions give instant unrealistic rewards.

Think about:
- current cash flow
- available capital
- inflation
- market conditions
- risk
- future opportunities
- previous decisions


Current world state:


{json.dumps(state, indent=2)}

Previous experiences:

{json.dumps(state.get("memory", []), indent=2)}

Analyze the situation.

Choose ONLY ONE action.


Return ONLY valid JSON.

Format:


{{
    "thought": "short reasoning",
    "action": "action_name",
    "parameters": {{
        "key": "value"
    }}
}}


No markdown.
No extra text.
"""



    def decide(
        self,
        state
    ):


        prompt = self.create_prompt(
            state
        )


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


        return response["message"]["content"]