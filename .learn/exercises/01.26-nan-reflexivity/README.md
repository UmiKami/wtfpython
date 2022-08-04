# `01.26` Nan-reflexivity
1\.

```py
a = float('inf')
b = float('nan')
c = float('-iNf')  # These strings are case-insensitive
d = float('nan')
```

**Output:**

```py
>>> a
inf
>>> b
nan
>>> c
-inf
>>> float('some_other_string')
ValueError: could not convert string to float: some_other_string
>>> a == -c # inf==inf
True
>>> None == None # None == None
True
>>> b == d # but nan!=nan
False
>>> 50 / a
0.0
>>> a / a
nan
>>> 23 + b
nan
```

2\.

```py
>>> x = float('nan')
>>> y = x / x
>>> y is y # identity holds
True
>>> y == y # equality fails of y
False
>>> [y] == [y] # but the equality succeeds for the list containing y
True
```



#### 💡 Explanation:

- `'inf'` and `'nan'` are special strings (case-insensitive), which, when explicitly typecast-ed to `float` type, are used to represent mathematical "infinity" and "not a number" respectively.

- Since according to IEEE standards ` NaN != NaN`, obeying this rule breaks the reflexivity assumption of a collection element in Python i.e. if `x` is a part of a collection like `list`, the implementations like comparison are based on the assumption that `x == x`.  Because of this assumption, the identity is compared first (since it's faster) while comparing two elements, and the values are compared only when the identities mismatch. The following snippet will make things clearer,

  ```py
  >>> x = float('nan')
  >>> x == x, [x] == [x]
  (False, True)
  >>> y = float('nan')
  >>> y == y, [y] == [y]
  (False, True)
  >>> x == y, [x] == [y]
  (False, False)
  ```

  Since the identities of `x` and `y` are different, the values are considered, which are also different; hence the comparison returns `False` this time.

- Interesting read: [Reflexivity, and other pillars of civilization](https://bertrandmeyer.com/2010/02/06/reflexivity-and-other-pillars-of-civilization/)