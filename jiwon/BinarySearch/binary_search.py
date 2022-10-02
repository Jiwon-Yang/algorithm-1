def bs(arr, target):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = (start + end) // 2

        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            end = start - 1
        else:
            start = end + 1

    return -1


def solution(n, t, a):
    s = 0
    e = max(a)
    res = 0

    while s <= e:
        mid = (s + e) // 2
        sumValue = 0
        for x in a:
            if x > mid:
                diff = x - mid
                sumValue += diff
        if sumValue < t:
            e = mid - 1
        else:
            res = sumValue
            s = mid + 1