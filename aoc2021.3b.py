import fileinput
everything = []
countOne = 0
countZero= 0
higher = ""
newList = []
savedList = []
for line in fileinput.input():
    if line[-1]=="\n":
        line = line[:-1]
    everything.append(line)
savedList = everything.copy()
for i in range(len(everything[0])):
    if len(everything) == 1:
        break
    countOne = 0
    countZero = 0
    for num in everything:
        if num[i]=="1":
            countOne+=1
        else:
            countZero+=1
    if countOne>=countZero:
        higher = "1"
    else:
        higher = "0"
    newList=[]
    for num in everything:
        if num[i] == higher:
            newList.append(num)
    everything = newList.copy()
    print(everything)
OGR = int(everything[0],2)
lower = 0
everything = savedList
for i in range(len(everything[0])):
    if len(everything) == 1:
        break
    countOne = 0
    countZero = 0
    for num in everything:
        if num[i]=="1":
            countOne+=1
        else:
            countZero+=1
    if countZero<=countOne:
        lower = "0"
    else:
       lower = "1"
    newList=[]
    for num in everything:
        if num[i] == lower:
            newList.append(num)
    everything = newList.copy()
    print(everything)
CO2 = int(everything[0],2)
print(OGR*CO2)
        