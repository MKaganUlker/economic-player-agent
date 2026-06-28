from dataclasses import dataclass
from config import Config


@dataclass
class Economy:

    inflation: float
    stock_return: float
    unemployment: float


    def monthly_update(self):

        pass



def create_economy():

    return Economy(
        inflation=Config.INITIAL_INFLATION,
        stock_return=Config.INITIAL_STOCK_RETURN,
        unemployment=Config.INITIAL_UNEMPLOYMENT
    )