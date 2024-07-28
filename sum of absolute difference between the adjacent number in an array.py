#sum of absolute difference between the adjacent number in an array


def sumofabsoluteDifference(a,p):
    if p > len(a)-1:
        return "Out of Index Range"
    else:
        return (a[p]-a[p-1]) + (a[p]-a[p+1])

n = int(input("Enter array size N : "))
a = []
for i in range(0,n):
    arr = int(input())
    a.append(arr)
p = int(input("P : "))
print(sumofabsoluteDifference(a,p))
