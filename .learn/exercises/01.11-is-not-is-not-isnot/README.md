# `01.11` `is not ...` is not `is (not ...)`

```py
>>> 'something' is not None
True
>>> 'something' is (not None)
False
```

#### 💡 Explanation

- `is not` is a single binary operator, and has behavior different than using `is` and `not` separated.
- `is not` evaluates to `False` if the variables on either side of the operator point to the same object and `True` otherwise. 
- In the example, `(not None)` evaluates to `True` since the value `None` is `False` in a boolean context, so the expression becomes `'something' is True`.