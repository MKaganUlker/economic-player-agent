def start_side_project(
    player,
    project
):

    cost = 5000


    if player.cash < cost:

        return "Not enough cash"


    player.cash -= cost


    player.projects.append(
        project
    )


    return (
        f"Started side project: {project}. "
        "Project may generate future income."
    )