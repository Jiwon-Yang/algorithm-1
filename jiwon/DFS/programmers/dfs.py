def dfs(x):
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            dfs(i)

if __name__ == "__main__":
    graph = [[], [2, 3], [1], [1, 4], [2]]
    visited = [False] * 4
    dfs(0)