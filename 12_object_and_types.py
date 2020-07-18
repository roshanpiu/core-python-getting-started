""" Python creates and Int Object with value of 1000
    And object reference with name x and refers x to Int Object"""
x = 1000

""" Python creates a new Int Object with value of 500
    And redirects the x reference to point to new Int Object"""
""" In python Int are immutable and can't be changed"""
""" Python garbage collector will reclaim the Int 1000
    As it's no longer being used"""

x = 500

# id() returns a unique integer identifier for an object that is
# constant for the life of the object

a = 17000
print(id(x), id(a))

x = a
print(id(x))

# is check for the equality of identity
# checks whether two references points to the same object
print(a is x)

b = 1
c = 1
print(b is c)

t = 5
print(id(t))
t += 2  # augmented assignment not a mutating operations
print(id(t))

# Assignment operator only bind objects to names
# It never copies object by value

# lists are mutable objects
# when we modify s we also modify r
# because both references points to the same object
r = [1, 2, 3]
s = r
print(r, s)
s[0] = 2
print(r, s)
print(s is r)

# Python doesn't have variables in the sense of boxes holding a value
# Python has named references to objects

# value equality vs identity equality
# comparison by value can be controlled programatically
# identity equality is controlled by language runtime
p = [1, 2, 3]
q = [1, 2, 3]
print(p == q)  # True
print(p is q)  # False
