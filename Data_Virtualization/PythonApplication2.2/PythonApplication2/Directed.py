
#!/usr/bin/env python
"""
==============
Directed Weighted Graph
==============

An example using Graph as an undirected weighted network.
"""

from matplotlib import pyplot as plt
from matplotlib import patches as pat

import networkx as nx

G = nx.MultiDiGraph()

G.add_nodes_from(['A','B','C','D'])

pos = nx.layout.spring_layout(G)  # positions for all nodes

G.add_edge('A', 'B', w = 3)
G.add_edge('A', 'C', w = 5)
G.add_edge('A', 'D', w = 7)

G.add_edge('B', 'A', w = 2)
G.add_edge('B', 'C', w = 4)
G.add_edge('B', 'D', w = 8)

G.add_edge('C', 'B', w = 2)
G.add_edge('C', 'D', w = 2)

G.add_edge('D', 'A', w = 3)
G.add_edge('D', 'C', w = 1)

# labels
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')

egdes = nx.biconnected_component_edges
nx.draw(G, pos, arrowsize=20)
nx.get_edge_attributes(G, 'w')
nx.draw_networkx_edge_labels(G,pos)

#style = pat.ConnectionStyle("ARC3", rad = 0.3)
plt.axis('off')
#plt.gca().add_patch(style)
plt.show()
 