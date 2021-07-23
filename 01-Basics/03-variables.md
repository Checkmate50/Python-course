## Introduction

So far, every function we've made has a single line: just return something that might depend as an input to that function.  However, it can often be useful to store and reuse intermediate steps along a computation.  Consider the following function that adds two numbers together, then multiplies the result by itself:

```
def add_mult(a, b):
  return (a + b) * (a + b)
```

In this function, we call `a` and `b` arguments to the function, but they are also _variables_: things that can store values.  

### Defining Variables

We can define our own variable inside the function to make this computation easier (and faster!):

```
def add_mult(a, b):
  x = a + b    # Makes a new variable x, with value equal to a + b
  return x * x # Note that this is the same result as above!
```

You can set variables to whatever you want, and you can even assign them outside of functions!

```
x = 5
y = 7.2
print(x + y)  # Prints 12.2 

def big_sum(a):
  b = a + a
  return b + b + b

# Remember, x = 5
print(big_sum(x)) # Prints 30
```

### Reassigning Variables

Whenever you assign to a variable, you overwrite whatever value it might have previously had.  This is called _variable reassignment_.  For example, consider the following code:

```
x = 5
print(x) # Prints 5
x = 7
print(x) # Prints 7
```

Python programs always execute one line at a time, so be careful about the order you do things in!  Try to avoid reassigning variables when possible, since it can make things confusing.

## Input

The thing we'll be using variables most for at the beginning is saving _input_ from the user.  So far, all of our programs have just run, they haven't been able to interact with the user at all.  By using the `input` function, we ask the user to input a value, which can then be saved:

```
print("Please type a phrase:")
x = input()
print(x) # Prints out whatever the user just typed
```

### Making input a number

When given to us, our input is something called a "String", which we will talk about in a later lecture.  A lot of the time, though, we actually want to input a number.  Suppose we want to make a simple program that adds two numbers given to us together; we need to use the `int` function to convert the input to an Integer:

```
# A simple addition program
print("Please give a number:")
x = int(input())
print("Please give another number:")
y = int(input())
print("x + y = ")
print(x + y) # Prints the result of adding the numbers together!
```

So just remember, if you want a number as input, make sure to wrap `input` in a call to `int`!

There's more to talk about variables, particularly something called _scope_, but that's a discussion for a later time.  We'll discuss it when we talk about advanced functions.  For now, you can name variables whatever you want, and assign whatever you want to them.  Just be careful you don't reassign a variable by accident!