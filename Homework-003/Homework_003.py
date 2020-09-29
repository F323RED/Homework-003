'''
Author : F323RED
Date : 2020/9/29
Version : 0.1.0
Describe : Python homework-003
'''

import pylab as lab
import math

def F(x) :      # Define function F()
    return math.sin(x) / abs(2 * x) + 10e-8     # Prevent divide by 0

#---------------------
# Begining of program

a = 10 * math.pi
b = -a                           # X c [-10 * PI, 10 * PI]
n = 1000                        # Number of points

listX = lab.linspace(a, b, n)
listY1 = [F(i) for i in listX ]

# Some fancy stuff
lab.title("f(x) = sin(x) / |2x|")
lab.xlabel("X axis")
lab.ylabel("Y axis")
lab.grid()

lab.plot(listX, listY1)         # Draw graph of F(x)

lab.show()                      # Show graph
