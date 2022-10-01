from classes.Node import Node


def createConnection(cityIndex, cost):
    return {"cityIndex": 19 - cityIndex, "cost": cost}


environment = [
    Node('Neamt', [createConnection(18, 87)]), # 0
    Node('Iasi', [createConnection(17, 92), createConnection(19, 87)]), # 1
    Node('Vaslui', [createConnection(14, 142), createConnection(18, 92)]), # 2
    Node('Eforie', [createConnection(15, 86)]), # 3
    Node('Hirsova', [createConnection(14, 98), createConnection(16, 86)]), # 4
    Node('Urziceni', [createConnection(12, 85), createConnection(15, 98), createConnection(17, 142)]), # 5
    Node('Giurgiu', [createConnection(12, 90)]), # 6
    Node('Bucharest', [createConnection(13, 90), createConnection(14, 85), createConnection(8, 101), createConnection(6, 211)]), # 7
    Node('Craiova', [createConnection(10, 120), createConnection(7, 146), createConnection(8, 138)]), # 8
    Node('Drobeta', [createConnection(9, 75), createConnection(11, 120)]), #9
    Node('Mehadia', [createConnection(5, 70), createConnection(10, 75)]), # 10
    Node('Pitesti', [createConnection(7, 97), createConnection(11, 138), createConnection(12, 101)]), # 11
    Node('Rimnicu Vilcea', [createConnection(3, 80), createConnection(8, 97), createConnection(11, 146)]), # 12
    Node('Fagaras', [createConnection(3, 99), createConnection(12, 211)]), # 13
    Node('Lugoj', [createConnection(4, 111), createConnection(9, 70)]), # 14
    Node('Timisoara', [createConnection(2, 118), createConnection(5, 111)]), # 15
    Node('Sibiu', [createConnection(0, 151), createConnection(2, 140), createConnection(6, 99), createConnection(7, 80)]), # 16
    Node('Arad', [createConnection(1, 75), createConnection(3, 140), createConnection(4, 118)]), # 17
    Node('Zerind', [createConnection(0, 71), createConnection(2, 75)]), # 18
    Node('Oradea', [createConnection(1, 71), createConnection(3, 151)]) # 19
]
