import fileinput
digits=[0,0,0,0,0,0,0,0,0,0,0,0]
gamma = [0,0,0,0,0,0,0,0,0,0,0,0]
total = 0
final = ""
rate=""
for line in fileinput.input():
    total+=1
    for i in range(len(line)):
        if line[i] == "1":
            digits[i]+=1
print(digits)
print(total)
for i in range(len(digits)):
    if total-digits[i]<digits[i]:
        gamma[i]=1
print(gamma)

for i in range(len(gamma)):
    final+=str(gamma[i])
print(final)

for i in range(len(gamma)):
    if gamma[i]==1:
        gamma[i]=0
    else:
        gamma[i]=1
    rate+=str(gamma[i])
    
print(final)
print(rate)
print(int(final,2) * int(rate,2))