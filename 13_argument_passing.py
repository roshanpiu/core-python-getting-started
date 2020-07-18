import time
m = [9, 15, 24]

""" m and k refers to the same list object there for m is modified in side the function 
    if you want to change the copy of an object it's the responsibility of the function to do the copying"""


def modify(k):
    k.append(39)
    print("k =", k)


modify(m)
print(m)

f = [14, 23, 37]


def replace(g):
    """ when f is passed in both f and g refers to the same list object
        but when we assign a new list to g the g now refers to the new list created"""
    g = [17, 28, 45]
    print("g =", g)


print(f)
replace(f)

print(f)

x = [14, 23, 37]


def replace2(h):
    """ x is actually modified in this case because h and x points to the same list
        and inside the function we modify the actual list object h refers to """
    h[0] = 1000


print(x)
replace2(x)

print(x)

""" Function arguments are transferred using pass-by-object-reference """
""" References to objects are copied, not the objects themselves."""

""" Return statements uses same pass-by-object-reference as function arguments """


def f(d):
    return d


c = 1000
e = f(c)
print(c is e)

""" formal function arguments a specified when a function is defined with def
    are comma seperated list of arguments names these can be made optional"""

""" params with defaults must come after the params without defaults """


def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)


banner("Hello World!")
banner("Hello World!", "*")

# Message string is a positional argument
# border string is a keyword argument
# All the keyword arguments must be supplied after the positional arguments
banner("Sun, Moon and Stars", border="*")
banner(border="*", message="Sun, Moon and Stars")

# Def is a statement when executed binds a function definition to a function name
# Default arguments are evaluated only once when def is executed
# Immutable default values does not cause a problem
# But Mutable defaults can cause confusing effects


def show_time(arg=time.ctime()):
    print(arg)


show_time()


def add_spam(menu=[]):
    menu.append("spam")
    print(menu)
    return menu


breakfast = ['bacon', 'eggs']
add_spam(breakfast)

# Empty list for the default argument is created only once
# When the def statement is executed so subsequent call to add_spam
# will keep adding to the same default param created when function got defined
add_spam()
add_spam()
add_spam()

# ALWAYS USE IMMUTABLE OBJECT FOR DEFAULT ARGUMENT VALUES
# Solution


def add_spam_2(menu=None):
    if menu is None:
        menu = []
    menu.append("spam")
    print(menu)
    return menu


add_spam_2()
add_spam_2()
add_spam_2()
