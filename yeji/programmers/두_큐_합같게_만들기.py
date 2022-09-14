from collections import deque

def solution(queue1, queue2):
    sum_1, sum_2 = sum(queue1), sum(queue2)
    half = (sum_1 + sum_2) // 2

    if sum_1 == sum_2:
        return 0
    
    count = 0
    queue1, queue2 = deque(queue1), deque(queue2)
    
    while queue1 and queue2:
        if sum_1 == half:
            return count
        elif sum_1 > half:
            sum_1 -= queue1.popleft()
        else:
            queue1.append(queue2.popleft())
            sum_1 += queue1[-1]
        count += 1
    return -1