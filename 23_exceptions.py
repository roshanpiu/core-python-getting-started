# When the program can't follow it's normal execution path exceptions are raised
# Exception handling is machanism for interrupting normal program flow and continuing in surrounding context

# Key concepts
# Raising, Handling, Unhandled
# Exception object contains information

from math import log
import sys
DIGIT_MAP = {
    'zero':   '0',
    'one':    '1',
    'two':    '2',
    'three':  '3',
    'four':   '4',
    'five':   '5',
    'six':    '6',
    'seven':  '7',
    'eight':  '8',
    'nine':   '9'
}

# try contains the block that could raise an exception
# except block contains code that hanles an exception
# except block can accept a tuple of exception types


def convert(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print(f"Conversion succeeded! x = {x}")
    except (KeyError, TypeError) as e:
        print(f"Conversion error: {e!r}", file=sys.stderr)
        raise ValueError()  # re raises a built in exception
    return x


def string_log(s):
    v = convert(s)
    if s == -1:
        raise ValueError()
    return log(v)


print(convert("one three three seven".split()))

print(convert("Hello".split()))

print(convert(123))

# Exceptions resulting from programmer error such as IndentationError, SyntaxError, NameError
# These should almost never be caught

# except (KeyError, TypeError):
#      pass
# Can be used as an empty exception block that doesn't do anything

# EXCEPTIONS ARE PART OF FUNCTION'S API AND MORE BROADLY PART OF CERTAIN PROTOCOLS
# Ex - Object that implement sequence protocol should raise IndexError for out-of-bounds indexing
# Exceptions that are raised from a function as important as it's arguments
# therefor they should be documented correctly
# Existing built in exception types are often the right choice
# Type follow established patterns. it's easier for others to integrate

def lookup(key, collection):
  if key not in collection:
    raise KeyError()
  return collection[key]

# Common exceptions 
# IndexError - An integer index is out of range
# ValueError - An object is of the correct type but has an inappropriate value
# KeyError - When a lookup in a mapping is failed

# Avoid type checks and raise exceptions - this goes against dynamic nature of Python
# Not worth adding type checking to your functions

# Prepare for failure - 2 approaches
# 1 - Check all preconditions - (LBYL - Look Before You Leap)
# 2 - Prepare for consequences - (EAFP - Easier to Ask Forgiveness than Permission)

# PYTHON PREFERS EAFP - THE CODE HAPPY PATH IS EMPHASIZED RATHER THAN BEING INTERSPERSED WITH ERROR HANDLING
# Attempt the operation without any in advanced checks but have error handler in place to deal with errors
# EAFP - is enabled by exceptions
# Exceptions can not be easily ignored, Error code are silent by default

# CLEAN UP AFTER EXCEPTIONS - finally block is used for this
# Finally block is always executed in all cases

# ERRORS SHOULD NEVER PASS SILENTLY UNLESS EXPLICITLY SILENCED

import os
import sys

def make_at(path, dir_name):
  original_path = os.getcwd()
  os.chdir(path)
  try:
    os.makedirs(dir_name)
  except OSError as e:
    print(e, file=sys.stderr)
    raise
  finally:
    os.chdir(original_path)