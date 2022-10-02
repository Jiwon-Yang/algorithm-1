# 소수 찾기

from itertools import permutations

def checkIsPrime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def solution(numbers):
    cnt = 0
    nums = list(numbers)
    candidates = set()

    for i in range(1, len(nums)+1):
        for n in permutations(nums, i):
            candidate = int(''.join(list(n)))
            candidates.add(candidate)

    for c in candidates:
        if c < 2:
            continue
        if checkIsPrime(c):
            cnt += 1

    return cnt

if __name__ == "__main__":
    print(solution("17"))