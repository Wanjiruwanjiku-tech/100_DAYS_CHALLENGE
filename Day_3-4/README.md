# FUNCTIONS
## I love recycling.
-------------------------------------

## Table of Contents.
- [Introduction](#introduction)
- [Components](#components-of-a-function)
- [Lambda](#lambda)

## Introduction
- Functions are blocks of reusable code designed to perform a single action.

- They help in organizing code, making it more readable and allowing reuse and modularity.

### Characteristics

1. __Encapsulation__ - Functions encapsulate a piece of functionality, making code cleaner and more manageable.

2. __Reusability__ - Once defined, functions can be reused/called multiple times in a program or across different programs.

3. __Abstraction__ - Help in Abstracting complex operations, allowing a programmer to use the function without knowing the inner workings of the function.

4. __Modularity__ - Functions help in breaking down large programs into smaller manageble parts (__modules__).

### Components of a Function

1. __Function Name__ - A uniqe name that identifies the function.

2. __Parameters/Arguments__ - Functions passed to a function when it is called.

3. __Function Body__ - Block of code that defines the function's functionality. It starts witha colon and it is indented.

4. __Return Statement__ - usualy optional, Used to return a value.


Example
--------------
             _ _________(__function name__)
            |       |----------------(__Parameter__)
        def greet(name):
            print(f'Hello, {name}') --------(__function body__)
        greet('Nat')
---------------------------------------


## Defining

- In python functions are defined using the __`def` keyword__, followed by the __function name__, then __parenthesis `()`__ and then a __colon `:`__.

```
def greet(name):
    print(f"Hello, {name}!")
 ```

 ## Calling

 - To call a function, you simply use the functions name followed by parenthesis and the required Args/parameters.

```
greet("Alice") __Output will be Hello, Alice
``` 

## Returning
```
def add(a, b):
    return a + b

result = add(5, 3)
print(result)
```

- For variable number or arguments
```
def add(*args):
    return sum(args)
print (add(1, 2, 3, 4))  # output = 10
```

## Lambda Functions

- Also called __anonymous functions__. They are small, one line functions defined using the __lambda__ keyword.

- Used for short term purposes where defining a full def function is uneccessary.

- Defined using the __lambda keyword, followed by a list of args, a colon and an expression__.

```
lambda arguments: expression
```

### Example

```
add = lambda x, y: x + Y
result = add(3, 5)
print(result)  # output = 8
```

### Characteristics

1. __Anonymous__ - They are namelss unless assigned to a variable.

2. __Single Expression__ - Consist of a single expression whose result is returned.

2. __Inline Definition__ - They are defined inline.


### Use Cases

- Used in Higher-order functions such as those that take other functions as args or return them as results.

1. Sorting

```
# Sorting a list of tuples by the second element
pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)  # Output: [(1, 'one'), (3, 'three'), (2, 'two')]
```

2. Filtering

```
# Filtering even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]
```

3. Mapping

```
# Squaring numbers in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
```