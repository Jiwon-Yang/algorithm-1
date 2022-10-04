from itertools import combinations_with_replacement as cwr

def solution(n, info):
    answer = [-1]
    maxGap = -1
    
    if info[0] == n:
        return [-1]
    
    for combi in cwr(range(11), n):
        lions = [0] * 11

        for i in combi:
            lions[10 - i] += 1

        apeach, lion = 0, 0
        
        for idx in range(11):
            if info[idx] == lions[idx] == 0:
                continue
            elif info[idx] >= lions[idx]:
                apeach += 10 - idx
            else:
                lion += 10 - idx

        if lion > apeach:
            gap = lion - apeach
            if gap > maxGap:
                maxGap = gap
                answer = lions
    return answer