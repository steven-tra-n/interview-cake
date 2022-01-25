from ast import Raise
import GraphNode

def graph_coloring(graph, colors):
    for node in graph:
        if node in node.neighbors:
            raise Exception('Legal coloring impossible for node with loop: %s' % node.label)

        # Get the node's neighbors' colors as a set so we can check if it's illegal in constant time
        illegal_colors = set([
            neighbor.color
            for neighbor in node.neighbors
            if neighbor.color
        ])

        # Loop through colors to find first legal color
        for color in colors:
            if color not in illegal_colors:
                node.color = color
                break

a = GraphNode.GraphNode('a')
b = GraphNode.GraphNode('b')
c = GraphNode.GraphNode('c')

a.neighbors.add(b)
b.neighbors.add(a)
b.neighbors.add(b)
c.neighbors.add(b)

graph = [a, b, c]
colors = ['red', 'blue', 'yellow', 'green']

graph_coloring(graph, colors)