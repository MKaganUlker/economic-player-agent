def develop_capability(
    player,
    capability
):

    if capability in player.capabilities:

        return (
            f"Already developing {capability}"
        )


    player.capabilities.append(
        capability
    )


    return (
        f"Developed capability: {capability}. "
        "Future opportunities increased."
    )