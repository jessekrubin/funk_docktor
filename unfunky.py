"""
some docstring
"""

from math import sqrt

def sqrt_mul(a, b): #$# function name and stuff w documentation
    return sqrt(a * b) #$# return the square root of a times b

def main(): #$# main function called from name main thingy
    some_list = [] #$# a list we do some stuff wit
    for i in range(10): #$# for i in range...
        for j in range(100): #$# for j in range...
            # p = sqrt_mul(i, j) #$# calculate the the sqrt_mul and set to p
            p = sqrt_mul(i, j) #$# calculate the the sqrt_mul and set to p
            some_list.append(p) #$# append p to that list some list
    return sum(some_list) #$# return something liek the sum of the list

if __name__ == '__main__': #$# if name is main
    result = main() #$# run main
    print("RESULT: {}".format(result)) #$# print and format the result
