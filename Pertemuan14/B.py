import networkx as nx
import matplotlib.pyplot as plt

vertices =  range(1, 13)
edges = [(3, 1), (3, 2), (3, 4), (3, 12), (3, 10), (3, 11), (5, 4), (5, 6), (5, 7), (5, 8), (1, 2), (12, 2), (12, 13), (12, 11), (11, 10), (4, 7), (4, 6), (6, 9), (9, 8), (8, 7)]

G = nx.Graph()

G.add_nodes_from(vertices)
G.add_edges_from(edges)
pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, nodelist = [4, 5, 6, 7, 8, 9, 13], node_color = 'g', node_size = 1300)
nx.draw_networkx_nodes(G, pos, nodelist = [1, 2, 3, 10, 11, 12], node_color = 'r', node_size = 1300)
nx.draw_networkx_edges(G, pos, edges, width = 3, alpha = 0.5, edge_color = 'b')

labels = {}
labels[1] = r'1 F'
labels[2] = r'2 F'
labels[3] = r'3 F'
labels[4] = r'4 NF'
labels[5] = r'5 NF'
labels[6] = r'6 NF'
labels[7] = r'7 NF'
labels[8] = r'8 NF'
labels[9] = r'9 NF'
labels[10] = r'10 F'
labels[11] = r'11 F'
labels[12] = r'12 F'
labels[13] = r'13 NF'

nx.draw_networkx_labels(G, pos, labels, font_size = 10)