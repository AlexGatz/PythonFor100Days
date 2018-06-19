"""
Created By: Alex J. Gatz
Date: 06/06/2018
Some random test code playing with sorting a dictionary and outputing the sorted values inna list.
"""

nameAge_dict = {'Alex':27, 'Taunee':26, 'Andrew':25, 'James':50, 'Marla':49}

# This is really key sort and value sort 
alphaSort = sorted(nameAge_dict, key=str.lower)
ageSort = sorted(nameAge_dict.values())

print(nameAge_dict)
print(alphaSort)
print(ageSort)
