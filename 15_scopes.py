# No type declarations are necessary in python
# Variable are just untyped name bindings to objects
# Variable can be rebound to objects of different types

# Scopes in python (from narrow to broadest)
# Local - Inside the current function
# Enclosing - Inside enclosing functions
# Global - At the top level of the module
# Built-in - In the special builtins module

# Names are looked up from narrowest to broadest context

# Scopes in Python do no correspond to source code blocks 

# Module name bindings are typically introduced by import statements and function or class definitions
# Typically for defining contants we use module scope

# modifying global scoped object with in a function

count = 0

def show_count():
  """ Function documentation string """
  print(count)

def set_count(c):
  #count = c # This doesnot modifies the global count
  global count # This does
  count = c

show_count()
set_count(5)
show_count()

# SPECIAL CASES ARE NOT SPECIAL ENOUGH TO BREAK THE RULES
# WE FOLLOW PATTERNS NOT TO KILL COMPLEXITY BUT TO MASTER IT

# All variables in Python are references to objects. even the basic types like Integers
# Everthing in Python are an Object including functions and modules

print(type(show_count)) # determines the type
print(dir(set_count)) # shows the attributes of an object
 
print(set_count.__name__) # prints the function name 
print(show_count.__doc__) # prints the function documentation string

##################################  NOTES  ##############################################

# Python uses name references to object
# Assignment attaches a name to an object
# Assigning one name to another points them both to the same object
# The garbage collector removes objects with no references
# is determines if tow names refer to the same object
# Function arguments are passed by object references to mutable arguments can be modified
# If a formal argument is rebound through assignment the original object reference is lost 
# return passes back an object reference to the caller
# default argument only evaluated once when function is defined 
# Python names are looked up using LEGB rule
# import and def results in binding to named references