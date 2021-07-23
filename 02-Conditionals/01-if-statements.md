## Introduction

So far, all of our code has been very sequential: we just do one thing after another.  For more complicated behavior and advanced functions, however, we need some way for the code to make decisions.  In other words, it is really important for the code to be able to have different behaviors or outputs depending on values in the program.

In Python, we can do this with an _if statement_.  An `if` statement takes in a _condition_: if the condition is true, then the following code is executed, otherwise it is not.

## Conditions

We will go over more conditions in the next topic, but for now we introduce number equality, less than, and greater than.

### Equality

We can see if two numbers are equal with `==`.  The reason we use `==` (two equal signs) for checking equality is that a single equal `=` denotes an _assignment_.  Be sure to remember the difference as this is a common thing to mixup for beginning programmers.  This also gives us a chance to see an `if` statement in action:

```
x = 5
# Note that the condition should stylistically go inside parantheses (though it doesn't have to!)
if (x == 5): # <-- remember the colon and indent!  Just like when defining functions
  print("x == 5")  # This will print since the comparison is True
if (x == 4):
  print("x == 4")  # This won't print since the comparison is False
```

### Less Than and Greater Than

We can also compare numbers with the math operators `<` (less than), `>` (greater than), `<=` (less than or equal to) and `>=` (greater than or equal to).  For example:

```
x = 6
if (x < 7):
  print("x < 7")  # This will print
if (x > 8):
  print("x > 8")  # This won't print
if (x <= 6):
  print("x <= 6") # This will print
if (x >= 3):
  print("x >= 3") # This will print
```

## Examples

Let's see some examples of the cool new functions we can write with `if` statements!

```
# Prints 0 only if the input is 0
def print_if_zero(x):
  # We can put if statements inside functions!  Just remember the indent
  if (x == 0):
    print(0)
  #^-- Note the two "indents"!  We need an indent after each colon `:`
  
print_if_zero(0) # Prints 0
print_if_zero(5) # Doesn't print anything
```

```
# Returns the sign of x (1, 0, or -1)
def sign(x):
  if (x > 0):
    return 1
  # Note that at the end of an if statement, we lose an indent, 
  #  just like with a function block
  if (x == 0):
    return 0
  # Experienced programmers know this last "if" statement is unnecesssary!
  # We'll cover why later
  if (x < 0):  
    return -1
    
print(sign(50)) # Prints 1
print(sign(0))  # Prints 0
print(sign(-3)) # Prints -1

# Returns the maximum of the numbers x and y
# (This is actually built-in to Python normally! We'll cover it later)
def max(x, y):
  z = x - y
  if (z >= 0):
    return x
  # We can use other functions in conditions
  if (sign(z) == -1):
    return y
    
print(max(4, 6))  # Prints 6
print(max(7, 3))  # Prints 7
```