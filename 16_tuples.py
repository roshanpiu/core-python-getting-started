# Tuples are Immutable sequences of arbitrary objects

t = ('Norway', 4.445, 3)
print(t[0])
print(t[2])

for item in t:
    print(item)


print(t + (213213.22, 213213.22))
print(t * 3)

t2 = ((1, 2), (3, 4))
print(t2[0][0])

t3 = (1,)  # single element tuple
t4 = ()  # empty tuple

t5 = 1, 2, 3, 4, 5  # tuple without paranthesese
print(t5)


def minmax(items):
    return min(items), max(items)  # returns a tuple of two values


print(minmax([1, 2, 3, 4]))

# Tuple unpacking - Destructuring operations that unpacks data structures into named references
lower, upper = minmax([1, 2, 3, 4])
print(lower, upper)

# Nested tuple unpacking
(a, (b, (c, d))) = (4, (3, (2, 1)))
print(a, b, c, d)

a = 'Jelly'
b = 'bean'

print(a, b)
# first right hand side pack a and b to a tuple
# then left had side unpacks the tuple into a and b
# swapping the original values
a, b = b, a

print(a, b)

t6 = tuple([1, 2, 3])  # creating tuple from an existing collection object
t7 = tuple("Hello")
print(t6)
print(t7)

# Check for if exists or not

if 1 in t6:
    print('In')

if 10 not in t6:
    print('Not In')
