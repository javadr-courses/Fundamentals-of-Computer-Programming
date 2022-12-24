# Introduction-to-Programming-with-Python
A repository containing all jupyter notebook files of csq_ipf22 class.
It has a table of content for finding the subjects/code-parts/algorithms easier. (And since github is able to render jupyter notebook files on its web page, it's accessible from everywhere).

<hr/>

## Table of contents

- [14010801](14010801/14010801.ipynb):
  - Introducing basic syntax of python (such as defining variables, how to call functions, inputting strings, etc..)
  - Basic usage of built-in functions (such as `print`, `help`, `input`, `len`)
  - Introducing `map(int, input().split())` syntax to get multiple input from one line.
  - Introducing **Syntax error**, **Runtime error** and **Logical error** in programming (and python).
  - Introducing to usage of single-quotation mark and double-quotation mark.

- [14010807](14010807/14010807.ipynb):
  - Introducing usage of `type`, differences between `float`, `int`, `NoneType`, etc...
  - Introducing usage of `bin`, `oct`, `hex`, etc...
  - Learning that `int() base must be >= 2 and <= 36, or 0`.
  - Introducing `math` package (`import math`), basic usage of `math.sin`, `math.pi`, `math.e` and `math.tan`.
  - Introducing function definitions (how to define a function header, arguments and return value).
  - Introducing _fruitful function_.
  - Introducing to syntax `from something import stuff`.

- [14010808](14010808/14010808.ipynb):
  - Introducing `min`, `max`, `abs` built-in functions.
  - Introducing `turtle` package and `turtle.Turtle` class.
  - Introducing `for something in range(number):` syntax (_basic for loop_).
  - Defining some functions called `n_angle`, `square`, `polygon`, `circle`, `arc` and `rectangle` for turtle
  - Introducing to how to set speed of the turtle (using `bob.speed` method).
  - Introducing python `docstring` feature (which is used for documentations (similar to comments)).
  - Defining a function called `area` which calculates the area using `math.pi`.
  - Introducing usage of `bob.shape` method (implemented on `turtle.Turtle` class).

- [14010814](14010814/14010814.ipynb):
  - Introducing some math operators such as `//`.
  - Showing that using `==` operator for floats can be dangerous, it's better to compare them like `< 10**-20` or use some tricks similar to this.
  - Showing that boolean values (`True`/`False`), are just integers (`True == 1`, `False == 0`).
  - Introducing basic `if...else` syntax.
  - Introducing new keyword `pass`.
  - Introducing new logical-boolean operators (such as `and`, `or`, `not`).
  - Encountering first `RecursionError` in our class (by calling `test` function inside of `test` function without any stop-condition).
  - Introducing basic `Recursion` (`Recursive function`).
  - Defining `fact` function as an example of `Recursion` to generate a piece of Factorial series.

- [14010815](14010815/14010815.ipynb):
  - Reminder for previous session, redefining `fact` function (an example of recursive).
  - Showing that `0 * 'string'` results in an empty string with length of 0.
  - Defining function `test_stack_depth` which has an argument of `depth` (to show maximum depth of stacks).
  - Re-introducing `map(test, input().split())` syntax (which was previously mentioned in first notebook).
  - Showing that first argument of `map` can be any function, which will get called on every single thing of its second argument.
  - Introducing `koch` using `turtle` module.

- [14010822](14010822/14010822.ipynb):
  - Showing that if we convert a `float` value to `int` value, the number after floating-point will be dropped and the result number will become a normal integer.
  - Introducing `end=` and `sep=` arguments for `print` function.
  - Showing how to calculate radical 2 using f(x) and f-prime(x) (`fp(x)`).
  - Introducing `while loop`.
  - Introducing `mod` operator (`i%2`).
  - Calculating Factorial series (redefining `fact` function) using `for` and `while` loops.
  - Calculating Fibonacci series (defining `fib` function) using `for loop`.
  - Calculating Fibonacci series (defining `fib` function) using `recursive function` (and comparing these two's running time).

- [14010828](14010828/14010828.ipynb):
  - Introducing string slices.
  - Introducing indexes in strings.
  - Defining `reverse` function which will reverse a given string (using `for loop`).
  - Defining `find` functions will will find a character/sub-str inside of the string (using loops).
  - Introducing `in` operator.
  - Introducing common methods defined in str class (such as `count`, `find`, `index`, `strip`, `lstrip`, `replace`).

- [14010905](14010905/14010905.ipynb):
  - Introducing **Algorithms, Flowcharts and Problem solving**.
  - Defining `fact` and `neper` functions and comparing their running time.
  - Defining `birthday` function which shows how to use `.format` method on strings to format float types in a string.
  - Defining `is_complete` function and calculating its running time.
  - Introducing a mathematic formula for `complete` numbers (which is `2**(p-1) * (2**p-1)`, where p is a primary number).
  - Calculating BMI.

- [14010906](14010906/14010906.ipynb):
  - Defining a function called `pi` which calculates and returns the `pi` number using a math formula.
  - Reminder to be careful when doing math operations with `float` types (for example `.1+.1+.1 != .3`).
  - Defining `sum_digit` function which calculates and returns summary of all of the digits inside of an integer (for example `134 --> 1+3+4`).
  - Defining `one_digitizer` function which calls `sum_digit` until the result number has only 1 digit (it's less than 10) using `for loop`.
  - Defining a function called `mehrpooya` which uses a faster, less-expensive and more efficient algorithm to compute the same thing as `one_digitizer` function.
  - Defining `rev_num` function which reverts all digits of a number and returns the result (for example `159 --> 951`).



</hr>

