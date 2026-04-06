
# Day 01- Say "Hello, World!" With Python
# Read a full line of input from stdin and save it to our dynamically typed variable, input_string.
input_string = input()
# Print a string literal saying "Hello, World." to stdout.
print('Hello, World.')
# TODO: Write a line of code here that prints the contents of input_string to stdout.
print(input_string)

# Day 02- Data Types
i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
i2 = 0
d2 = 0.0
s2 = ''
# Read and save an integer, double, and String to your variables.
i2 = int(input())
d2 = float(input())
s2 = input()
# Print the sum of both integer variables on a new line.
print(i + i2)
# Print the sum of the double variables on a new line.
print(d + d2)
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s + s2)
    
# Day 03: Operators
import math
import os
import random
import re
import sys
# Complete the 'solve' function below.
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    tip = meal_cost*tip_percent/100
    tax = meal_cost*tax_percent/100
    total_cost = meal_cost+tip+tax
    print(round(total_cost))
if __name__ == '__main__':
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())
    solve(meal_cost, tip_percent, tax_percent)
    
# Day 04: Intro to Conditional Statements
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    N = int(input().strip())
    if N % 2 != 0:
        print('Weird')
    else:
        if 2 <=N <=5:
            print('Not Weird')
        elif 6 <=N<=20:
            print('Weird')
        else:
            print('Not Weird')

# Day 05: Class vs. Instance
class Person:
    def __init__(self,initialAge):
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
            self.age=0
        else:
            self.age = initialAge
    def amIOld(self):
        if self.age<13:
            print("You are young.")
        elif self.age>=13 and self.age<18:
            print("You are a teenager.")
        else:
            print("You are old.")
    def yearPasses(self):
        self.age+=1
t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")
