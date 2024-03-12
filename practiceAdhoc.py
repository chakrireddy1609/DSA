from collections import Counter


def majorityElement(nums):
    c = Counter(nums)
    print(max(c))
majorityElement([2,2,1,1,1,2,2])