# `01.01` First things first!

The Walrus operator (`:=`) was introduced in Python 3.8, it can be useful in situations where you'd want to assign values to variables within an expression.

```py
def some_func():
        # Assume some expensive computation here
        # time.sleep(1000)
        return 5

# So instead of,
if some_func():
        print(some_func()) # Which is bad practice since computation is happening twice

# or
a = some_func()
if a:
    print(a)

# Now you can concisely write
if a := some_func():
        print(a)
```

**Output (> 3.8):**

```py
5
5
5
```

This saved one line of code, and implicitly prevented invoking `some_func` twice.

- Unparenthesized "assignment expression" (use of walrus operator), is restricted at the top level, hence the `SyntaxError` in the `a := "wtf_walrus"` statement of the first snippet. Parenthesizing it worked as expected and assigned `a`.  

- As usual, parenthesizing of an expression containing `=` operator is not allowed. Hence the syntax error in `(a, b = 6, 9)`. 

- The syntax of the Walrus operator is of the form `NAME:= expr`, where `NAME` is a valid identifier, and `expr` is a valid expression. Hence, iterable packing and unpacking are not supported which means, 

  - `(a := 6, 9)` is equivalent to `((a := 6), 9)` and ultimately `(a, 9) ` (where `a`'s value is 6')

    ```py
    >>> (a := 6, 9) == ((a := 6), 9)
    True
    >>> x = (a := 696, 9)
    >>> x
    (696, 9)
    >>> x[0] is a # Both reference same memory location
    True
    ```

  - Similarly, `(a, b := 16, 19)` is equivalent to `(a, (b := 16), 19)` which is nothing but a 3-tuple. 