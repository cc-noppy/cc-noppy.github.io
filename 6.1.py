from collections import deque, defaultdict

def valid_path(n, edges, source, destination):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    queue = deque([source])
    
    while queue:
        node = queue.popleft()
        if node == destination:
            return True
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
    return False
