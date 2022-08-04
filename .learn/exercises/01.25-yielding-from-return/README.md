# `01.25` Yielding from... return!
1\.

```py
def some_func(x):
    if x == 3:
        return ["wtf"]
    else:
        yield from range(x)
```

**Output (> 3.3):**

```py
>>> list(some_func(3))
[]
```

Where did the `"wtf"` go? Is it due to some special effect of `yield from`? Let's validate that,

2\.

```py
def some_func(x):
    if x == 3:
        return ["wtf"]
    else:
        for i in range(x):
          yield i
```

**Output:**

```py
>>> list(some_func(3))
[]
```

The same result, this didn't work either.

#### 💡 Explanation:

+ From Python 3.3 onwards, it became possible to use `return` statement with values inside generators (See [PEP380](https://www.python.org/dev/peps/pep-0380/)). The [official docs](https://www.python.org/dev/peps/pep-0380/#enhancements-to-stopiteration) say that,

> "... `return expr` in a generator causes `StopIteration(expr)` to be raised upon exit from the generator."

+ In the case of `some_func(3)`, `StopIteration` is raised at the beginning because of `return` statement. The `StopIteration` exception is automatically caught inside the `list(...)` wrapper and the `for` loop. Therefore, the above two snippets result in an empty list.

+ To get `["wtf"]` from the generator `some_func` we need to catch the `StopIteration` exception,

  ```py
  try:
      next(some_func(3))
  except StopIteration as e:
      some_string = e.value
  ```

  ```py
  >>> some_string
  ["wtf"]
  ```
