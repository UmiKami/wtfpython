# `01.05` Hash brownies
* Uniqueness of keys in a Python dictionary is by *equivalence*, not identity. So even though `5`, `5.0`, and `5 + 0j` are distinct objects of different types, since they're equal, they can't both be in the same `dict` (or `set`). As soon as you insert any one of them, attempting to look up any distinct but equivalent key will succeed with the original mapped value (rather than failing with a `KeyError`):
  ```py
  >>> 5 == 5.0 == 5 + 0j
  True
  >>> 5 is not 5.0 is not 5 + 0j
  True
  >>> some_dict = {}
  >>> some_dict[5.0] = "Ruby"
  >>> 5.0 in some_dict
  True
  >>> (5 in some_dict) and (5 + 0j in some_dict)
  True
  ```
* This applies when setting an item as well. So when you do `some_dict[5] = "Python"`, Python finds the existing item with equivalent key `5.0 -> "Ruby"`, overwrites its value in place, and leaves the original key alone.
  ```py
  >>> some_dict
  {5.0: 'Ruby'}
  >>> some_dict[5] = "Python"
  >>> some_dict
  {5.0: 'Python'}
  ```
* So how can we update the key to `5` (instead of `5.0`)? We can't actually do this update in place, but what we can do is first delete the key (`del some_dict[5.0]`), and then set it (`some_dict[5]`) to get the integer `5` as the key instead of floating `5.0`, though this should be needed in rare cases.

* How did Python find `5` in a dictionary containing `5.0`? Python does this in constant time without having to scan through every item by using hash functions. When Python looks up a key `foo` in a dict, it first computes `hash(foo)` (which runs in constant-time). Since in Python it is required that objects that compare equal also have the same hash value ([docs](https://docs.python.org/3/reference/datamodel.html#object.__hash__) here), `5`, `5.0`, and `5 + 0j` have the same hash value.
  ```py
  >>> 5 == 5.0 == 5 + 0j
  True
  >>> hash(5) == hash(5.0) == hash(5 + 0j)
  True
  ```
  **Note:** The inverse is not necessarily true: Objects with equal hash values may themselves be unequal. (This causes what's known as a [hash collision](https://en.wikipedia.org/wiki/Collision_(computer_science)), and degrades the constant-time performance that hashing usually provides.)
