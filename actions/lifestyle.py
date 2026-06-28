def optimize_lifestyle(
    player,
    area
):

    if area == "general":

        reduction = (
            player.expenses * 0.05
        )


        player.expenses -= reduction


        return (
            "Optimized lifestyle. "
            f"Expenses reduced by {reduction}"
        )


    return "Unknown optimization"