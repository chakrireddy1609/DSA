def house(nums):
    rob1,rob2 = 0,0
    for n in nums:
        temp = max(rob1+n,rob2)
        rob1 = rob2
        rob2 = temp
    return rob2

print(house([1,2,3,1]))