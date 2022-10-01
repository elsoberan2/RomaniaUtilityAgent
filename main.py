from classes.Agent import Agent
from classes.Environment import environment


def main():
    agent = Agent(19, environment, 3)
    agent.solveStateSpace()

main()
