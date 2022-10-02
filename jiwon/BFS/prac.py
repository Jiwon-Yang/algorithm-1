from collections import deque

INVALID = 0
VALID = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = []
    for _ in range(n):
        l = list(map(int, input()))  # int -> str 입력 받기
        graph.append(l)

    cnt = 0

    dq = deque([(0, 0)])
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == VALID:
                    graph[nx][ny] = graph[x][y] + 1
                    dq.append((nx, ny))
