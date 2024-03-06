def oneBits(num):
    res = 0
    while num:
        res += num%2
        num = num >> 1
    return res