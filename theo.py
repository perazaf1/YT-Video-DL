from math import *

def find_number():

    x = 1 

    while True :
        
        cond1 = x%2 == 1
        cond2 = x%3 == 2
        cond3 = x%4 == 3
        cond4 = x%5 == 4
        cond5 = x%6 == 5

        if cond1 and cond2 and cond3 and cond4 and cond5:

            print(f"La solution est x = {x}")

            break
        
        x += 1

find_number()