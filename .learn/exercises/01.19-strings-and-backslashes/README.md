# `01.19` Strings and the backslashes
**Output:**
```py
>>> print("\"")
"

>>> print(r"\"")
\"

>>> print(r"\")
File "<stdin>", line 1
    print(r"\")
              ^
SyntaxError: EOL while scanning string literal

>>> r'\'' == "\\'"
True
```

#### 💡 Explanation

- In a usual python string, the backslash is used to escape characters that may have a special meaning (like single-quote, double-quote, and the backslash itself).
    ```py
    >>> "wt\"f"
    'wt"f'
    ```
- In a raw string literal (as indicated by the prefix `r`),  the backslashes pass themselves as is along with the behavior of escaping the following character.
    ```py
    >>> r'wt\"f' == 'wt\\"f'
    True
    >>> print(repr(r'wt\"f')
    'wt\\"f'

    >>> print("\n")

    >>> print(r"\\n")
    '\\n'
    ```
- This means when a parser encounters a backslash in a raw string, it expects another character following it. And in our case (`print(r"\")`), the backslash escaped the trailing quote, leaving the parser without a terminating quote (hence the `SyntaxError`). That's why backslashes don't work at the end of a raw string.