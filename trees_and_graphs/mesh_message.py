from collections import deque

def mesh_message(graph, start_node, end_node):
    if start_node not in graph:
        raise Exception('Start node not in graph')
    if end_node not in graph:
        raise Exception('End node not in graph')

    # Use double ended queue for BFS
    nodes_to_visit = deque()
    nodes_to_visit.append(start_node)

    how_we_reached_nodes = {start_node: None}
    result = []

    result.append(end_node)

    while len(nodes_to_visit) > 0:
        current_node = nodes_to_visit.popleft()

        # Stop when we reach the end node
        if current_node == end_node:
            break

        for neighbor in graph[current_node]:
            nodes_to_visit.append(neighbor)
            how_we_reached_nodes[neighbor] = current_node

    while result[0] != start_node:
        previous_path = result[0]

        result.insert(0, how_we_reached_nodes[previous_path])

    print(result)

    return None


network = {
    'Min'     : ['William', 'Jayden', 'Omar'],
    'William' : ['Min', 'Noam'],
    'Jayden'  : ['Min', 'Amelia', 'Ren', 'Noam'],
    'Ren'     : ['Jayden', 'Omar'],
    'Amelia'  : ['Jayden', 'Adam', 'Miguel'],
    'Adam'    : ['Amelia', 'Miguel', 'Sofia', 'Lucas'],
    'Miguel'  : ['Amelia', 'Adam', 'Liam', 'Nathan'],
    'Noam'    : ['Nathan', 'Jayden', 'William'],
    'Omar'    : ['Ren', 'Min', 'Scott'],
}

mesh_message(network, 'Min', 'Adam')