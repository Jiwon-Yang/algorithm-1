import heapq as hq

def solution(scoville, K):
    hq.heapify(scoville)
    cnt = 0

    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        new = first + second * 2
        hq.heappush(scoville, new)
        cnt += 1

    return cnt

if __name__ == "__main__":
        print(solution([1, 2, 3, 9, 10, 12], 7))