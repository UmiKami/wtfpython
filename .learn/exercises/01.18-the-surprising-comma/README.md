# `01.18` The surprising comma
**Output (< 3.6):**

```py
>>> def f(x, y,):
...     print(x, y)
...
>>> def g(x=4, y=5,):
...     print(x, y)
...
>>> def h(x, **kwargs,):
  File "<stdin>", line 1
    def h(x, **kwargs,):
                     ^
SyntaxError: invalid syntax

>>> def h(*args,):
  File "<stdin>", line 1
    def h(*args,):
                ^
SyntaxError: invalid syntax
```

#### 💡 Explanation:

- Trailing comma is not always legal in formal parameters list of a Python function.
-  In Python, the argument list is defined partially with leading commas and partially with trailing commas. This conflict causes situations where a comma is trapped in the middle, and no rule accepts it.
-  **Note:** The trailing comma problem is [fixed in Python 3.6](https://bugs.python.org/issue9232). The remarks in [this](https://bugs.python.org/issue9232#msg248399) post discuss in brief different usages of trailing commas in Python.