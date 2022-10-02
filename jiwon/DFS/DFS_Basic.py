##### solution 0 #####
# n = 3
# ch = [0] * (n+1)
# def DFS_0(v):
#     if v > n:
#         for x in range(1, n+1):
#             if ch[x] == 1:
#                 print(x, end=" ")
#         return
#     else:
#         ch[v] = 1
#         DFS_0(v+1)
#         ch[v] = 0
#         DFS_0(v+1)

##### solution1 #####
# def DFS_1(v):
#     global cnt
#     if v == n:
#         cnt += 1
#     else:
#         for i in range(1, n+1):
#             if graph[v][i] == 0 and ch[i] == 0:
#                 ch[i] = 1
#                 DFS_1(i)
#                 ch[i] = 0

