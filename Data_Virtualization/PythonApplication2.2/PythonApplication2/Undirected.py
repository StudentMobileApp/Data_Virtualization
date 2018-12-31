
#!/usr/bin/env python
"""
==============
Undirected Weighted Graph
==============

An example using Graph as an undirected weighted network.
"""

import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

G.add_edge('A', 'B', weight = 3)
G.add_edge('A', 'C', weight = 5)
G.add_edge('A', 'D', weight = 7)
G.add_edge('B', 'C', weight = 4)
G.add_edge('B', 'D', weight = 8)
G.add_edge('C', 'D', weight = 2)


elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 5]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 5]

pos = nx.spring_layout(G)  # positions for all nodes

# nodes
nx.draw_networkx_nodes(G, pos, node_size=700)

# edges
nx.draw_networkx_edges(G, pos, edgelist=elarge,
                       width=6)
nx.draw_networkx_edges(G, pos, edgelist=esmall,
                       width=6, alpha=0.5, edge_color='b', style='dashed')

# labels
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

plt.axis('off')
plt.show()
