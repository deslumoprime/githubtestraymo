import random

# roll() — Returns the sum of the first nondouble dice roll 
def roll():
    double = False
    tries = []
    for i in range(3):
        tries.append([random.randint(1,6), random.randint(1,6)])
    
    print(tries)
    for j in tries:
        if (j[0] == j[1]):
            double = True
        else:
            return (j[0] + j[1]) 

print("done")
