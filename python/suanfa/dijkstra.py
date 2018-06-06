"""
    狄克斯特拉算法：计算前往x的最短路径（计算两点之间的最短路径）
    基本步骤：
        找出最便宜的节点，即可在最短时间内前往的节点
        对该节点的邻居，检查是否有前往它们的最短路径;如果有,更新其开销
        重复这个过程，直到对图中的每个节点都这样做了
        计算最终路径

    算法中：需要不停的更新开销列表和父节点表
"""

# 路径散列表
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

# 开销表
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# 存储父节点的散列表
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# 用于记录处理过的节点
processed = []

####################################################
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node

node = find_lowest_cost_node(costs) # 在未处理的节点中找到开销最小的节点
while node is not None: # 在所有的节点都被处理过后结束
    cost = costs[node] # 获取节点的开销
    neighbors = graph[node] # 获取邻居节点表

    print(neighbors)
    for n in neighbors.keys(): # 循环所有邻居点
        new_cost = cost + neighbors[n] # 计算所有所有邻居点的开销总和
        if costs[n] > new_cost: # 如果开销总和大于节点开销
            costs[n] = new_cost # 更新开销表中的开销
            parents[n] = node # 更新父节点表

    processed.append(node) # 增加到已经处理列表中
    node = find_lowest_cost_node(costs)

print(costs)
print(parents)







