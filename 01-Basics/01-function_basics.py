# Remember, this is a comment, it doesn't do anything!
# The first thing you should do is run this program, it should print a bunch of garbage

# Part 1: Calling functions
# Update the following function calls to get them to print what's in the comments:

print("Part 1:")  #spacing, ignore

print("")               # Hello World!
print("wrong")          # right
print(0)                # 2
print(abs(0))           # 5
print(abs(3))           # -3 -- you can think outside the box for this one
print(pow(1, 2))        # 4 -- try to use the pow function!
print(pow(0, 0))        # -9 -- try to use the pow function!

# Part 2: Writing your own functions:
# Fill in the function definitions so they do what they say in the comments
# I've provided some tests along with comments about what they should produce

print("\nPart 2:") #spacing, ignore

# Prints the negative of a number
def print_neg_abs(x):
    print()

print("print_neg_abs:") # spacing, ignore   
print_neg_abs(-5)   # Should print -5
print_neg_abs(3)    # Should print -3

# Returns the value of x squared (to the power of 2)
def square(x):
    return 0
    
print("\nsquare:") # spacing, ignore  
print(square(4))    # Should print 16
print(square(-2))   # Should print 4

# Returns the absolute value of x to the y

def abs_pow(x, y):
    return 0
    
print("\nabs_pow:") # spacing, ignore  
print(abs_pow(2, 4))    # Should print 16
print(abs_pow(-3, 3))   # Should print 27

# Bonus question!  Uncomment (remove the '#' before) the print statements below to try it:

# Write a function (from scratch!) that computes and returns the following:
# x^|y^z|, where ^ is the power function, and |x| is the absolute value of x
# Call it pow_abs_pow

# print("\nBonus Question:")
# print(pow_abs_pow(1, 2, 1))  # Should print 1
# print(pow_abs_pow(-2, 2, 2)) # Should print 16
# print(pow_abs_pow(3, -2, 2)) # Should print 81