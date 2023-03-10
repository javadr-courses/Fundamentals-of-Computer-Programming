## Table of contents

- [14010801](14010801.ipynb):
  - Basic usage of built-in functions (such as `print`, `help`, `input`, `len`)
  - `map(int, input().split())` syntax to get multiple input from one line
  - Types of Error: **Syntax error**, **Runtime error** and **Logical error**
  - single-quotation mark and double-quotation mark -- as a way to show strings in python

- [14010807](14010807.ipynb):
  - `type` function as well as differences between `float`, `int`, `NoneType`, etc.
  - `bin`, `oct`, `hex`, etc.
  - `int() base must be >= 2 and <= 36, or 0`
  - `math` package (`import math`) -- `math.sin`, `math.pi`, `math.e`, `math.tan`, etc.
  - Function definition (how to define a function header, arguments and return value)
  - **fruitful function** versus **void function**
  - `from something import stuff` vs. `import stuff`

- [14010808](14010808.ipynb):
  - `min`, `max`, `abs` built-in functions
  - `turtle` package and `turtle.Turtle` class
  - **for loop**: `for something in range(number):` syntax (_basic for loop_)
  - Function example: `n_angle`, `square`, `polygon`, `circle`, `arc` and `rectangle` for turtle
  - Set speed of the turtle (using `bob.speed` method)
  - Python `docstring` feature (used for documentations)
  - function definitio: `area` which calculates the area using `math.pi`
  - `bob.shape` method (implemented on `turtle.Turtle` class)

- [14010814](14010814.ipynb):
  - Several math operators such as `//`.
  - Comparing float numbers using `==` operator is root of error in some cases
    - just check their distance, i.e. `abs(x-y)< 10**-20`
    - `0.1+0.1+0.1 == 0.3` returns `Flase`
  - Boolean values (`True`/`False`), are just integers (`True == 1`, `False == 0`)
  _ All numbers are booleans too (zero is `Flase` and all non-zero is `True`)
  - `if...else`
  - New keyword `pass`
  - Logical-boolean operators (`and`, `or`, `not`)
  - `RecursionError` (by calling `test` function inside of `test` function without any stop-condition)
  - `Recursion` (`Recursive function`)
  - `fact` function as an example of `Recursion` to calculate the factorial

- [14010815](14010815.ipynb):
  - Reminder for previous session: `fact` function (an example of recursive)
  - `int * str`: `0 * 'string'` results in an empty string with length of 0
  - Checking the depth of Recursion Stack: `test_stack_depth`
  - `map(function, sequence)`
    - `function` will be called on each elements of the `sequence`
    - its usage in getting several inputs in just one lines:
      - `map(int, input().split())`
      - `map(float, input().split())`
  - [**koch snowflake**](https://en.wikipedia.org/wiki/Koch_snowflake): drawing it with `turtle` module; another application of `recursion`

- [14010822](14010822.ipynb):
  - `typecasting` `float` to `int`; return just the integeral part of number:
    - `int(4.7)` --> `4`
    - `int(-4.7)` --> `-4`
  - Showing that if we convert a `float` value to `int` value, the number after floating-point will be dropped and the result number will become a normal integer.
  - Other `print` function arguments: `end` and `sep`
  - Calculating square root of 2
    - hypotenuse of an isosceles right-angled triangle with the side of 1
    - **Newton Raphson Method**
      - $x_{n+1} = x_n - \frac{f(x)}{f'(x)}$
  - `while` loop
  - `mod` operator (`%`).
  - **Factorial** function:
    - `for` loop
    - `while` loops.
  - **Fibonacci** numbers:
    - `non-recursive` method: `for` loop
    - `recursive` function
    - comparing running time of recursion and non-recursive version

- [14010828](14010828.ipynb):
  - string
    - slicing `[start[:end:[step]]]`
    - indexing `[index]` or `[-index]`
  - reversing a string:
    - `for` loop
    - slice: `[::-1]`
  - finding a character/substring in a string:
    - with the aid of loops
    - `in` operator
  - `str` methods:
    - `count`
    - `find`
    - `index`
    - `strip`, `lstrip`, `rstrip`
    - `replace`

- [14010905](14010905.ipynb):
  - **Algorithms, Flowcharts and Problem solving**.
  - `factorial` and `neper` functions and their running time
  - `format` strings:
    - practical usage in a function (`birthday`)
    - formatting float types; `f`, `g`
  - `is_complete` function and its running time
  - **Perfect numbers**
    - mathematical formula:
      - `2**(p-1) * (2**p-1)`, where p is a prime number
  - Body Mass Index (BMI):
    - A person's weight in kilograms (or pounds) divided by the square of height in meters (or feet)

- [14010906](14010906.ipynb):
  - Calculating `pi`:
    - $\frac{\pi}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \cdots$
  - Curse of `float` numbers:
    - `0.1+0.1+0.1` is not equal to  `0.3`
  - Reduction of an n-digit integer to a one-digit integer:
    - Defining `sum_digit` function: sum up all digits of an integer (e.g. `134 --> 1+3+4=8`).
    - Defining `one_digitizer` function; calls `sum_digit` until the result number has only 1 digit (=greater than 9)
    - A more efficient algorithm in comparison to above:
    >  while n >= 10: n = (n % 10) + (n // 10)
  - Reversing an integer with the aid of mathematical operation(e.g. `159 --> 951`).



- [14010912](14010912.ipynb):
  - Case Studies: Word Play and Lists
  - Files:
    - How to open a file with `open` function
      - `open(file_name)`.
    - Read all lines of the opened file:
      - `readlines()` method on an opened file object (`_io.TextIOWrapper`) to get all lines of a file as a list

- [14010913](14010913.ipynb):
- [14010919](14010919.ipynb):
- [14010920](14010920.ipynb):
- [14010926](14010926.ipynb):
- [14010927](14010927.ipynb):
- [14011003](14011003.ipynb):
- [14011004](14011004.ipynb):
- [14011010](14011010.ipynb):
- [14011011](14011011.ipynb):
- [14011015](14011015.ipynb):
- [14011017](14011017.ipynb):
- [14011022](14011022.ipynb):
