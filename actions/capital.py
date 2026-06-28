def allocate_capital(
    player,
    amount,
    asset="stocks"
):

    if amount > player.cash:

        return "Not enough cash"


    player.cash -= amount


    if asset == "stocks":

        player.investments += amount


        return (
            f"Invested {amount} into stocks"
        )


    return "Unknown asset"