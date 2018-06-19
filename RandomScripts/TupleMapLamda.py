"""
Created by: Alex J. Gatz
Date: 06/08/2018
"""

# Playing with tuple, map and lambda 

names = ("Bill", "Tom", "Sam", "Joe")

repeated = tuple(map(lambda x: (x +' ')*5, names))

print(repeated)
