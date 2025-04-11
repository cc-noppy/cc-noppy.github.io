def minimum_cost(N, connections):
    parent = list(range(N + 1))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False
        parent[py] = px
        return True

    connections.sort(key=lambda x: x[2])
    cost = 0
    edges_used = 0

    for u, v, w in connections:
        if union(u, v):
            cost += w
            edges_used += 1
            if edges_used == N - 1:
                return cost

    return -1
