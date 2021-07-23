# The first thing you should do is run this program, it should print a bunch of garbage

# Part 1: Variable Assignment
# Update the variables below so that the print statements do what they should do
# Don't modify the print statements!!

print("Part 1:")

x = 0
y = 0
z = 0
s = ""

# Don't modify any of the following print statements!!
print(x)        # Should print 5
print(x + y)    # Should print 12
print(x - y)    # Should print -2
print(z * 2)    # Should print 12.2
print(s)        # Should print Hey there!
print()         # Spacing, ignore

# Part 2: Input
# Update the following functions as described
# I've included partial tests, but you will have to test them yourself with your own inputs!

print("Part 2:")

# Note that this function has no arguments!  This is completely legal
# This function should print whatever the user types in
# If the user types Howdy, this function should print Howdy
# If the user types 5, this function should print 5
def echo():
  print()
  
echo()  # Once you update the function, this should ask for input
print() # spacing, ignore

# This function takes in a user input, and returns the input minus the argument
# For example if the user inputs 3 to sub_x(2), the result would be 1

def sub_x(x):
  return 0
  
print(sub_x(5))  # Prints input-5
print(sub_x(-2)) # Prints input+2