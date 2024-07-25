# Program that counts the given charecter 
# In the given String

s = input("Enter string Value : ")
c = input("Enter the cchar to count : ")
count = 0
for i in range(0,len(s)-1):
    if s[i] == c:
        count+=1
print(count)