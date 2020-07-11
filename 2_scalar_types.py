# python comes with number of built in data types
# primitive scalar types like integers and collection types like dictionaries

#########  BASIC SCALAR TYPES #########

# Int
# Float
# NoneType
# Bool

############### Int type #################

# unlimited precision signed integers

int1 = 1
int2 = int(3.5)
int3 = int(-3.5)
int4 = int("35")
int5 = int("10000", 3)

print(int1, int2, int3, int4, int5)

############### Float type #################

# IEEE-753 double-precision with 53-bits of binary precision
# Any number with a decimal point interpreted by python as a float
# Any calculation with int and float promoted to a float

float1 = float(7)
float2 = float("1.614")
float3 = float("nan")
float4 = float("inf")
float5 = float("-inf")

print(float1, float2, float3, float4, float5)

############### None type #################

# Represents absence of a value

none1 = None
print(none1, none1 is None)

############### Bool type #################

# Contains logical states used in control flow structures

true = True
false = False
bool1 = bool(0)
bool2 = bool(1)
bool3 = bool(-1)
bool4 = bool([])
bool5 = bool([1, 2, 3])
bool6 = bool("True")  # True
bool7 = bool("False")  # False


print(true, false, bool1, bool2, bool3, bool4, bool5)
