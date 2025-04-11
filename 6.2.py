def longest_cycle(edges):
    n = len(edges)
    visited = [False] * n
    longest = -1

    def dfs(node, depth_map, depth):
        nonlocal longest
        if node == -1:
            return
        if visited[node]:
            if node in depth_map:
                longest = max(longest, depth - depth_map[node])
            return
        visited[node] = True
        depth_map[node] = depth
        dfs(edges[node], depth_map, depth + 1)
        depth_map.pop(node)

    for i in range(n):
        if not visited[i]:
            dfs(i, {}, 0)
    return longest
