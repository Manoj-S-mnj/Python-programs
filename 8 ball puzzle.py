#Puzzle | 8 balls problem
#Puzzle: You are provided with 8 identical balls 
#And a measuring instrument. 7 of the eight balls are equal in weight 
#And one of the eight given balls is defective and weighs less. 
#The task is to find the defective ball in exactly two measurements.

def lightWeightBall(balls):
    group_A = balls[0:3]
    group_B = balls[3:6]
    group_C = balls[6:]

    A = sum(group_A)
    B = sum(group_B)
    C = sum(group_C)

    if A == B:
        if group_C[0] < group_C[1]:
            return balls.index(group_C[0])
        else:
            return balls.index(group_C[1])
    else:
        if A < B :
            lighterBallGroup = group_A
        else:
            lighterBallGroup = group_B
        if lighterBallGroup[0] < lighterBallGroup[1]:
            return balls.index(lighterBallGroup[0])
        elif lighterBallGroup[0] > lighterBallGroup[1]:
            return balls.index(lighterBallGroup[1])
        else:
            return balls.index(lighterBallGroup[2])

balls = [2,1,2,2,2,2,2,2]
print(lightWeightBall(balls))