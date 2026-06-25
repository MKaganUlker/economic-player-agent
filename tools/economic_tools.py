from models.player import Player


def invest(player: Player, amount: float) -> str:
    """
    Move cash into investments.
    """

    if amount <= 0:
        return "Invalid investment amount"

    if player.cash < amount:
        return "Not enough cash"

    player.cash -= amount
    player.investments += amount

    return (
        f"Invested {amount}. "
        f"Investment balance: {player.investments}"
    )



def save_money(player: Player, amount: float) -> str:
    """
    Keep money as cash.
    """

    if amount <= 0:
        return "Invalid saving amount"

    if player.cash < amount:
        return "Not enough cash"

    return (
        f"Saved {amount} as cash"
    )



def learn_skill(player: Player, skill: str) -> str:
    """
    Increase future earning potential.
    """

    if skill in player.skills:
        return "Skill already known"


    player.skills.append(skill)

    # Later:
    # this will affect salary dynamically

    return (
        f"Learned new skill: {skill}"
    )



def do_nothing(player: Player) -> str:
    """
    Agent chooses no action.
    """

    return "No action taken"