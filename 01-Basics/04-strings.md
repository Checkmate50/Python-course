## Introduction

We've been using things called "Strings" for a while, stuff like `"Hello World"` and `"Hey there"` -- things wrapped inside of double-quotation marks.  Now it's finally time to learn a bit about what they are and how we can modify them in code.

A string is a series of "characters", which are symbols you can type on your keyboard.  "a", "q", "1", "/", and "&" are all examples of characters, since I wrapped them in double-quotes.  These are also strings, along with things like "hello", "good/bye", and "12345".

## String Operations

The reason strings are important is that Python can do operations on them!  Things like "string concatenation", "repetition", "length", and "string slices".  We'll go through each of these in detail and see how you can use them to make cool functions!

### Concatenation

Strings can be "concatenated" together, where you essentially "smash" two strings together.  For example if I had the strings "Hello " and "World", I can put them together using the `+` operation:

```python
x = "Hello "
y = "World"
print(x + y) # Prints Hello World
```

### Repetition

Python has a cool feature, where you can multiply a string by a number to duplicate that string.  For example:

```python
x = "good"
print(x * 3) # prints goodgoodgood
```

### Length

A useful Python function is the function `len`, which returns the length (or number of characters) of a string:

```python
x = "string"
print(len(x)) # prints 6 (the number of characters in "string")
```

### Slicing

Finally, you can get subsets of a complete string.  This last topic is a bit complicated, and we'll return to it when we cover lists, but basically you can access "parts" of a string with slicing syntax `[]`.  Here's some examples of how it works:

```python
x = "Hello"
print(x[0]) # Prints H
print(x[4]) # Prints o
```

Note that strings in Python are _zero-indexed_, meaning that the first character in a string can be gotten with the number `0`, while the fifth character can be gotten with the number `4`.

String slicing also has a cool property, where you can get entire _parts_ of the string.  For example, if we want the first 3 characters of a string, we could use the slice `[0:3]`.  Alternatively, if we want the 2nd through 5th characters, we might use `[2:6]` (note that the second number is non-inclusive).

Here's some examples of string slicing in action:

```python
x = "Hello"
y = "Goodbye"
print(x[0:2]) # Prints He
print(x[1:3]) # Prints el
print(y[4:7]) # Prints bye
```

## Examples

Let's use our knowledge of string operations to write some cool functions!

Example 1: 

```python
# This function adds "Hello " to the start of any string
def hello_add(x):
  return "Hello " + x
  
print(hello_add("Bob"))    # Prints "Hello Bob"
print(hello_add("Cathy"))  # Prints "Hello Cathy"
```

Example 2:

```python
# This function adds a dash to the middle of a word:
def add_dash(s):
  return s[0:(len(s) // 2)] + "-" + s[(len(s) // 2):len(s)]
  
print(add_dash("heya"))   # Prints "he-ya"
print(add_dash("Hello"))  # Prints "He-llo"
```

Example 3:

```python
# This function adds the first two characters of the first word
#  to the last two characters of the second word
def combine(s1, s2):
  return s1[0:2] + s2[len(s2)-2:len(s2)]
  
print(combine("Hello", "Goodbye")) # Prints Heye
```
