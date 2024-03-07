def guessNumber(n):
    l,r = 1,n
    while l < r:
        m = (l+r)//2
        res = guess(m)
        if res > 0:
            l = m+1
        elif res < 0:
            r = m-1
        else:
            return m

