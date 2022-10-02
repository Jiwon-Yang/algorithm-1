import heapq as hq

def solution(jobs):
    time = 0
    heap = []
    sumVal = 0
    numJob = len(jobs)

    jobs.sort(key=lambda x:x[0], reverse=True)

    jobs.sort(key=lambda x:x[0], reverse=True)

    while jobs:
        while jobs and jobs[-1][0] <= time:
            start, execution = jobs.pop()
            hq.heappush(heap, (execution, start))

        if not heap: # 현재 실행 가능한 job이 없는 경우
            start, duration = jobs.pop()
            hq.heappush(heap, (duration, start))
            time = start

        execution, start = hq.heappop(heap)
        time += execution
        sumVal += time - start

    while heap:
        execution, start = hq.heappop(heap)
        time += execution
        sumVal += time - start

    return sumVal // numJob

if __name__ == "__main__":
    print(solution([[0, 3], [0, 2], [1, 9], [2, 6]]))
