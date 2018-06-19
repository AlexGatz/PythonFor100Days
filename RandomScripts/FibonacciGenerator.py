"""
Created By: Alex J. Gatz
Date: 06/06/2018

This is some code playijg with the usage of a python 
"Generator" which is really very cool. Another use case
I want to play with is properly ordering installation of
packages to ensure that if there are dependencies that they are installed in the proper order. 
"""

# Fibonacci generator
def fibonacci(n): 
    a, b, counter = 0, 1, 0 
    while True: 
        if (counter > n): 
            return 
        yield a 
        a, b = b, a + b 
        counter += 1 

# How many values donyou want?
f = fibonacci(30) 

# Iterate multiple calls of the fibonacci generator
for x in f: 
    print(x, " ", end="")
