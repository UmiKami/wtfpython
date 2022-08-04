# `01.07` Disorder within order
- The reason why intransitive equality didn't hold among `dictionary`, `ordered_dict` and `another_ordered_dict` is because of the way `__eq__` method is implemented in `OrderedDict` class. From the [docs](https://docs.python.org/3/library/collections.html#ordereddict-objects)
  
    > Equality tests between OrderedDict objects are order-sensitive and are implemented as `list(od1.items())==list(od2.items())`. Equality tests between `OrderedDict` objects and other Mapping objects are order-insensitive like regular dictionaries.
- The reason for this equality in behavior is that it allows `OrderedDict` objects to be directly substituted anywhere a regular dictionary is used.
- Okay, so why did changing the order affect the length of the generated `set` object? The answer is the lack of intransitive equality only. Since sets are "unordered" collections of unique elements, the order in which elements are inserted shouldn't matter. But in this case, it does matter. Let's break it down a bit,
    ```py
    >>> some_set = set()
    >>> some_set.add(dictionary) # these are the mapping objects from the snippets above
    >>> ordered_dict in some_set
    True
    >>> some_set.add(ordered_dict)
    >>> len(some_set)
    1
    >>> another_ordered_dict in some_set
    True
    >>> some_set.add(another_ordered_dict)
    >>> len(some_set)
    1

    >>> another_set = set()
    >>> another_set.add(ordered_dict)
    >>> another_ordered_dict in another_set
    False
    >>> another_set.add(another_ordered_dict)
    >>> len(another_set)
    2
    >>> dictionary in another_set
    True
    >>> another_set.add(another_ordered_dict)
    >>> len(another_set)
    2
    ```
    So the inconsistency is due to `another_ordered_dict in another_set` being `False` because `ordered_dict` was already present in `another_set` and as observed before, `ordered_dict == another_ordered_dict` is `False`.
