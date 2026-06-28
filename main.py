import json
import time


from models.player import create_player
from models.economy import create_economy

from agent.react_agent import ReactAgent

from tools.economic_tools import (
    invest,
    save_money,
    learn_skill,
    do_nothing
)



TOOLS = {

    "invest": invest,

    "save": save_money,

    "learn_skill": learn_skill,

    "do_nothing": do_nothing

}



def execute_action(player, decision):

    action = decision.get(
        "action"
    )

    parameters = decision.get(
        "parameters",
        {}
    )


    if action not in TOOLS:

        return f"Unknown action: {action}"


    tool = TOOLS[action]


    import inspect


    allowed_parameters = (
        inspect.signature(tool)
        .parameters
    )


    filtered_parameters = {

        key: value

        for key, value in parameters.items()

        if key in allowed_parameters
    }


    return tool(
        player,
        **filtered_parameters
    )


def get_state(player, economy):

    return {

        "cash": player.cash,

        "salary": player.salary,

        "expenses": player.expenses,

        "investments": player.investments,

        "debt": player.debt,

        "skills": player.skills,

        "inflation": economy.inflation,

        "stock_return": economy.stock_return,

        "unemployment": economy.unemployment

    }



def show_state(player, economy):

    print("\n===== PLAYER =====")

    print(f"Cash: {player.cash}")
    print(f"Salary: {player.salary}")
    print(f"Expenses: {player.expenses}")
    print(f"Investments: {player.investments}")
    print(f"Debt: {player.debt}")
    print(f"Skills: {player.skills}")
    print(f"Net Worth: {player.net_worth()}")


    print("\n===== ECONOMY =====")

    print(f"Inflation: {economy.inflation}")
    print(f"Stock Return: {economy.stock_return}")
    print(f"Unemployment: {economy.unemployment}")



def main():

    player = create_player()

    economy = create_economy()


    show_state(
        player,
        economy
    )


    agent = ReactAgent()


    state = get_state(
        player,
        economy
    )


    print("\n=== AGENT THINKING ===")


    start_time = time.perf_counter()


    decision_text = agent.decide(
        state
    )


    end_time = time.perf_counter()


    decision_time = end_time - start_time


    print(
        f"Decision time: {decision_time:.2f} seconds"
    )


    print("\n=== AGENT DECISION ===")

    print(decision_text)



    try:

        decision = json.loads(
            decision_text
        )


    except json.JSONDecodeError:

        print(
            "Agent output is not valid JSON"
        )

        return



    print("\n=== EXECUTING ACTION ===")


    result = execute_action(
        player,
        decision
    )


    print(result)


    print("\n=== UPDATED WORLD ===")


    show_state(
        player,
        economy
    )



if __name__ == "__main__":

    main()