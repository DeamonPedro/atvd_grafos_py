graph = {
    'A': {'B': 15, 'C': 4, 'E': 10},
    'B': {'E': 5},
    'C': {'E': 11, 'D': 2},
    'D': {'E': 3},
    'E': {}
}


def dijkstra(graph, vertex):
    queue = [vertex]
    distance = {vertex: 0}
    while queue:
        current = queue.pop(0)
        for neighbors in graph[current]:
            queue.append(neighbors)
            new_distance = distance[current] + graph[current][neighbors]
            if(neighbors not in distance or new_distance < distance[neighbors]):
                distance[neighbors] = new_distance

    return distance


distance = dijkstra(graph, 'A')
print("Distances", str(distance))
