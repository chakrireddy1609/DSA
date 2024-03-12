def bubble(nums):
    indexing_length = len(nums)-1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0,indexing_length):
            if nums[i]>nums[i+1]:
                sorted = False
                nums[i],nums[i+1]=nums[i+1],nums[i]
    return nums


print(bubble([2,1,5,4,7,6]))