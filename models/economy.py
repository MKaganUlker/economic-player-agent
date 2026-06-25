from dataclasses import dataclass


@dataclass
class Economy:
    inflation: float
    stock_return: float
    unemployment: float

    def monthly_update(self):
        """
        Placeholder.
        Later this will become dynamic.
        """

        pass