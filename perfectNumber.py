def checkPerfectNumber(num):
    """
    :type num: int
    :rtype: bool
    """
    sum = 0
    for i in range(1, (num // 2) + 1):
        if (num % i) == 0:
            sum += i
    if num == sum:
        return True
    else:
        return False

print(checkPerfectNumber(33550336))
