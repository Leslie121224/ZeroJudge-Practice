n = int(input())
if n <= 100000000 and n > 1:
    list1 = []

    for i in range(2, int(n+1)):
        while n % i == 0:
            list1.append(i)
            n = n // i    
        if list1.count(i) != 0:
            print(i,end = '')
            if list1.count(i) > 1:
                print("^",list1.count(i),sep ='',end = '')
            if n * i != list1[-1]:
                print(" * ",sep = '', end = '') 
    
