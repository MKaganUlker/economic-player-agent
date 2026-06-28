from dataclasses import dataclass
import random

from config import Config



@dataclass
class Economy:

    inflation: float
    stock_return: float
    unemployment: float


    def monthly_update(self):

        # small market fluctuations

        self.stock_return += random.uniform(
            -0.02,
            0.02
        )

        self.inflation += random.uniform(
            -0.005,
            0.005
        )

        self.unemployment += random.uniform(
            -0.01,
            0.01
        )


        # boundaries

        self.stock_return = max(
            -0.5,
            min(
                self.stock_return,
                0.5
            )
        )


        self.inflation = max(
            0,
            min(
                self.inflation,
                1
            )
        )


        self.unemployment = max(
            0,
            min(
                self.unemployment,
                0.3
            )
        )



def create_economy():

    return Economy(
        inflation=Config.INITIAL_INFLATION,
        stock_return=Config.INITIAL_STOCK_RETURN,
        unemployment=Config.INITIAL_UNEMPLOYMENT
    )