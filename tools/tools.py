def save_money(player, amount):
    return f"Saved {amount}"


def invest(player, amount):
    player.cash -= amount
    player.investments += amount

    return f"Invested {amount}"


def do_nothing(player):
    return "No action taken"