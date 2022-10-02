cnt = 0

def dfs(numbers, v, target, depth, sumVal):
    global cnt

    if v == depth:
        if sumVal == target:
            cnt += 1
        return

    dfs(numbers, v + 1, target, depth, sumVal - numbers[v])
    dfs(numbers, v + 1, target, depth, sumVal + numbers[v])


def solution(numbers, target):
    global cnt
    dfs(numbers, 0, target, len(numbers), 0)
    return cnt