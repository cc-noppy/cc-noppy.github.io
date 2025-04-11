from collections import deque

def shortestPathLength(graph):
    n = len(graph)
    all_visited = (1 << n) - 1
    queue = deque((i, 1 << i, 0) for i in range(n))  # (node, visited_mask, steps)
    visited = set((i, 1 << i) for i in range(n))

    while queue:
        node, mask, steps = queue.popleft()
        if mask == all_visited:
            return steps
        for nei in graph[node]:
            next_mask = mask | (1 << nei)
            if (nei, next_mask) not in visited:
                visited.add((nei, next_mask))
                queue.append((nei, next_mask, steps + 1))
