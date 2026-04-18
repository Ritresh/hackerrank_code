
# Day 11: Binary Numbers
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input().strip())
    binary = bin(n)[2:]
    ones=binary.split('0') # only group of 1 
    max_count=0# find max length
    for i in ones:
        if len(i)> max_count:
            max_count=len(i)
    print(max_count)
    
# Day 12: 2D Arrays
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    max_sum = -63 # minimum possible hourglass sum
    for i in range(4):
        for j in range(4):
            hourglass_sum=(
                arr[i][j]+arr[i][j+1]+arr[i][j+2]+
                arr[i+1][j+1]+
                arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]  
            )
            if hourglass_sum>max_sum:
                max_sum=hourglass_sum
    print(max_sum)

# Day 13: Inheritance
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)
class Student(Person):
    #   Class Constructor
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        avg = sum(self.scores) / len(self.scores)

        if avg >= 90:
            return 'O'
        elif avg >= 80:
            return 'E'
        elif avg >= 70:
            return 'A'
        elif avg >= 55:
            return 'P'
        elif avg >= 40:
            return 'D'
        else:
            return 'T'

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())