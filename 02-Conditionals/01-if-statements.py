# The first thing you should do is run this program, it should print a bunch of garbage

# Part 1: Basic Conditions
# Fill in the following functions as defined by the comments:

print("Part 1:")

# Prints "negative" if x is negative
def print_if_negative(x):
  print()

print_if_negative(5)  # Does nothing
print_if_negative(-7) # negative
print()

# Returns the minimum of two numbers
def min(x, y):
  return 0
  
print(min(3, 6)) # 3
print(min(5, 4)) # 4
print(min(1, 1)) # 1
print()

# Returns absolute value (without using the builtin 'abs' function!)
def my_abs(x):
  return 0
  
print(my_abs(-3)) # 3
print(my_abs(6))  # 6
print()

# Part 2: Nested Conditions
# You can nest conditions to do more complicated comparisons!
# Just remember to have a colon and indent after each comparison

print("Part 2:")

# Returns "both zero" if both x and y are zero
# Otherwise returns "non-zero"
# Hint: x != y is True when x does not equal y
def are_zero(x, y):
  return ""
  
print(are_zero(0, 0)) # both zero
print(are_zero(1, 0)) # non-zero
print(are_zero(0, 5)) # non-zero
print(are_zero(1, 6)) # non-zero
print()

# Returns 1 if x, y, and z are in ascending numerical order
# Otherwise returns 0
def ordered(x, y, z):
  return 0
  
print(ordered(1, 2, 3)) # 1
print(ordered(2, 1, 2)) # 0
print(ordered(2, 2, 1)) # 0
print(ordered(3, 3, 3)) # 1
print()

# Returns 1 if all arguments are in ascending numerical order
# Can you use a previous function to make this easier?
def long_ordered(a, b, c, d, e):
  return 0
  
print(long_ordered(1, 2, 3, 3, 4)) # 1
print(long_ordered(3, 2, 3, 3, 4)) # 0
print(long_ordered(1, 2, 4, 4, 3)) # 0
print(long_ordered(5, 0, 1, 2, 3)) # 0
print()

# Challenge problems!  
# Uncomment the tests to try these out

# print("Challenge Problems:")

# Write a function called perfect_square
# Returns 1 if x is a perfect square 
# (i.e. if squareroot(x) is an integer)
# Otherwise returns 0
# Tip: you can use the int() function to round down to the nearest integer

# print(perfect_square(5)) # 0
# print(perfect_square(9)) # 1
# print(perfect_square(0)) # 1

# Write a function called bounded
# Given three arguments x, y, z
# Returns 1 if x is between y and z (inclusive)
# Otherwise returns 0
# Note that y may be less than z or vice-versa

# print(bounded(1, 1, 1)) # 1
# print(bounded(5, 6, 4)) # 1
# print(bounded(3, 2, 2)) # 0
# print(bounded(0, 2, 1)) # 0
# print(bounded(1, 0, 2)) # 1

# Write a function called multi_bounded
# Given x, y, z, l, u
# Returns true if x, y, and z are all bounded by l and u
# Can you use a previous function to help?

# print(multi_bounded(1, 2, 3, 0, 5)) # 1
# print(multi_bounded(3, 3, 1, 2, 4)) # 0
# print(multi_bounded(1, 4, 2, 1, 3)) # 0
# print(multi_bounded(2, 3, 4, 4, 2)) # 1