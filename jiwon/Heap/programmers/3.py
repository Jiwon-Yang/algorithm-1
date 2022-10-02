import heapq

def solution(arguments):
    dp_queue = []
    for arg in arguments:
        op, val = arg.split(' ')
        if op == 'I':
            heapq.heappush(dp_queue, int(val))
        else:
            try:
                if val == '1':
                    remove_value = heapq.nlargest(1, dp_queue)[0]
                else:
                    remove_value = heapq.nsmallest(1, dp_queue)[0]
            except IndexError:
                pass
            else:
                dp_queue.remove(remove_value)
                heapq.heapify(dp_queue)

    if len(dp_queue) == 0:
        max_value = 0
        min_value = 0
    elif len(dp_queue) == 1:
        max_value = dp_queue[0]
        min_value = dp_queue[0]
    else:
        max_value = heapq.nlargest(1, dp_queue)[0]
        min_value = heapq.nsmallest(1, dp_queue)[0]

    return [max_value, min_value]

if __name__ == "__main__":
    print(solution(["I 16","D 1"]))
    # print(solution(["I 7","I 5","I -5","D -1"]))
    # print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
    # print(solution(["I 3", "I 2", "I 1", "D 1", "D 1", "I 3", "D -1"]))
    # print(solution(["I 6", "I 2", "I 1", "I 4", "I 5", "I 3", "D 1", "I 7", "D -1", "I 6", "D -1", "D -1"]))