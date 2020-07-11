import math
from math import factorial
from math import factorial as fac

print(math.sqrt(81))

n = 100
k = 2
print(fac(n) // (fac(k) * fac(n-k)))

print(fac(n))

# printed out put is a side effect of the function
# not a return value
print(len(str(fac(n))))

for target_list in [1, 2, 3]:
    print('!!!!!!!', target_list)
