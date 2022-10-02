def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a ,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def kruskal(parent, a, b, cost):
    global result

    # 사이클이 생기지 않으면 union
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost


if __name__ == "__main__":
    v, e = map(int, input().split())
    parent = [0] * (v + 1)
    for i in range(1, v + 1):
        parent[i] = i

    edges = []
    for _ in range(e):
        a, b, cost = map(int, input().split())
        edges.append((cost, a, b))

    edges.sort()  # 1. cost 순으로 정렬

    # 2. kruskal 실행
    result = 0
    for e in edges:
        cost, a, b = e
        kruskal(parent, a, b, cost)

    print(result)
