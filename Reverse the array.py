# With Using new Array
def reversetheArrray(a):
    b=[]
    for i in range(len(a)-1,-1,-1):
        b.append(a[i])
    print("Reversed Array : ",b)
#Without Extra array
def anotherReverse(c):
    i = 0
    j = len(a)-1
    while i <= j:
        c[i],c[j] = c[j],c[i]
        i+=1
        j-=1
    print(c)
#Variables and Arrays        
a = [1,2,3,4,5]
reversetheArrray(a)
anotherReverse(a)