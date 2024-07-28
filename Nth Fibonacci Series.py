def findFibonacci(n):
    a = 0 
    b = 1
    print(a)
    print(b)
    for i in range(0,n):
        c=a+b
        a,b = b,c
        print(c)

n=int(input("Enter N value : "))
findFibonacci(n)