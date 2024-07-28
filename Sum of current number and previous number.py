# Sum of current number and previous number

def sumofCNandPN(arr,l):
    for i in range(1,l):
        sum = 0
        sum = arr[i] + arr[i-1]
        print(sum)
            

a = [0,1,3,5,6,7,9]
sumofCNandPN(a,len(a))