import datetime
import math
string_length = len("Hello")

print(string_length)

s1 = "Hello" + "World"
print(id(s1))
s1 += "!"
print(s1)
print(id(s1))

# Strings are immutable
# modifying s1 is possible because s1 is a reference to an object
# not the object it self

# Use str.join() to Join String is more efficient
# + operator for string concatenation results in temporaries which impacts memory

colors = ';'.join(['red', 'green', 'blue'])
print(colors)
print(colors.split(';'))

s2 = ''.join(['high', 'way', 'man'])
print(s2)

# THE WAY MAY NOT BE OBVIOUS AS FIRST
# To concatenate Invoke join on empty text

s3 = "unforgettable".partition('forget')  # returns a tuple
print(s3)

# _ is for unused (dummy) values this is a convension
origin, _, destination = "Seattle-Boston".partition('-')
print(origin, destination)

# String formatting
s4 = "{0} north {1} east".format(57, 10)
print(s4)

# format with positional arguments
s5 = "Current position {lat} {lon}".format(lat=10, lon=20)
print(s5)

# Indexing a tuple
s6 = "Galactic position x={pos[0]}, y={pos[1]}, z={pos[2]}".format(
    pos=(1, 2, 3))
print(s6)

s7 = "Math constants: pi={m.pi}, e={m.e}".format(m=math)
print(s7)

# F-string allows to evaluate expressions inside strings

s8 = f"one plus one is {1+1}"  # evaluated and inserted at runtime
print(s8)

value = 4 * 20
s9 = f'The value is {value}'
print(s9)

# Floating point formatting
s10 = f"Math constants: pi={math.pi:.3f}, e={math.e:.3f}"
s11 = f"The current time is {datetime.datetime.now().isoformat()}"
print(s10)
print(s11)

# prints string methods
print(help(str))
