from .capital import allocate_capital
from .development import develop_capability
from .projects import start_side_project
from .lifestyle import optimize_lifestyle


def do_nothing(player):

    return "No action taken"



TOOLS = {


    "allocate_capital":
        allocate_capital,


    "develop_capability":
        develop_capability,


    "start_side_project":
        start_side_project,


    "optimize_lifestyle":
        optimize_lifestyle,


    "do_nothing":
        do_nothing

}