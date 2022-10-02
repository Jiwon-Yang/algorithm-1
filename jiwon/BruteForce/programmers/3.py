# 카펫
# 테두리 박스 개수, 내부 박스 개수

def solution(brown, yellow):
    sumVal = (brown + 4) // 2
    h = 3
    w = sumVal - 3

    while w >= h:
        if w * h == (brown + yellow):
            break
        w -= 1
        h += 1

    return [w, h]

if __name__ == "__main__":
    print(solution(10, 2))
    print(solution(8, 21))
    print(solution(24, 24))