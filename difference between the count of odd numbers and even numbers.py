# Write a python program to find the 
# difference between the count of odd numbers and even numbers

def differenceCount(a):
    OddCount = 0
    EvenCount = 0
    for i in range(0,len(a)):
        if a[i]%2 == 0:
            EvenCount+=1
        else:
            OddCount+=1
    if EvenCount > OddCount:
        return EvenCount - OddCount
    else:
        return OddCount - EvenCount 

a = [2,23,45,67,12,34,56,78,90,23,23,11,21,111,17,67]
print("difference between the count of odd numbers and even numbers",differenceCount(a))