import fileinput
points = []
for line in fileinput.input():
    hold = line.split("->")
    startStrings = hold[0].split(",")
    endStrings = hold[1].split(",")
    start = [int(startStrings[0]),int(startStrings[1])]
    end = [int(endStrings[0]),int(endStrings[1])]
    points.append(start)
    points.append(end)
board = []
for i in range(1000):
    row = [0]*1000
    board.append(row)
for j in range(0, len(points),2):
    if(points[j][1] == points[j+1][1]):
        col = points[j+1][1]
        if(points[j+1][0]>points[j][0]):
            loop = points[j+1][0]- points[j][0]
            small = points[j][0]
        else:
            loop = points[j][0]- points[j+1][0]
            small = points[j+1][0]
        for i in range(loop+1):
            board[small+i][col] +=1
    elif(points[j][0] == points[j+1][0]):
        row = points[j+1][0]
        if(points[j+1][1]>points[j][1]):
            loop = points[j+1][1]- points[j][1]
            small = points[j][1]
        else:
            loop = points[j][1]- points[j+1][1]
            small = points[j+1][1]
        for i in range(loop+1):
            board[row][small+i] +=1
            
    else:
        if(points[j+1][0]>points[j][0]):
            loop = points[j+1][0]- points[j][0]
            moveX = 1
        else:
            loop = points[j][0]- points[j+1][0]
            moveX = -1
        if(points[j+1][1]>points[j][1]):
            loop = points[j+1][1]- points[j][1]
            moveY = 1
        else:
            loop = points[j][1]- points[j+1][1]
            moveY = -1
        for i in range(loop+1):
            row = points[j][0] +moveX*i
            col = points[j][1] +moveY*i
            board[row][col] +=1                
count = 0
for row in board:
    print(row)
    for value in row:
        if(value>1):
            count+=1        
print(count)