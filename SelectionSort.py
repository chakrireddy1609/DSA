def selection(nums):
    indexing_length = range(0,len(nums)-1)
    for i in indexing_length:
        min_value = i
        for j in range(i+1,len(nums)):
            if nums[j]<nums[min_value]:
                min_value = j
        if min_value != i:
            nums[min_value],nums[i]=nums[i],nums[min_value]

    return nums


print(selection([2,1,3,1,6,5,4]))