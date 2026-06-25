from dataclasses import dataclass, field


@dataclass
class Player:
    cash: float
    salary: float
    expenses: float
    investments: float
    debt: float
    skills: list[str] = field(default_factory=list)

    def net_worth(self) -> float:
        return (
            self.cash
            + self.investments
            - self.debt
        )

    def receive_salary(self):
        self.cash += self.salary

    def pay_expenses(self):
        self.cash -= self.expenses