import math
from collections import defaultdict

def timeToMin(time):
    hour, minutes = time.split(":")
    return int(hour) * 60 + int(minutes)

def calcCost(fees, mins):
    defaultMin, defaultFee, unitMin, unitFee = fees
    if mins <= defaultMin:
        return defaultFee
    cost = defaultFee + math.ceil((mins - defaultMin) / unitMin) * unitFee
    return int(cost)

def solution(fees, records):
    answer = []
    inTimes = {}
    totalTimes = defaultdict(int)

    for record in records :
        time, car, state = record.split()
        mins = timeToMin(time)
        
        if car in inTimes:
            totalTimes[car] += mins - inTimes[car]
            del inTimes[car]
        else:
            inTimes[car] = mins

    maxTime = timeToMin('23:59')
    for car, mins in inTimes.items():
        totalTimes[car] += maxTime - mins

    for car, mins in totalTimes.items() :
        cost = calcCost(fees, mins)
        answer.append((car, cost))

    answer.sort()
    return [cost for car, cost in answer]