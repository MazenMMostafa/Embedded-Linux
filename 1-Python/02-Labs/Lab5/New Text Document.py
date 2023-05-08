# Create two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Check if set1 is a subset of set2
if set1.issubset(set2):
    print("set1 is a subset of set2")
else:
    print("set1 is not a subset of set2")

# Check if set2 is a superset of set1
if set2.issuperset(set1):
    print("set2 is a superset of set1")
else:
    print("set2 is not a superset of set1")

# Find the intersection of set1 and set2
intersection_set = set1.intersection(set2)
print("The intersection of set1 and set2 is:", intersection_set)

# Remove elements from set1 that are in set2
set1.difference_update(set2)
print("The updated set1 is:", set1)

# Create a new set with elements that are in either set1 or set2, but not both
symmetric_difference_set = set1.symmetric_difference(set2)
print("The symmetric difference of set1 and set2 is:", symmetric_difference_set)
