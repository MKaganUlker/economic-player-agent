def increase_income(
    player,
    strategy
):

    if strategy == "develop_ai_expertise":

        if "AI" not in player.skills:

            player.skills.append(
                "AI"
            )


        player.salary *= 1.25


        return (
            "Developed AI expertise. "
            "Salary increased by 25%"
        )


    elif strategy == "improve_existing_skills":

        player.salary *= 1.10


        return (
            "Improved existing skills. "
            "Salary increased by 10%"
        )


    return "Unknown income strategy"