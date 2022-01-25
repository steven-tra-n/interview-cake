class GraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None