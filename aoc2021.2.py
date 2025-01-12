import fileinput
horizontal = 0
depth = 0
aim = 0 
for line in fileinput.input():
    directions=line.split()
    if directions[0] == "forward":
        horizontal+=int(directions[1])
        depth+=aim*int(directions[1])
    if directions[0] == "down":
        aim+=int(directions[1])
    if directions[0] == "up":
        aim-=int(directions[1])
answer = horizontal * depth
print(answer)