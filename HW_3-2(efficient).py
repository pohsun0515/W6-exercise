# HW3-2: (初級)  Two Sum

nums = [2, 7, 11, 15]
target = 9

A=[]
for i in range(len(nums)) :
    if nums[i] >= 9 : break
    for j in range(i+1,len(nums)) :
        if nums[j] >= 9 : break
        if nums[i] + nums[j] == target : A.append((i,j))
print(*A)