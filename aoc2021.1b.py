import fileinput
nums=[]
increase = 0
for line in fileinput.input():
  nums.append(int(line))
print(nums)

groups = []
for i in range(len(nums)-2):
    sum = nums[i] + nums[i+1] +nums[i+2]
    groups.append(sum)
for i in range(len(groups)-1):
  if(groups[i]<groups[i+1]):
    increase+=1
print(increase)
