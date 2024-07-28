# Build a program that will allow you to find out how many clothing pieces in total of a certain length 
# can be extracted from a particular number of cloth pieces. We can take the required length for each 
# clothing piece as 10 feet.
# In this case, we must first decide upon the length unit as feet and determine the inputs we need. 
# For this function, we will need two inputs, first the number of pieces ( in the array) and 
# the size of each piece in feet inside the array.
# A cloth merchant has some pieces of cloth of different lengths. 
# He has an order of curtains of length 12 feet. He has to find how many curtains can be made from 
# these pieces. Length of pieces of cloth is recorded in feet.
# For example, suppose the total number of elements is 3 and these are the elements:
# 0 10 40
# Then, the first input is 3 followed by the second input of 0, 10 and 40.
# Hence, the sum would be a total of 0 + (10/10) + (40/10) = 5
# Thus, there could be 5 pieces of clothing extracted from these 3 pieces of cloth of variable sizes.

def numberofclothpiece(x,y):
    piece = 0
    for i in range(0,len(x)):
        piece += (x[i]/y)
    print(piece)

a = [10,15,20,45]
constant_length = 5
numberofclothpiece(a,constant_length)