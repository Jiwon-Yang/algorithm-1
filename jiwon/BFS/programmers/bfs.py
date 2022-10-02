from collections import deque

def bfs(graph, start, visited):
    queue = deque([])
    visited[start] = True

    while queue:
        now = queue.popleft()
        for x in graph[now]:
            if not visited[x]:
                queue.append(x)
                visited[x] = True

if __name__ == "__main__":
    graph = [[], [2, 3], [1], [1, 4], [2]]
    visited = [False] * 4
    bfs(graph, (0), visited)