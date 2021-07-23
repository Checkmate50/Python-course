## Introduction

Remember how conditions require that the result be True or False?  True and false values have a special name in programming, called Boolean values.  Boolean values can _only_ be true or false, and can't take on any other form.

The words True and False are actually keywords in Python, and can be used in if statements directly (to have a very silly if statement):

```
if (True):
  print (True) # Prints True
if (False):
  print (False) # Doesn't print
```

## Boolean connectives

Booleans have operations, just like numbers!  In Python, these operations take the form of keywords that connect Booleans together.  The three words to learn are `not`, `and`, and `or`.

The word `not` means the opposite boolean of the given value: so `not True` is `False` and vice-versa.  The word `and` "connects" two booleans, and only returns `True` if _both_ Booleans are true.  In contrast, `Or` returns `True` if _either_ of the two booleans are `True`.  Let's see a few examples:

```
print(not False)            # True
print(False and True)       # False
print(True or False)        # True
print(True and True)        # True
print(not (False or False)) # True
```

## Extra comparisons

So far, we've learned about number comparisons with `==`, `<`, and the like.  Now we know that these operations actually return a Boolean!  

```
print(1 < 2)                  # True
print(not (3 > 4))            # True
print((1 == 1) and (1 == 2))  # False
```

There are also a few more comparison behaviors you should know about.

One is the `!=` operator, which was mentioned in the first assignment.  This returns True if the two compared values are _not_ equal to each other.  Why did I say "values" there and not "numbers"?  It turns out you can use comparison operators to compare Strings as well as numbers!  Strings are _ordered_ alphabetically, so "a"<"b", "hello">"goodbye", and "hi"=="hi".

```
print(1 != 2)           # True
print("a" != "a")       # False
print("abc" > "baa")    # False
print("H" == "h")       # False -- be careful, capital letters are weird!
print("H" < "a")        # True -- what happened?  It turns out capital letters always come before lower-case letters
```

## Converting to Booleans

You can convert a value to a Boolean using the `bool` function (much like the `int` or `str` functions).  This will happen automatically if you put a non-Boolean in an `if` statement, which is quite powerful.  Note that any non-0 number is `True` while any non-empty string is also `True` (including the string `False`, confusingly).

```
print(bool(1))        # True
print(bool(""))       # False
print(bool("False"))  # True
if (0):
  print("Hello")      # Doesn't print
if ("Hello"):
  print("Howdy")      # Howdy
```

Now let's use these new boolean rules to write some functions!