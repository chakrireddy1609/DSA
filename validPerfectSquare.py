def validSquare(num):
    l,r = 1,num
    while l <=r:
        mid = (l+r)//2
        if mid * mid > num:
            r-=1
        elif mid * mid < num:
            l+=1
        else:
            return True
    return False


print(validSquare(25))