from models.player import Player
from models.economy import Economy


def create_world():

    player = Player(
        cash=50000,
        salary=40000,
        expenses=25000,
        investments=0,
        debt=0,
        skills=[
            "python"
        ]
    )


    economy = Economy(
        inflation=0.30,
        stock_return=0.12,
        unemployment=0.08
    )


    return player, economy



def show_state(player, economy):

    print("\n===== PLAYER =====")

    print(f"Cash: {player.cash}")
    print(f"Salary: {player.salary}")
    print(f"Expenses: {player.expenses}")
    print(f"Investments: {player.investments}")
    print(f"Debt: {player.debt}")

    print(
        f"Net Worth: {player.net_worth()}"
    )

    print("\n===== ECONOMY =====")

    print(
        f"Inflation: {economy.inflation}"
    )

    print(
        f"Stock Return: {economy.stock_return}"
    )

    print(
        f"Unemployment: {economy.unemployment}"
    )



if __name__ == "__main__":

    player, economy = create_world()

    show_state(
        player,
        economy
    )