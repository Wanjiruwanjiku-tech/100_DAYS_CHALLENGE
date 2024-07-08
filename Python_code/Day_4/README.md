# String Manipulation and Formatting
## Have fun with words.

# Table of Contents

- [Introduction](introduction)
- [Basic Operations](basic-operations)
- [Common Methods](common-methods)
- [String Formatting](string-formatting)
- [Advanced String Manipulation](advanced-string-manipulation)
-----------------------------------------

# DAY FOUR OF ONE HUNDRED CODING IN PYTHON

## Introduction

- Strings are one of the most commonly used data types in Pyhon. Strings are essential for representing and working with text.

### What is a Sring?

- A string is a __sequence of characters enclosed within single,double or triple quotes `''`, `""`,`(`'''`, `"""`)`.__

- Strings are Immutable meaning once a string is created, its contents cannot be changed.

- Examples

```
single_quote = 'Hello'
double_quote = "World"
triple_quote = '''
                    Hello World
                '''
```

## Basic Operations

- Python supports basic operations for manipulating strings.

1. __Concatenation__ - Joining two or more strings using the __+__ operator.

2. __Repetition__ - Repeating a sring using the __*__ operator.

3. __Indexing and Slicing__ - Accessing individual characters or substrings using indices.

4. __Length__ - Determining the number of characters in a string using the __len()__ function.


### Concatenation
```
string1 = 'Hello'
string2 = 'World'
full_string = string1 + " " + string2
print(full_string)  # output = Hello World
```

### Repetition
```
word = 'Go'
word2 = 'Shawty its your Birthday'

lyric = word * 5
print(lyric + " " + word2) # output = Go Go Go Go Go Shawty its your Birthday
```

### Indexing and Slicing
```
word = "Superman"
print(word[0]) # output = S
print(word[-4]) # output = r
print(word[1:4]) # output = upe
print(word[5]) # output = m
print(word[2:6]) # output = pe
```

### Length
```
word = 'Hello'
result = len(word)
print(result) # Output = 5
```

## Common Methods

- __lower()__ - Convert string to lowecase
- __upper()__ - Convert string to uppercase
- __strip()__ - Remove leading and trailing whitespece
- __split()__ - Split the string into a list of substring based on a delimiter
- __join()__ - Join a list of strings into a single string with a specified seperator
- __replace()__- Relpace all occurrences of a substring with another substring
- __find() and index()__ - Find the position of a substring within a string

### lower() and upper() methods
```
str1 = "Hello World"
print(str1.lower())  # Output: hello world
print(str1.upper())  # Output: HELLO WORLD

```

### strip() Method
```
str1 = "  Hello World  "
print(str1.strip())  # Output: Hello World

```

### split() Method
```
str1 = "Hello World"
print(str1.split())  # Output: ['Hello', 'World']

```

### join() Method
```
list1 = ["Hello", "World"]
print(" ".join(list1))  # Output: Hello World

```

### replace() Method
```
str1 = "Hello World"
print(str1.replace("World", "Python"))  # Output: Hello Python

```

### find() and index() Method
```
str1 = "Hello World"
print(str1.find("World"))  # Output: 6
print(str1.index("World"))  # Output: 6

```


## String Formatting
- Essential for creating __dynamic text__ based on variable content.

- Python has several ways of formatting strings.

1. __Old Style__ - `% operator`

2. __f-string__ - `f"words are {variable_name}"`

3. __str.format__ - `"Words are {}".format(variable_name)`


### Old style
```
name = 'Alice'
age = 30
print("Hello, %s. Are you %d years old?"% (name, age))

```

### f-string
```
name = 'Alice'
age = 30

print(f'Hi, my name is {name} and i am {age} years old.')

```