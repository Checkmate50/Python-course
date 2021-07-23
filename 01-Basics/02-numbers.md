## Introduction

There are two main kinds of numbers in Python: integers and decimals.  Integers are whole numbers, such as 1, 6, -5, and 0.  Decimals, also called floating points, are parts of whole numbers, such as 0.5, 1.42, -3.9, and -0.01.  

Decimals in Python are sometimes represented in [scientific notation](https://en.wikipedia.org/wiki/Scientific_notation), where `e` represents `10^`.  For example, `3.42e3=3.42*10^3=3,420`.  This is not a detail you need to remember, but it shows up sometimes and I like having a reference somewhere to all the weird Python behaviors that might show up.

Numbers of all kinds can be printed in Python.  The following code prints what you would expect:

```
print(4)
print(-42)
print(3.68)
print(-0.01)
```

## Numeric Operations

Python supports a wide variety of standard numeric operations, some of which we've already seen.  Some basic operations Python supports include `+` (addition), `-` (negation and subtraction), `*` (multiplication), and `/` (division).  Consider the following code:

```
print(2 + 3) # Prints 5
print(4 - 1) # Prints 3
print(3 * 6) # Prints 18
print(4 / 2) # Prints 2.0
```

Python also supports a special syntax for exponents: `**`.  This is the same as calling the `pow` function that we saw earlier:

```
print(2 ** 3)     # Prints 8
print(pow(2, 3))  # Prints 8
```

Finally, Python supports a few "special" operations: `%` (modulus) and `//` (integer division) are the main two we will discuss.  `%` calculates the remainder of division between two numbers (this even works with decimals!), and `//` calculates division but rounds down to the nearest lower integer.  Here are some examples of these operations in action:

```
print(7 % 5)    # Prints 2
print(5.5 % 3)  # Prints 2.5
print(6 // 3)   # Prints 2
print(4 // 3)   # Prints 1
```

### Floating Point Error

Remember how decimals are sometimes called floating points?  This has very good reason in computer science, but can be confusing when you don't know what it means.  Basically, decimals in Python aren't exact, so sometimes operations have something called "floating point error", where they produce numbers that are slightly off what you would expect.

For example, consider `.1 + .2`.  This operation should clearly be `.3`.  Python, however, gets it "wrong"!

```
print(.1 + .2) # Prints 0.30000000000000004
```

No, your computer isn't broken, this is actually what it calculates!  The reasons for this are too complicated to get into here, but just remember that computers often give decimals that are slightly off the real answer.

## Examples

Let's look at some examples of functions we can defined with these fancy new number operations!

```
def double(x):
  return 2 * x
  
print(double(5))          # Prints 10

def sum(a, b, c, d):
  return a + b + c + d
  
print(sum(1, 2, 3, 4))    # Prints 10

def sub_squares(a, b):
  return a**2 - b**2
  
print(sub_squares(4, 2))  # Prints 12

# sqrt is short for square root
def sqrt(x):
  # Remember that x ^ (1/2) = sqrt!
  return x ** .5
  
print(sqrt(4))            # Prints 2

# Calculates the longest edge of a triangle
def longest_edge(x, y):
  return sqrt(x**2+y**2)
  
print(longest_edge(3, 4)) # Prints 5
```

Now it's time to try your hand at writing your own operations and functions!  What can you come up with?

## Bonus Topic (Challenging)

This is a bit more complicated, but if you're feeling up for some really challenging number theory, read on!  I won't refer to this content again throughout the course, so this is by no means required.  If you're really interested in how computers work, though, this is the section for you!

Specifically, I want to talk about how numbers are actually represented in a computer.  See, a computer stores everything in _binary_: 1s and 0s.  Using only 1s and 0s, though, how does the computer represent something like the number 5?  The answer is with binary representation!

`print(0b101) # Prints 5: 0b means "binary" in Python`

See, each 1 and 0 in binary means the same thing as a tens place with regular numbers, but multiplied by a power of 2.  For example, the decimal 27 can be read as `2*10^1 + 7*10^0=2*10+7*1=27`.  Similarly, the binary number `101` can be read as `1*2^2+0*2^1+1*2^0=1*4+0*2+1*1=4+0+1=5`.

Why does this matter for us though?  This is just how the computer thinks, is there any reason we should care?  The answer is _yes_!  Not only is this interesting, but it allows us to define the following powerful operations: `&` (bitwise AND), `|` (bitwise OR), and `^` (bitwise XOR).  These operations have the following properties:

```
print(0b1 & 0b0)    # Prints 0, since 1 and 0 is 0
print(0b10 & 0b10)  # Prints 2, since 1 and 1 is 1
print(0b10 | 0b01)  # Prints 3, since 1 or 0 is 1
print(0b00 | 0b10)  # Prints 2, since 0 or 0 is 0
```

See if you can figure out what `^` does without me telling you!  I'll give you a clue: XOR stands for "exclusive or", which means _either_ a OR b, as opposed to "inclusive or".

If this was interesting and you want to read more, check out [this article](https://www.stat.berkeley.edu/~nolan/stat133/Spr04/chapters/representations.pdf) on representations.  It also gets into a fancy trick called "Two's Complement", which is a bit tricky to get into here, but allows you to represent negative numbers as well.  

Finally, computers also use binary to represent floating point numbers, like `1.5`.  Unfortunately, this representation is _very_ complicated, and way outside the scope of this course.  Check out [this article](https://en.wikipedia.org/wiki/IEEE_754) for the basics, but be warned that it gets complicated fast.

Let me know if you have any questions about computer representations: I love this stuff and can talk about it all day.  Thanks for reading this section, it was pretty intense, but I hope you learned something!  Take a break now, and then we can move onto the next assignment and topic!