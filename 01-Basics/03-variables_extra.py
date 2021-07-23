# This is an extra assignment to give more practice with variables and writing functions
# Doing this work is by no means required, but it might be helpful :)
# The first thing you should do is run this program, it should print a bunch of garbage

# Part 1: Basic Functions
# Write the body of the following functions

print("Part 1:")

# Returns x squared (x^2)
def square(x):
  return 0
    
print(square(3))    # 9
print(square(-5))   # 25
print()

# Suppose z = x + y.  This function returns z * z + z
def mult_add(x, y):
  return 0
    
print(mult_add(2, 3))    # 42
print(mult_add(-1, 2))   # 2
print(mult_add(0, 3))    # 12
print()

# Returns x % n (the remainder of x / n) BUT you can't use '%'
# Hint, the solution involves '//'
# (This problem is a bit tricky!)
def mod(x, y):
  return 0
    
print(mod(5, 2))   # 1.0
print(mod(5, 3))   # 2.0
print(mod(7, 3))   # 1.0000000000000004 is the answer I got (floating point error)
print()

# Part 2: Writing your own functions
# Write each of the following functions from scratch
# Uncomment (remove the '#' preceding) the tests once you've written the function to try it out!

print("Part 2:")

# Write a funcion called sub_five that subtracts 5 from a number

# print(sub_five(7)) # 2
# print(sub_five(3)) # -2
# print()

# Write a function called average that finds the average of 4 numbers
# Recall that the average is (x_1+x_2+...+x_n/n)

# print(average(1, 2, 3, 4)) # 2.5
# print(average(5, 5, 5, 5)) # 5
# print()

# Finally, write a function called mod_difference
# This calculates the difference between two numbers mod the second number
# (Is this ever different than just the mod?)

# print(mod_difference(7, 3))      # 1
# print(mod_difference(8, 4))      # 0
# print()