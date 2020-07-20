# Classes - Define the structure and behavior of objects
# Act as a template for creating new objects and controls object's initial state, attributes and methods
# Classes can make simple problems unnecessarily complex
# Python Let's you strike the right balance between python and classes
# All types in python has a class 
# Object's class is set when it's initialized and fixed for the object's lifetime
# Defining Classes

from pprint import pprint as pp


class Flight:
    """ A flight with a particular passenger aircraft."""

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}'")
        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code '{number}'")
        if not (number[:2].isalpha() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalid airline code '{number}'")
        self._number = number  # assigning to non existing attribute _number creates it
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + \
            [{letter: None for letter in seats} for _ in rows]

    def aircraft_model(self):
        return self._aircraft.mode()

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def allocate_seat(self, seat, passenger):
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError(f"Invalid seat letter {letter}")
        row_text = seat[:-1]
        try:
            row = int[row_text]
        except ValueError:
            raise ValueError(f"Invalid seat row {row_text}")

        if row not in rows:
            raise ValueError(f"Invalid row number {row}")

        if self._seating[row][letter] is not None:
            raise ValueError(f"Seat {seat} already taken")

        self._seating[row][letter] = passenger

    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self._seating
                   if row is not None)


class Aircraft:
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self._num_rows + 1), "ABCDEFGHJK"[:self._num_seats_per_row])


a = Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6)
f = Flight("BA758", Aircraft("G-EUPT", "Airbus A319",
                             num_rows=22, num_seats_per_row=6))

pp(f._seating)
print(f.num_available_seats())

print(a.model())
print(a.registration())
print(a.seating_plan())


f = Flight("SN160", a)

print(type(f))
print(f.number())
f.number()  # is syntactic sugar for
f.number()

f2 = Flight("SN160", a)
print(f2.number())
print(f2._number)  # not a good approaches

# in python classes no access modifiers everything is public and can be accessed
# private attributes are defined with naming convension underscore

# methods are just functions defined inside a class
# instance methods must accept a reference to the actual instance on the which the method was called as first argument
# by convension it's called self

# __init__() instance method for initializing new objects

# __init__() is not a constructor it's an initializer for already created object
# python rumtime checks for the instance initializer __init__() and calls it when it's present
# initializer doesnot return anything it just modifies the object referred to by self
# _number is used because by convension implementation details that are not exposed to the client prefixed with _

# Class invariants - Truths about an object that endures for it's lifetime.
# It's a good practice for a initializer of an class of establish Class invariants

# The low of Demeter - the principle of least knowledge
# You should never call methods on objects you receive on other calls

# OOP principle - Tell Don't ask - Tell other objects what to do instead of asking them their state and responding to it

# Polymorphism - using object of different types through a uniform interface
# It applies to both functions and as well as more complex types

# Polymorphism is python is done through duck typing
# "If it walks like a duck, looks like a duck and shouts like a duck I call it a duck"
# An object's fitness for use is only determined at use(at runtime)

# Inheritance - inherit attributes and behavior
# 1. Normally-typed languages use inheritance for polymorphism
# 2. Python uses late bining
# 3. You can try any method on any object

# Inheritance in Python is primarily useful for sharing implementation between classes
# Inheritance is used less in Python


class Animal:
    def identify(self):
        pass


class Dog(Animal):
    pass
