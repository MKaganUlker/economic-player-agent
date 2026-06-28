from dataclasses import dataclass, field
from config import Config


@dataclass
class Player:

    cash: float
    salary: float
    expenses: float
    investments: float
    debt: float

    skills: list[str] = field(default_factory=list)

    projects: list[str] = field(default_factory=list)

    capabilities: list[str] = field(default_factory=list)


    def net_worth(self):

        return (
            self.cash
            +
            self.investments
            -
            self.debt
        )


    def monthly_update(
        self,
        economy
    ):

        # income

        self.cash += (
            self.salary / 12
        )


        # expenses

        self.cash -= (
            self.expenses / 12
        )


        # investment growth

        self.investments *= (
            1 +
            economy.stock_return / 12
        )



def create_player():

    return Player(

        cash=Config.INITIAL_CASH,

        salary=Config.INITIAL_SALARY,

        expenses=Config.INITIAL_EXPENSES,

        investments=Config.INITIAL_INVESTMENTS,

        debt=Config.INITIAL_DEBT,


        skills=[
            "python"
        ],

        projects=[],

        capabilities=[
            "software_development"
        ]

    )