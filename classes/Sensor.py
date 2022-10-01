class Sensor:
    def __init__(self, environment):
        self.environment = environment

    def getCurrentState(self, index):
        return self.environment[index]
