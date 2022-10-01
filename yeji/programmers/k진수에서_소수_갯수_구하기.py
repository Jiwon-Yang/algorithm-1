import math

def nBase(n, k):
    revBase = ''
    
    while n > 0:
        n, mod = divmod(n, k)
        revBase += str(mod)
    return revBase[::-1]

def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    changed = nBase(n, k)
    splited = changed.split('0')
    for i in splited:
        if len(i) > 0:
            num = int(i)
            if num != 1 and isPrime(num):
                answer += 1
    return answer