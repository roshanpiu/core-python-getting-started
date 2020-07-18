# Python has a dynamic and strong type system
# Dynamic typing - type of an object reference isn't resolved until to program is running

def add(a, b):
    print(a + b)
    return a + b


add(5, 7)
add(3.1, 2.4)
add("news", "paper")
add([1, 6], [21, 10])

# causes a type error
# PYTHON WILL NOT GENERALLY PERFORM IMPLICIT CONVERSION BETWEEN TYPES
# add("add", 5.7)

# THE EXCEPTION TO THIS CASE IS IF AND WHILE PREDICATE CONVERSIONS TO BOOL
a = "1"
if a:
    print(a)
