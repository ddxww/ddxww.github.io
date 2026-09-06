import networkx as nx
import matplotlib.pyplot as plt
G=nx.complete_graph(7)
nx.draw(G)
plt.show()
print(G.size())
plt.figure()
G=nx.complete_graph(7,nx.DiGraph())
nx.draw(G)
plt.show()
plt.figure()
G=nx.cycle_graph(6)
nx.draw(G)
plt.show()
import networkx as nx
import matplotlib.pyplot as plt

# 创建图
G = nx.karate_club_graph()  # 示例：空手道俱乐部社交网络

# 计算节点位置（使用弹簧布局）
pos = nx.spring_layout(G)

# 绘制图
plt.figure(figsize=(10, 8))  # 设置画布大小
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=500,
    node_color='lightblue',
    font_size=10,
    font_weight='bold',
    width=2,          # 边的宽度
    edge_color='gray' # 边的颜色
)

# 添加标题
plt.title("空手道俱乐部社交网络", fontsize=14)

# 显示图形
plt.show()