def replaceGreatest(arr):
    rightMax = -1
    for i in range(len(arr)-1,-1,-1):
        newMax = max(rightMax,arr[i])
        arr[i]=rightMax
        rightMax = newMax
    return arr

print(replaceGreatest([17,18,6,5,2,1]))