# 위장
# 조합의 개수
def solution(clothes):
    map = {}
    for name, category in clothes:
        if category in map:
            prev = map[category]
            prev.append(name)
            map[category] = prev
        else:
            map[category] = [name]

    answer = 1
    for value in map.values():
        answer *= len(value) + 1


    map.keys()
    return answer - 1


if __name__ == "__main__":
    print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))