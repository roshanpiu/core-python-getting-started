# Negative indices
# Index from the end of the sequence using negative numbers

# The last element is at index -1

# This applies to tuples and strings as well

r = [1, 2, 3, 4, 5, 6]
print(r[len(r)-1])
print(r[-1])  # The elegant way

# Slicing - Extended from of indexing for referring to a porting
# of a list or other sequence

print(r[1:3])  # Slices first and second element
print(r[1:-1])  # Get all except first and last elements

print(r[2:])  # slices from third element to end of the list

print(r[:4])  # slices from start to 4th element of the list

t = r
print(t is r)

t = r[:]  # IDIOM FOR COPYING THE LIST
print(t is r)
print(t == r)

# Eventhough we have a new list which can be independently modified
# The values inside reference to the same object referred to by the original list

# Other ways of copying
t = r.copy()
t = list(r)  # preferable since can work with any iterable series as the source

# All of these techniques performs a shallow copies
# Creates new list containing same object references from the source list

# Demo
a = [[1, 2], [3, 4]]
b = a[:]
print(a is b)
print(a[0] is b[0])
print(a[1] is b[1])

a[0] = [8, 9]

print(a, b)

# For performing deep copies use copy module from python std lib

# Initializes a list of a size with constant value
x = [0] * 9
print(x)

# When using mutable object as elements the repetition will repeat the reference

s = [[-1, +1]] * 5
print(s)
s[2].append(7)  # modifies every element in the list
print(s)

# Finds the location of an object in a list
# Returns the index of the first element which is equal to the argument
w = "Hello World".split()
print(w.index("Hello"))

del w[0]  # Removes the element from the list
print(w)

print(w.count("a"))

print(1 in [1, 2, 3])  # Checks for membership if 1 is in the list
# Checks for non membership if 10 is not in the list
print(10 not in [1, 2, 3])

y = [1, 2, 3]
y.remove(1)  # throws a value error if the value doesn't exist

y.insert(0, 4)
print(y)

# Concats lists
z = w + y
print(z)

z.extend([1])
print(z)

list1 = list(range(1, 10))
list1.reverse()
print(list1)

# Key parameter can be any callable object that accepts a single parameter
# Items passed to callable and sorted on it's return value

print(list("Hello World!".split()).sort(key=len))

# IN BUILT SORT AND REVERT CAUSES THE ARGUMENT OF A FUNCTION TO BE MODIFIED

# Safe method that does not mutate the original object
list3 = list(range(1, 10))
l4 = list(reversed(list3))
l5 = sorted(list3)
print(list3, l4, l5)
