def insertion(nums):
    indexing_length = range(1,len(nums))
    for i in indexing_length:
        while nums[i-1]>nums[i] and i > 0:
            nums[i],nums[i-1] = nums[i-1],nums[i]
            i-=1
    return nums

print(insertion([2,1,5,4,7,6]))