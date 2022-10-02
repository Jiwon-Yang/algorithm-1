# 네트워크
# 방문하지 않은 노드가 없을 때까지 -> 각 노드의 edge를 재귀 탐색

def visit(i, computers, visited):
    visited[i] = 1
    for now in range(len(computers[i])):
        if computers[i][now] == 1 and visited[now] == 0:
            visit(now, computers, visited)


def solution(n, computers):
    cnt = 0
    visited = [0] * n

    for i in range(n):
        if visited[i] == 0:
            visit(i, computers, visited)
            cnt += 1
        if 0 not in visited:
            break

    return cnt


if __name__ == "__main__":
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))