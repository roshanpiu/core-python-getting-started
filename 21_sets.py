# Sets are unordered collections for unique elements
# Sets are mutable
# Elements in a set must be immutable

s1 = {1, 2, 3, 4}
print(s1, type(s1))

# Can be used to remove duplicates
s2 = set([1, 2, 3, 3])
print(list(s2))

# membership and non-membership
1 in s2
10 not in s2

s2.add(10)
print(s2)
s2.remove(10)
print(s2)

# Shallow copying sets
s3 = s2.copy()
s4 = set(s2)

# Set Algebra and operations

blue_eyes = {'Olivia', 'Harry', 'Lily', 'Jack', 'Amelia'}
blond_hair = {'Harry', 'Jack', 'Amelia', 'Mia', 'Joshua'}
smell_hcn = {'Harry', 'Amelia'}
taste_ptc = {'Harry', 'Lilly'}

print(blond_hair.union(blue_eyes))
print(blond_hair.intersection(blue_eyes))
print(blond_hair.symmetric_difference(blue_eyes))
print(blue_eyes.issuperset(smell_hcn))