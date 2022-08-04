# `01.22` What's wrong with booleans?
* `bool` is a subclass of `int` in Python
    
    ```py
    >>> issubclass(bool, int)
    True
    >>> issubclass(int, bool)
    False
    ```
    
* And thus, `True` and `False` are instances of `int`
  ```py
  >>> isinstance(True, int)
  True
  >>> isinstance(False, int)
  True
  ```

* The integer value of `True` is `1` and that of `False` is `0`.
  ```py
  >>> int(True)
  1
  >>> int(False)
  0
  ```

* See this StackOverflow [answer](https://stackoverflow.com/a/8169049/4354153) for the rationale behind it.

* Initially, Python used to have no `bool` type (people used 0 for false and non-zero value like 1 for true).  `True`, `False`, and a `bool` type was added in 2.x versions, but, for backward compatibility, `True` and `False` couldn't be made constants. They just were built-in variables, and it was possible to reassign them

* Python 3 was backward-incompatible, the issue was finally fixed, and thus the last snippet won't work with Python 3.x!