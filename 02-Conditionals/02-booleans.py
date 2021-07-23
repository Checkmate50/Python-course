# The first thing you should do is run this program, it should print a bunch of garbage

# Part 1: Basic Booleans
# Fill in the following functions as defined by the comments:
# All can be written in one line (no if statements required!)  
#  To achieve this, think carefully about how booleans work

print("Part 1:")

# Returns True if any of the inputs are True, otherwise False
def big_or(x, y, z):
  return True
  
print(big_or(True, True, False))    # True
print(big_or(False, False, False))  # False
print(big_or(False, False, True))   # True
print()

# Returns True if either of the inputs are True, but not Both
# (XOR stands for _exclusive or_)
def xor(x, y):
  return True
  
print(xor(True, True))    # False
print(xor(True, False))   # True
print(xor(False, True))   # True
print(xor(False, False))  # False

# Returns True if x is a multiple of y, otherwise False
def is_multiple(x, y):
  return True
  
print(is_multiple(5, 2))  # False
print(is_multiple(8, 3))  # False
print(is_multiple(8, 2))  # True
print()

# Returns True if x ends with the number 8 or 9, otherwise False
# Hint: how does x % 10 work?
def ends_with_eight_or_nine(x):
  return True
  
print(ends_with_eight_or_nine(119))  # True
print(ends_with_eight_or_nine(132))  # False
print(ends_with_eight_or_nine(5738)) # True
print(ends_with_eight_or_nine(5737)) # False
print()

# Part 2: Boolean Conditions
# Fill out the following functions as described in the comments

print("Part 2:")

# Returns x + y if x and y are both negative
# Otherwise returns x * y
def funny_mult(x, y):
  return 0
  
print(funny_mult(-1, -3)) # -4
print(funny_mult(3, 4))   # 12
print(funny_mult(-2, 5))  # -10
print()

# Returns "Hello " added to the start of the string s
# Unless s starts with the word Hello (remember string slicing?)
def add_hello(s):
  return ""
  
print(add_hello("Bob"))         # Hello Bob
print(add_hello("Carol"))       # Hello Carol
print(add_hello("Hello Alex"))  # Hello Alex

print()

# Challenge Problems (not required)
# Fill out the following functions if you're up for an extra challenge!
# Be sure to uncomment tests to try them out

# Write a function exactly_one that takes in three Boolean inputs
# Returns True if exactly one of the three inputs is True, and False otherwise
# You might find this a bit easier if you use a previous function you wrote!

#print(exactly_one(True, True, False))   # False
#print(exactly_one(False, True, False))  # True
#print(exactly_one(True, True, True))    # False
#print(exactly_one(False, False, False)) # False
#print(exactly_one(False, False, True))  # True

# Write a function my_round that rounds a decimal to the nearest integer
# Don't use the built-in function `round` which does exactly this (but you can use it to test!)
# As a tip, int rounds _down_, which is helpful for implementing this function

#print(my_round(1.3))   # 1
#print(my_round(2.73))  # 3
#print(my_round(7.5))   # 8