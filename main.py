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



# Дейкстра
def dijkstra_path(graph, start, end):
    return nx.dijkstra_path(graph, start, end)

shortest_path = dijkstra_path(G, "Park", "Lviv Theatre")



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

print(f"Найкоротший шлях (Дейкстра) з Парку до Оперного театру: {shortest_path}")
