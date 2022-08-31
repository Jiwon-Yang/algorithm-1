def solution(survey, choices):
    answer = ''
    types = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    scores = [0] * 8
    
    
    for i in range(0, len(survey)):
        choice = choices[i]
        t = survey[i][0] if choice < 4 else survey[i][1]
        
        idx = types.index(t[0])
        
        if choice == 1 or choice == 7:
            scores[idx] += 3
        elif choice == 2 or choice == 6:
            scores[idx] += 2
        elif choice == 3 or choice == 5:
            scores[idx] += 1
        elif choice == 4:
            scores[idx] += 0
    
    for i in range(0, len(scores), 2):
        if (scores[i] >= scores[i+1]):
            answer += types[i]
        elif (scores[i] < scores[i+1]):
            answer += types[i+1]
        
    
    return answer