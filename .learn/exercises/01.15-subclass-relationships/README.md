# `01.15` Subclass relationships

**Output:**
```py
>>> from collections import Hashable
>>> issubclass(list, object)
True
>>> issubclass(object, Hashable)
True
>>> issubclass(list, Hashable)
False
```

The Subclass relationships were expected to be transitive, right? (i.e., if `A` is a subclass of `B`, and `B` is a subclass of `C`, the `A` _should_ a subclass of `C`)

#### 💡 Explanation:

* Subclass relationships are not necessarily transitive in Python. Anyone is allowed to define their own, arbitrary `__subclasscheck__` in a metaclass.
* When `issubclass(cls, Hashable)` is called, it simply looks for non-Falsey "`__hash__`" method in `cls` or anything it inherits from.
* Since `object` is hashable, but `list` is non-hashable, it breaks the transitivity relation.
* More detailed explanation can be found [here](https://www.naftaliharris.com/blog/python-subclass-intransitivity/).