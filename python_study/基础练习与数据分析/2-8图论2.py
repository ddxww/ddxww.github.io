import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
# 图4：使用邻接矩阵构建的加权图
a = [[0, 3, 9, 2],
     [3, 0, 8, 0],
     [9, 8, 0, 0],
     [2, 0, 0, 0]]
G4 = nx.from_numpy_matrix(np.array(a))
pos = nx.spring_layout(G4)
nx.draw(G4, pos, with_labels=True, node_color='lightblue', node_size=500, edge_color='gray', font_size=15, width=2)
labels = nx.get_edge_attributes(G4, 'weight')
nx.draw_networkx_edge_labels(G4, pos, edge_labels=labels)
plt.xticks([])  # 隐藏X轴刻度
plt.yticks([])  # 隐藏Y轴刻度
plt.show()
# 图5：加权有向图
s = [1, 2, 3, 4]
t = [2, 3, 1, 1]
w = [3, 8, 9, 2]
G5 = nx.DiGraph()
for i in range(len(s)):
    G5.add_edge(s[i], t[i], weight=w[i])

pos = nx.spring_layout(G5)
nx.draw(G5, pos, with_labels=True, node_color='lightblue', node_size=500, edge_color='gray', font_size=15, width=2)
labels = nx.get_edge_attributes(G5, 'weight')
nx.draw_networkx_edge_labels(G5, pos, edge_labels=labels)
plt.xticks([])  # 隐藏X轴刻度
plt.yticks([])  # 隐藏Y轴刻度
plt.show()
# 图6：使用邻接矩阵构建的有向加权图
a = [[0, 3, 0, 0],
     [0, 0, 8, 0],
     [9, 0, 0, 0],
     [2, 0, 0, 0]]
G6 = nx.from_numpy_matrix(np.array(a), create_using=nx.DiGraph)
pos = nx.spring_layout(G6)
nx.draw(G6, pos, with_labels=True, node_color='lightblue', node_size=500, edge_color='gray', font_size=15, width=2)
labels = nx.get_edge_attributes(G6, 'weight')
nx.draw_networkx_edge_labels(G6, pos, edge_labels=labels)
plt.xticks([])  # 隐藏X轴刻度
plt.yticks([])  # 隐藏Y轴刻度
plt.show()