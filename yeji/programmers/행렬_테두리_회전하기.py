def solution(rows, columns, queries):
    answer = []
    table = []
    
    for r in range(rows):
        table.append([a for a in range(r*columns+1, (r+1)*columns+1)])
    
    for x1, y1, x2, y2 in queries:
        x1 = x1 - 1
        y1 = y1 - 1
        x2 = x2 - 1
        y2 = y2 - 1
        
        tmp = table[x1][y1]
        smallest = table[x1][y1]
        
        for k in range(x1, x2): # 왼쪽 세로
            test = table[k+1][y1]
            table[k][y1] = test
            smallest = min(smallest, test)

        for k in range(y1, y2):
            test = table[x2][k+1]
            table[x2][k] = test
            smallest = min(smallest, test)

        for k in range(x2, x1,-1):
            test = table[k-1][y2]
            table[k][y2] = test
            smallest = min(smallest, test)

        for k in range(y2, y1, -1):
            test = table[x1][k-1]
            table[x1][k] = test
            smallest = min(smallest, test)

        table[x1][y1+1] = tmp
        answer.append(smallest)
        
    return answer