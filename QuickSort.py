def quick(nums):
    length = len(nums)
    if length <= 1:
        return nums
    else:
        pivot = nums.pop()
    items_greater = []
    items_smaller = []
    for i in nums:
        if i > pivot:
            items_greater.append(i)
        else:
            items_smaller.append(i)
    return quick(items_smaller)+[pivot]+quick(items_greater)

print(quick([2,1,5,4,7,6]))
