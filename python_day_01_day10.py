
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

# Day 06: Loops
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input().strip())
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

# Day 07: Let's Review
# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for i in range(t):
    s = input()
    even_char = s[::2]
    odd_char = s[1::2]
    print(f'{even_char} {odd_char}')
    
# Day 08: Array
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    reverse_arr = arr[::-1]
    print(*reverse_arr)

# Day 09: Dictionaries and Maps
n = int(input())
phone_book ={}
for i in range(n):
    name, number = input().split()
    phone_book[name]=number
# taking input 
while True:
    try:
        query=input()
        if query in phone_book:
            print(f"{query}={phone_book[query]}")
        else:
            print("Not found")
    except EOFError:
        break

# Day 10: Recursion 
import math
import os
import random
import re
import sys
# Complete the 'factorial' function below.
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
def factorial(n):
    # Write your code here
    result=1
    for i in range(1, n+1):
        result *= i
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    result = factorial(n)
    fptr.write(str(result) + '\n')
    fptr.close()
