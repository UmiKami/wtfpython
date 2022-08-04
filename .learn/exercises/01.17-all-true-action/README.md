# `01.17` All-true-ation

```py
>>> all([True, True, True])
True
>>> all([True, True, False])
False

>>> all([])
True
>>> all([[]])
False
>>> all([[[]]])
True
```

Why's this True-False alteration?

#### 💡 Explanation:

- The implementation of `all` function is equivalent to

- ```py
  def all(iterable):
      for element in iterable:
          if not element:
              return False
      return True
  ```

- `all([])` returns `True` since the iterable is empty. 
- `all([[]])` returns `False` because the passed array has one element, `[]`, and in python, an empty list is falsy.
- `all([[[]]])` and higher recursive variants are always `True`. This is because the passed array's single element (`[[...]]`) is no longer empty, and lists with values are truthy.
