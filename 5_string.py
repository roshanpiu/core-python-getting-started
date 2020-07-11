############### String type #################
# str -> Data type for string in Python
# Sequence of Unicode code points
# String are Immutable
# Considered sequence types
str("hello world")
str('hello world')
str("'hello' world")

# Moment of Zen
# Practicality beats purity
# Beautiful text strings 
# Rendered in literal form 
# Simple elegance

############### Multi line String ####################
""" Hello
    This is a 
    Multiline sting """

# Escape sequences 

print('Python\'s way of Escape')

# raw strings

path = r'C:\Users'
print(path)

s = "parrot"
print(s[4])

print(type(s))
print(type(s[4]))

c = "oslo"
print(c.capitalize())
print(c) # String unchanged because it's immutable