from dataclasses import dataclass


@dataclass(frozen=True)
class Config:

    # LLM
    MODEL_NAME = "gemma4:e4b"
    TEMPERATURE = 0.2


    # Simulation
    SIMULATION_MONTHS = 12


    # Player Initial State
    INITIAL_CASH = 50_000
    INITIAL_SALARY = 40_000
    INITIAL_EXPENSES = 25_000
    INITIAL_INVESTMENTS = 0
    INITIAL_DEBT = 0


    # Economy Initial State
    INITIAL_INFLATION = 0.30
    INITIAL_STOCK_RETURN = 0.12
    INITIAL_UNEMPLOYMENT = 0.08


    # Agent Goal
    GOAL = "maximize net worth"