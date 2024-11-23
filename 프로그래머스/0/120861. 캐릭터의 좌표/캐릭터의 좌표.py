def solution(keyinput, board):
    """
    ["left", "right", "up", "right", "right"], [11, 11]
    
    가로 범위 : -5~5, 세로범위 : -5~5
    [0,0] > [-1,0] > [0,0] > [0,1] > [1,1] > [2,1]
    """
    point = [0,0]
    dict = {"left":[-1,0], "right":[1,0], "up":[0,1], "down":[0,-1]}
    con1 = board[0]//2
    con2 = board[1]//2
    for go in keyinput:
        point = [x + y for x, y in zip(point,dict[go])]
        if abs(point[0])>con1:
            if point[0]>0:
                point[0]=con1 
            else:
                point[0]=-con1
        if abs(point[1])>con2:
            if point[1]>0:
                point[1]=con2
            else:
                point[1]=-con2
            
        
    return point