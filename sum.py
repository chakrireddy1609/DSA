def sum(nums,target):
    prevMap ={}
    for i,n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff],i]
        prevMap[n]=i

print(sum([1,2,3,4],7))