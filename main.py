import networkx as nx
import matplotlib.pyplot as plt

# Побудова графу
G = nx.Graph()

places = ["Lviv Theatre", "Forum", "Museum", "Spartak",  "Park", "Mall", "Hospital"]
G.add_nodes_from(places)
 
roads = [
    ("Lviv Theatre", "Forum", 2),
    ("Lviv Theatre", "Museum", 5),
    ("Lviv Theatre", "Spartak", 7),
    ("Forum", "Museum", 3),
    ("Forum", "Mall", 6),
    ("Museum", "Spartak", 4),
    ("Spartak", "Park", 1),
    ("Park", "Mall", 2),
    ("Mall", "Hospital", 3),
    ("Hospital", "Lviv Theatre", 8),
]

G.add_weighted_edges_from(roads)

# DFS
def dfs_path(graph, start, goal):
    visited = set()
    stack = [(start, [start])]
    
    while stack:
        (vertex, path) = stack.pop()
        if vertex in visited:
            continue
        if vertex == goal:
            return path
        visited.add(vertex)
        for neighbor in set(graph.neighbors(vertex)) - visited:
            stack.append((neighbor, path + [neighbor]))
    return None

dfs_result = dfs_path(G, "Park", "Lviv Theatre")


# BFS
def bfs_path(graph, start, goal):
    visited = set()
    queue = [(start, [start])]
    
    while queue:
        (vertex, path) = queue.pop(0)
        if vertex in visited:
            continue
        if vertex == goal:
            return path
        visited.add(vertex)
        for neighbor in set(graph.neighbors(vertex)) - visited:
            queue.append((neighbor, path + [neighbor]))
    return None

bfs_result = bfs_path(G, "Park", "Lviv Theatre")



def dijkstra(graph, start):
    # Ініціалізація
    shortest_paths = {start: (None, 0)}
    current_node = start
    visited = set()

    while current_node is not None:
        visited.add(current_node)
        destinations = graph.neighbors(current_node)
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph[current_node][next_node]['weight'] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            break
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    return shortest_paths

def shortest_path(graph, start, goal):
    shortest_paths = dijkstra(graph, start)
    path = []
    current_node = goal
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    path = path[::-1]
    return path

shortest_path_result = shortest_path(G, "Park", "Lviv Theatre")



# Візуалізація
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_color='black', font_weight='bold', edge_color='red')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("City Network")
plt.show()

# Аналіз
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())

print(f"Кількість вузлів: {num_nodes}")
print(f"Кількість ребер: {num_edges}\n")
print("Ступінь вершин:")
for node, degree in degrees.items():
    print(f"{node}: {degree}")

print()

print(f"DFS шлях з Парку до Оперного театру: {dfs_result}")
print(f"BFS шлях з Парку до Оперного театру: {bfs_result}")

print()

print(f"Найкоротший шлях (Дейкстра) з Парку до Оперного театру: {shortest_path_result}")
