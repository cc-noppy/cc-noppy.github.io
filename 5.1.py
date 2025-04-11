from collections import deque

def removeInvalidParentheses(s):
    def is_valid(string):
        count = 0
        for char in string:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0

    queue = deque([s])
    visited = set([s])
    results = []
    found = False

    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            current = queue.popleft()
            if is_valid(current):
                results.append(current)
                found = True
            if found:
                continue  # stop going deeper if one level has valid result
            for i in range(len(current)):
                if current[i] not in ('(', ')'):
                    continue
                next_str = current[:i] + current[i+1:]
                if next_str not in visited:
                    visited.add(next_str)
                    queue.append(next_str)
        if found:
            break

    return results
