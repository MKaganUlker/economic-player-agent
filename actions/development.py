from simulation.capabilities import CAPABILITIES



def develop_capability(
    player,
    capability,
    month
):


    if capability not in CAPABILITIES:

        return "Unknown capability"



    data = CAPABILITIES[capability]


    cost = data["cost"]

    cooldown = data["cooldown"]



    if player.cash < cost:

        return (
            "Not enough cash "
            "to develop capability"
        )



    last_time = player.capability_history.get(
        capability
    )



    if last_time is not None:


        if month - last_time < cooldown:

            return (
                f"{capability} is still on cooldown"
            )



    player.cash -= cost



    player.capabilities.append(
        capability
    )



    player.capability_history[capability] = month



    player.memory.append({

        "month": month,

        "action": "develop_capability",

        "capability": capability,

        "cost": cost

    })



    return (
        f"Developed {capability}. "
        f"Cost: {cost}"
    )