from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
graph = [
    [0, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [1, 0, 1, 0]
]
def BFS_0():
    dq = deque()
    cnt = 0

    for x in range(0, 4):
        for y in range(0, 4):
            if graph[x][y] == 1:
                cnt += 1

                graph[x][y] = 0 # 방문 기록
                dq.append((x, y))

                while dq:
                    xx, yy = dq.popleft()
                    for i in range(4):
                        nx = xx + dx[i]
                        ny = yy + dy[i]
                        if 0<= nx < 4 and 0<= ny < 4 and graph[nx][ny] == 1:
                            dq.append((nx, ny))
                            graph[nx][ny] = 0 # 방문 기록

def BFS_1(n, m):
    dq = deque()
    dq.append((0, 0))

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or ny>=n or ny<0 or ny>=m:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                dq.append((nx, ny))

    return graph[n-1][m-1]


def BFS_2(n):
    cnt = 0
    dq = deque()

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                dq.append((i, j))
                cnt += 1

                while dq:
                    x, y = dq.popleft()
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if nx<0 or nx>=n or ny<0 or ny>=n:
                            continue
                        if graph[nx][ny] == 0:
                            continue
                        dq.append((nx, ny))
                        graph[nx][ny] = 0
