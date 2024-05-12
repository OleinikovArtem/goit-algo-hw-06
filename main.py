import networkx as nx
import matplotlib.pyplot as plt

####################################################
###                    STEP 1                    ###
####################################################

G = nx.Graph()

edges = [
    ('A', 'B', {'weight': 4}),
    ('B', 'C', {'weight': 2}),
    ('C', 'D', {'weight': 1}),
    ('D', 'A', {'weight': 5}),
    ('A', 'C', {'weight': 3}),
    ('B', 'D', {'weight': 2})
]
G.add_edges_from(edges)

nx.draw(G, with_labels=True, font_weight='bold')
# plt.show()

print("Number of vertices:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())
print("Degrees of vertices:", dict(G.degree()))


####################################################
###                    STEP 2                    ###
####################################################

dfs_tree = list(nx.dfs_tree(G, source='A'))
print("DFS order:", dfs_tree)

bfs_tree = list(nx.bfs_tree(G, source='A'))
print("BFS order:", bfs_tree)


####################################################
###                    STEP 3                    ###
####################################################

dijkstra_path = nx.single_source_dijkstra_path(G, source='A')
print("Dijkstra paths from A:", dijkstra_path)

# Open the window
plt.show()
