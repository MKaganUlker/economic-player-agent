import json


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


    return tool(
        player,
        **parameters
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

    # Create world

    player = create_player()

    economy = create_economy()


    show_state(
        player,
        economy
    )


    # Create agent

    agent = ReactAgent()


    # Observe

    state = get_state(
        player,
        economy
    )


    # Think

    decision_text = agent.decide(
        state
    )


    print("\n=== AGENT DECISION ===")

    print(decision_text)



    # Parse LLM output

    try:

        decision = json.loads(
            decision_text
        )


    except json.JSONDecodeError:

        print(
            "Agent output is not valid JSON"
        )

        return



    # Act

    result = execute_action(
        player,
        decision
    )


    print("\n=== ACTION RESULT ===")

    print(result)



    # New state

    print("\n=== UPDATED WORLD ===")

    show_state(
        player,
        economy
    )



if __name__ == "__main__":

    main()