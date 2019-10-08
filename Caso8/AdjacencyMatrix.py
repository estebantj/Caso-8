class Graph(object):
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    def addEdge(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def removeEdge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def containsEdge(self, v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False

    def __len__(self):
        return self.size

    def toString(self):
        count = 1
        for row in self.adjMatrix:
            print("[", count, "]: ", row)
            count += 1

    def getAllAdjacencies(self, elementPosition):
        adjacenciesPositions = []
        for column, value in enumerate(self.adjMatrix[elementPosition]):
            if value > 0:
                adjacenciesPositions += [column]
        return adjacenciesPositions
