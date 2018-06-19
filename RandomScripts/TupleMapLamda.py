 Playing with tuple, map and lambda 

names = ("Bill", "Tom", "Sam", "Joe")

repeated = tuple(map(lambda x: (x +' ')*5, names))

print(repeated)
