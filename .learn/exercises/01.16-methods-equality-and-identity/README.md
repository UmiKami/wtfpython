# `01.16` Methods equality and identity

1.
```py
class SomeClass:
    def method(self):
        pass

    @classmethod
    def classm(cls):
        pass

    @staticmethod
    def staticm():
        pass
```

**Output:**
```py
>>> print(SomeClass.method is SomeClass.method)
True
>>> print(SomeClass.classm is SomeClass.classm)
False
>>> print(SomeClass.classm == SomeClass.classm)
True
>>> print(SomeClass.staticm is SomeClass.staticm)
True
```

Accessing `classm` twice, we get an equal object, but not the *same* one? Let's see what happens
with instances of `SomeClass`:

2.
```py
o1 = SomeClass()
o2 = SomeClass()
```

**Output:**
```py
>>> print(o1.method == o2.method)
False
>>> print(o1.method == o1.method)
True
>>> print(o1.method is o1.method)
False
>>> print(o1.classm is o1.classm)
False
>>> print(o1.classm == o1.classm == o2.classm == SomeClass.classm)
True
>>> print(o1.staticm is o1.staticm is o2.staticm is SomeClass.staticm)
True
```

Accessing` classm` or `method` twice, creates equal but not *same* objects for the same instance of `SomeClass`.
* Functions are [descriptors](https://docs.python.org/3/howto/descriptor.html). Whenever a function is accessed as an
attribute, the descriptor is invoked, creating a method object which "binds" the function with the object owning the
attribute. If called, the method calls the function, implicitly passing the bound object as the first argument
(this is how we get `self` as the first argument, despite not passing it explicitly).
```py
>>> o1.method
<bound method SomeClass.method of <__main__.SomeClass object at ...>>
```
* Accessing the attribute multiple times creates a method object every time! Therefore `o1.method is o1.method` is
never truthy. Accessing functions as class attributes (as opposed to instance) does not create methods, however; so
`SomeClass.method is SomeClass.method` is truthy.
```py
>>> SomeClass.method
<function SomeClass.method at ...>
```
* `classmethod` transforms functions into class methods. Class methods are descriptors that, when accessed, create
a method object which binds the *class* (type) of the object, instead of the object itself.
```py
>>> o1.classm
<bound method SomeClass.classm of <class '__main__.SomeClass'>>
```
* Unlike functions, `classmethod`s will create a method also when accessed as class attributes (in which case they
bind the class, not to the type of it). So `SomeClass.classm is SomeClass.classm` is falsy.
```py
>>> SomeClass.classm
<bound method SomeClass.classm of <class '__main__.SomeClass'>>
```
* A method object compares equal when both the functions are equal, and the bound objects are the same. So
`o1.method == o1.method` is truthy, although not the same object in memory.
* `staticmethod` transforms functions into a "no-op" descriptor, which returns the function as-is. No method
objects are ever created, so comparison with `is` is truthy.
```py
>>> o1.staticm
<function SomeClass.staticm at ...>
>>> SomeClass.staticm
<function SomeClass.staticm at ...>
```
* Having to create new "method" objects every time Python calls instance methods and having to modify the arguments
every time in order to insert `self` affected performance badly.
CPython 3.7 [solved it](https://bugs.python.org/issue26110) by introducing new opcodes that deal with calling methods
without creating the temporary method objects. This is used only when the accessed function is actually called, so the
snippets here are not affected, and still generate methods :)