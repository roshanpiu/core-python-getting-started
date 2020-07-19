# Iteration protocols
# Iterable Objects - Can be passed to iter() to produce an iterator
# Iterator Objects - Can be passed to next() to get the next value in the sequence

# For loops and comprehensions are built on top of these low level iteration protocols
iterable = ['Spring', 'Summer', 'Autumn', 'Winter']
iterator = iter(iterable)
print(next(iterator))
print(next(iterator))
print(next(iterator))

# StopInteration exception is raised when there are no more values to iterate
def first(iterable):
  iterator = iter(iterable)
  try:
    return next(iterator)
  except StopIteration:
    raise ValueError("iterable is empty")

print(first(iterable))