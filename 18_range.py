# Range is a sequence representing an arithmetic progression of integers

r1 = range(5)
print(r1)  # start value defaults to 0

for i in range(5):
    print(i)

r2 = range(5, 10)
range_list = (list(range(5, 10)))
print(range_list)

print(list(range(0, 10, 2)))  # count 0 to 9 by 2s 2 is the step

start, stop, step = 0, 10, 2
range(stop)
range(start, stop)
range(start, stop, step)

# Range does not support keyword arguments

# Enumerate - Constructs an iterable of (index, value) tuples around another iterable object

t = [1, 2, 3, 4]

for p in enumerate(t):
    print(p)

# with tuple unpacking
for i, v in enumerate(t):
    print(f"Index = {i}, Value = {v}")
