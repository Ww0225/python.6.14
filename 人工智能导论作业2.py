from collections import deque

graph = {
    's': ['d', 'e', 'p'],
    'd': ['b', 'c', 'e'],
    'e': ['h', 'r'],
    'p': ['q'],
    'b': ['a'],
    'c': ['a'],
    'h': ['p', 'g'],
    'a': [],
    'q': [],
    'r': ['f'],
    'f': ['c', 'G'],
    'G': []
}

def dfs(graph, start, end, path=None):
    if path is None:
        path = []
    path.append(start)
    if start == end:
        return path
    if start not in graph:
        return None
    for neighbor in graph[start]:
        if neighbor not in path:
            new_path = dfs(graph, neighbor, end, path)
            if new_path:
                return new_path
    return None

def bfs(graph, start, end):
    queue = deque()
    queue.append((start, [start]))
    while queue:
        node, path = queue.popleft()
        if node == end:
            return path
        for neighbor in graph.get(node, []):
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor]))
    return None

start = 's'
end = 'G'
print("DFS路径:", dfs(graph, start, end))
print("BFS路径:", bfs(graph, start, end))