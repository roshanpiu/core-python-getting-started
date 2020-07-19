# Generator functions - Iterables defined by functions, lazy evaluation
# Must include yield keyword at least once inside the function
# May also contain return statement

from math import sqrt
from itertools import count, islice, chain


def gen123():
    yield 1
    yield 2
    yield 3


# Create two iterator object
g = gen123()
h = gen123()
print(g)
print(id(g), id(h), g is h)

print(next(g))
print(next(g))
print(next(g))


def get246():
    print('About to yield 2')
    yield 2
    print('About to yield 4')
    yield 4
    print('About to yield 6')
    yield 6
    print('About to return')


g = get246()
next(g)
# when called next the generator resumes from where it left off
next(g)

# maintaining state in generators


def take(count, iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def run_pipeline():
    items = [3, 6, 6, 2, 1, 1]
    for item in take(3, distinct(items)):
        print(item)


run_pipeline()

# LAZINESS AND THE INFINITE
# Generators only do enough work to produce requested data
# This allows generators to model infinite (or just very large) sequences
# Usecases - sensor readings, Mathematical sequences, Contents of large files


def lucas():
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a, b = b, a + b


# for x in lucas():
#     print(x)

print(next(lucas()))
print(next(lucas()))
print(next(lucas()))
print(next(lucas()))

# Generator Expressions - across between comprehensions and generator functions
# Creates a Generator object which results in procusing the specified sequence lazily
# Used when lazy evaluation of generators and declarativeness of comprehension is needed

million_squares = (x*x for x in range(1, 1000001))

# force evaluation of a generator resources heavily used
last = list(million_squares)[-10:]
print(last)

# Generators are single use objects
# To recreate a generator from a generator expression, you must execute the expression again

sum1 = sum(x*x for x in range(1, 1000001))
print(sum1)

sum2 = sum(x for x in range(1001) if x > 500)
print(sum2)


# Comprehensions, Generators or any object which follows iterable or iterator protocol can be used for iteration

# Python provides a powerful vocabulary for working with iterators
# ex - enumerate() and sum(). The itertools module provides many more


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
print(list(thousand_primes))

print(any([False, False, True]))  # True if any value in list is True
print(all([False, False, True]))  # True if all values in list are True

# are there any prime numbers between 1328, 1261
print(any(is_prime(x) for x in range(1328, 1261)))

print(all(name == name.title() for name in ['London', 'Paris', 'Colombo']))

# zip() synchronizes iteration across two or more iterables.

a1 = [1, 2, 3]
a2 = [4, 5, 6]
a3 = [7, 8, 9]

for item in zip(a1, a2):
    print(item)

for  items in zip(a1, a2, a3):
    print(f"min = {min(items)}, max = {max(items)}")

# No data duplication
print(all(t < 0 for t in chain(a1, a2, a3)))