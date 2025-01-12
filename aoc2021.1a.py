import fileinput
nums=[]
increase = 0
for line in fileinput.input():
  nums.append(int(line))
print(nums)
for i in range(len(nums)-1):
  if(nums[i]<nums[i+1]):
    increase+=1
print(increase)
