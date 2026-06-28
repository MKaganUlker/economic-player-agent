import json
import time


from agent.react_agent import ReactAgent

from actions import TOOLS

class Simulator:


    def __init__(
        self,
        player,
        economy,
        months=12
    ):

        self.player = player

        self.economy = economy

        self.months = months

        self.agent = ReactAgent()


        self.history = []



    def get_state(self):

        return {

            "month": len(self.history) + 1,

            "cash": self.player.cash,

            "salary": self.player.salary,

            "expenses": self.player.expenses,

            "investments": self.player.investments,

            "debt": self.player.debt,

            "skills": self.player.skills,

            "inflation": self.economy.inflation,

            "stock_return": self.economy.stock_return,

            "unemployment": self.economy.unemployment,

            "memory": self.player.memory[-5:],

            "capabilities": self.player.capabilities,

        }



    def execute_action(
        self,
        decision
    ):

        import inspect


        action = decision.get("action")

        parameters = decision.get(
            "parameters",
            {}
        )


        if action not in TOOLS:

            return f"Unknown action: {action}"


        tool = TOOLS[action]


        signature = inspect.signature(tool)


        filtered_parameters = {

            key: value

            for key, value in parameters.items()

            if key in signature.parameters

        }


        if "month" in signature.parameters:

            filtered_parameters["month"] = (
                len(self.history) + 1
            )


        required_parameters = [

            name

            for name, param in signature.parameters.items()

            if name != "player"

            and name != "month"

            and param.default == inspect.Parameter.empty

        ]


        for required in required_parameters:

            if required not in filtered_parameters:

                return (
                    f"Invalid action. "
                    f"Missing parameter: {required}"
                )


        return tool(
            self.player,
            **filtered_parameters
        )



    def run_month(self):


        state = self.get_state()


        start = time.perf_counter()


        decision_text = self.agent.decide(
            state
        )


        elapsed = (
            time.perf_counter()
            -
            start
        )


        decision = json.loads(
            decision_text
        )


        result = self.execute_action(
            decision
        )


        record = {

            "month": state["month"],

            "decision": decision,

            "result": result,

            "time": elapsed,

            "net_worth": self.player.net_worth()

        }


        self.history.append(
            record
        )
        
        self.player.monthly_update(
            self.economy
        )


        self.economy.monthly_update()

        print(
            f"""
=====================
MONTH {state["month"]}
=====================

Action:
{decision["action"]}

Reason:
{decision["thought"]}

Result:
{result}

Net Worth:
{self.player.net_worth()}

Decision Time:
{elapsed:.2f}s

"""
        )



    def run(self):

        for _ in range(self.months):

            self.run_month()