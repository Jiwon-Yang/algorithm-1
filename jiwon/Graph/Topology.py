from collections import deque

def topology_sort():
    result = []
    dq = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            dq.append(i)

    while dq:
        now = dq.popleft()
        result.append(now)

        for e in graph[now]:
            indegree[e] -= 1
            if indegree[e] == 0:
                dq.append(e)

    return result

if __name__ == "__main__":
    v, e = map(int, input().split())
    indegree = [0] * (v+1)
    graph = [[] for _ in range(v+1)]

    # 1. 진입 차수 기록
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1


    # 2. 위상정렬 실행
    result = topology_sort()
    print(result)