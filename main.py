from models.player import create_player
from models.economy import create_economy

from simulation.simulator import Simulator



def show_initial_state(player, economy):

    print("\n===== INITIAL PLAYER =====")

    print(f"Cash: {player.cash}")
    print(f"Salary: {player.salary}")
    print(f"Expenses: {player.expenses}")
    print(f"Investments: {player.investments}")
    print(f"Debt: {player.debt}")
    print(f"Skills: {player.skills}")
    print(f"Net Worth: {player.net_worth()}")


    print("\n===== INITIAL ECONOMY =====")

    print(f"Inflation: {economy.inflation}")
    print(f"Stock Return: {economy.stock_return}")
    print(f"Unemployment: {economy.unemployment}")



def main():

    player = create_player()

    economy = create_economy()


    show_initial_state(
        player,
        economy
    )


    simulator = Simulator(
        player,
        economy,
        months=12
    )


    simulator.run()


    print("\n=====================")
    print("SIMULATION FINISHED")
    print("=====================")


    print("\nFINAL RESULT")

    print(
        f"Net Worth: {player.net_worth()}"
    )

    print(
        f"Skills: {player.skills}"
    )

    print(
        f"Investments: {player.investments}"
    )



if __name__ == "__main__":

    main()