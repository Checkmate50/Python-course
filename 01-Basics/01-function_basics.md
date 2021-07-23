## Introduction

This is a fairly long lecture, so don't get intimidated!  Most after this will be shorter, there's just a lot I need to explain to get started.

The most fundamental thing in programming and particularly Python is the _function_.  You might remember the idea of a function from math: it's a thing that takes an input and produces an output.

Functions work the same way in Python.  They take in an input (or multiple inputs), and produce some kind of output.

### A Function

Remember the very first Python program we wrote?  It's just the text `print("Hello World!")`, which makes the computer print the words "Hello World!".  The word `print` is actually a function!

Specifically, we _call_ `print` with the _argument_ `"Hello World!"`, which tells the computer to print that thing!  You can provide lots of arguments to print: writing `print("Howdy")` prints the word `Howdy`, while writing `print(42)` prints the number 42 (try it yourself!).  We can even chain prints together.  For example, try copy-pasting the following code into your IDLE terminal and running it:

```
# Anything with a '#' in front is a comment: it doesn't do anything
print("Hello")
print("I am a program")
print("That prints the number")
print(42)
```

There are lots of functions in Python!  Unlike the `print` function, however, most functions output things _inside_ the Python program.  For example, the `abs` function (which stands for absolute value) takes in negative numbers and makes them positive.  The following program should print the numbers `1 2 3`:

```
print(1)
# Call a function with the output of another function!
print(abs(2))
# What about the absolute value of a negative number?
print(abs(-3))
```

Note that in this program, we printed the _output_ of the `abs` function: in other words, the _input_ to the `print` function was the _output_ of the `abs` function.  Note also that `abs` takes in one input argument, a single number, such as `-3`.

## Multiple Arguments

Functions can also take in multiple arguments!  Note, though, that they _always_ produce a single output (which, as in the case of print, might be nothing).  Consider the `pow` function (which stands for `power`), which takes in two arguments `x` and `y`.  This function is the same as taking `x` to the power `y`.  For example, the following calls to print produce the numbers `1`, `8`, and `9`:

```
# Two arguments now!  But _only_ to pow, print still has one argument
print(pow(1, 1))
print(pow(2, 3))
print(pow(3, 2))
```

Try playing around with the `pow`, `abs`, and `print` functions to see what you can do!  What happens if you give a function too many arguments (such as giving the `print` function 2 arguments)?  What if you call `print` on another `print` function?  Can you give a function as an argument to `pow`?

## Making our own functions

We'll cover this in more detail later, but I want to introduce the idea of defining our _own_ functions!  Right now, all we can do is use functions that Python has already made, but what if we wanted to make our own?

Let's start with something simple: making a function that takes in a single number and prints the absolute value of that number.  The code for this would look like the following:

```
# The function "header"
def print_abs(input):
  # 'input' is the only argument to this function
  print(abs(input))
#^-- Note the tab here (or two spaces): this is important!!
```

Every function we define starts with the word `def` (meaning define), followed by a _function name_ (which can be anything), followed by the arguments to the function (in this case, `input` is our only argument).  Our function here doesn't produce any output to the program, but it does print any number we give it.  We can now call our function!

```
def print_abs(input):
  print(abs(input))

# Note that we lose the tab when 
#  we "leave" the function definition
print_abs(-3) # Will print "3"
```

### Function Outputs

Now let's try making a function that _returns_ a value.  Let's make the function `negative_abs`, which always returns a negative number:

```
# We can call our "arguments" whatever we want
# Here we call it x
def negative_abs(x)
  # -x gives negative x (go figure!)
  return -abs(x)
```

Here, the `return` keyword says that we want the following "thing" to be the output of the function.  In this case, the output of our function is the negative of `abs(x)`, where `x` is our input!  Consider the following:

```
def negative_abs(x)
  return -abs(x)

# Note that we lose the "whitespace" when
#  when leaving the function again
print(negative_abs(-3)) # prints -3
print(negative_abs(42)) # prints -42
```

### Multiple Arguments

Just like when calling functions, we can have make our own with multiple arguments:

```
def print_pow(x, y):
  print(pow(x, y))
  
print_pow(2, 3)  # Prints 8
print_pow(-3, 2) # Prints -9
```

You made it through the longest lecture of the course (I hope)!  Take a break, do some stretches, and then let's try out the first assignment: making your own functions!