# The first thing you should do is run this program, it should print a bunch of garbage

# Part 1: Reading Functions
# Given the following function definitions
# Make calls to these functions that print the expected thing!

# Don't modify these functions!
# Removes the last character of the string
def trim_end(s):
  return s[0:len(s)-1]
  
# Puts the first half of the first string with the second half of the second string
def combine(s1, s2):
  return s1[0:len(s1)//2] + s2[len(s2)//2:len(s2)]
  
# Does something (what does this function do?)
def dup(s):
  return s[0:len(s)//3] * 3
  
print("Part 1:")

# Do modify these print statements
  
print(trim_end("a"))                       # Should print Hello World
print(combine("Hello World", ""))         # Should print Hello World
print(trim_end(combine("ab", "ab")))      # Should print ab
print(dup("abcdef"))                      # Should print aaa

# Part 2: Writing Functions
# Fill out the following functions (I've provided test cases)

print("Part 2:")

# Concatenates x to y
def concat(x, y):
  return ""
  
print(concat("Hello ", "World"))  # Should print Hello World
print(concat("abc", "def"))       # Should print abcdef
print()

# Returns the first 3 characters of a string
def first_three(s):
  return ""
  
print(first_three("Howdy"))       # Should print How
print(first_three("There"))       # Should print The
print()

# Requires a string of 3 characters
# Returns that string reversed
def reverse_three(s):
  return ""
  
print(reverse_three("abc"))       # Should print cba
print(reverse_three("yaY"))       # Should print Yay
print()

# Bonus Question!

# Write a function called 'long_dup' that takes in an integer 'n' and a string 's'
#  Using these, it should return the first 'n' characters of 's' 'n' times!

#print("Bonus Question:")
# print(long_dup(3, "abcd"))  # Should print abcabcabc
# print(long_dup(2, "Hello")) # Should print HeHe