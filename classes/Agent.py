from classes.Sensor import Sensor


class Agent:
    def __init__(self, index, environment, goal):
        self.start = index
        self.current = index
        self.goal = goal
        self.lowestPath = {"path": [], "cost": 0}
        self.sensor = Sensor(environment)

    def nodeLambda(self, node):
        return self.getCurrentState(node).name

    def printPath(self, data):
        copy = map(self.nodeLambda, data["path"])
        string = "-> ".join(copy)
        string2 = data["cost"]
        print(f"{string} with a cost of {string2}")

    # La acción a tomar del agente, se mueve de un sitio a otro
    def action(self, city):
        self.current = city

    # El agente hace uso del sensor para conocer en qué sitio se encuentra actualmente
    def getCurrentState(self, index):
        if index == None:
            index = self.current

        return self.sensor.getCurrentState(index)

    # Algoritmo de búsqueda
    def getGoalAtLowestCost(self, history, cost, current, goal):

        ## El agente tiene que conocer el sitio en el que se encuentra actualmente
        self.current = current
        currentState = self.getCurrentState(current)

        ## Verfificación para saber si me encuentro en la meta
        if goal == currentState.name:
            ## Si es la primera ruta completada, el agente lo recordará automáticamente como
            ## La ruta más corta
            if len(self.lowestPath["path"]) == 0:
                self.lowestPath = {"path": history, "cost": cost}
                self.printPath(self.lowestPath)
            ## Si no es la primera ruta completada, tiene que comparar la ruta guardada menos
            ## costosa con el cost de la ruta completada más reciente
            elif self.lowestPath["cost"] > cost:
                self.lowestPath = {"path": history, "cost": cost}
                self.printPath(self.lowestPath)

            return

        ## Saca los sitios adyacentes del sitio actual
        neighbors = currentState.neighbors

        ## Se recorre cada sitio adyacente
        for i in range(len(neighbors)):
            ## Si el sitio no ha sido visitado en la ruta, el agente puede avanzar a ese sitio
            if neighbors[i]["cityIndex"] not in history:
                ## Al avanzar al sitio, se guarda en el historial de sitios visitados
                list = [j for j in history] + [neighbors[i]["cityIndex"]]
                ## Recursión para seguir avanzando
                self.getGoalAtLowestCost(
                    list, cost + neighbors[i]["cost"], neighbors[i]["cityIndex"], goal)

        return self.lowestPath

    # Función de inicio
    def solveStateSpace(self):
        data = self.getGoalAtLowestCost(
            [self.current], 0, self.current, self.getCurrentState(self.goal).name)

        print(f"BEST SOLUTION TO TRAVEL FROM {self.getCurrentState(self.start).name} TO {self.getCurrentState(self.goal).name}")
        print(data)
