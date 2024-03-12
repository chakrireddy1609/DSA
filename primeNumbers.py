def primeNumbers(a,b):
    for i in range(a,b+1):
        for k in range(2,i):
            if i%k==0:
                break
        else:
            print(i)
primeNumbers(5,10)