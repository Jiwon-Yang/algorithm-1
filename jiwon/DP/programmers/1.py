# N으로 표현

# 문제 조건으로 유추
# 1. 1<= N <= 9
# 2. 최솟값은 8 이하 -> 최대 8자리 수

def solution(N, number):
    S = [{N}]
    print(S)
    for i in range(2, 9):
        lst = [int(str(N) * i)]
        for l in range(0, int(i / 2)):
            for x in S[l]:
                for y in S[i - l - 2]:
                    lst.append(x + y)
                    lst.append(x - y)
                    lst.append(y - x)
                    lst.append(x * y)
                    if x != 0: lst.append(y // x)
                    if y != 0: lst.append(x // y)
        if number in set(lst):
            return i
        S.append(lst)
    return -1


if __name__ == "__main__":
    print(solution(5, 12))
    # solution(2, 11)