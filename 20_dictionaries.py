urls = {
    'Google': 'https://google.com',
    'Pluralsight': 'https://pluralsight.com'
}

# Keys must be unique in dictionaries
# Key must be immutable
# Value can be muttable
print(urls['Google'])

# dict constructor can be used to convert iterable series to dictionaries
names_and_ages = [('Alice', 32), ('Bob', 28)]
d = dict(names_and_ages)
d1 = dict(a=1, b=2, c=3)
print(d)
print(d1)

# Dictionary copying is a shallow
# Methods to copy
d2 = d1.copy()
d3 = dict(d1)

# Adds entries from one dictionary into another
dict.update(d1, {'d': 4})
print(d1)

for key in d1:
    print(f"{key} => {d1[key]}")

for value in d1.values():
    print(f"{value}")

# dict.items() iterates over keys and values in tandom
# yields a (key, value) tuple on each iteration
for key, value in d1.items():
    print(f"{key} => {value}")

# in and not in works on dict keys
print('a' in d1)
print('a' not in d1)

# del can be used for deleting element
del d1['a']
print(d1)
