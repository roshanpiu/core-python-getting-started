# Comprehensions - Concise syntax for describing lists, sets and dictionaries
# Readable and expressive Close to natural language
from math import factorial
from pprint import pprint as pp

sentense = "Hello World! From Python".split()

# List Comprehension Syntax
# Creates a new list with word lengths
# Expresson producing the new list's elements can be any python expression
wordslength = [len(word) for word in sentense]
print(wordslength)


f = [len(str(factorial(x))) for x in range(20)]
print(f, type(f))

# Set Comprehensions
s = {len(str(factorial(x))) for x in range(20)}
print(s)

# Dictionary Comprehensions
urls = {
    'Google': 'https://google.com',
    'Pluralsight': 'https://pluralsight.com'
}

pp(urls)

# When duplicate keys the later keys replaces the older ones
inverted_urls = {url: name for name, url in urls.items()}
pp(inverted_urls)

############################## Filtering Comprehensions #################################

from math import sqrt

def is_prime(x):
  if x < 2:
    return False
  for i in range(2, int(sqrt(x)) + 1):
    if x % i == 0:
      return False
  return True

primes = [x for x in range(101) if is_prime(x)] 
print(primes)

# Don't use overuse comprehensions which impacts the readability
# Comprehensions should normally have no side-effects
# Comprehensions and for loops iterates over the entire for loop by default

# Having a good understanding on how to work with iteration is often the key to designing elegant and sophisticated solutions