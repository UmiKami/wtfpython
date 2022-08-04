# `01.13` Schrödinger's variable

* When defining a function inside a loop that uses the loop variable in its body, the loop function's closure is bound to the *variable*, not its *value*. The function looks up `x` in the surrounding context, rather than using the value of `x` at the time the function is created. So all of the functions use the latest value assigned to the variable for computation. We can see that it's using the `x` from the surrounding context (i.e. *not* a local variable) with:
```py
>>> import inspect
>>> inspect.getclosurevars(funcs[0])
ClosureVars(nonlocals={}, globals={'x': 6}, builtins={}, unbound=set())
```
Since `x` is a global value, we can change the value that the `funcs` will lookup and return by updating `x`:

```py
>>> x = 42
>>> [func() for func in funcs]
[42, 42, 42, 42, 42, 42, 42]
```

* To get the desired behavior you can pass in the loop variable as a named variable to the function. **Why does this work?** Because this will define the variable *inside* the function's scope. It will no longer go to the surrounding (global) scope to look up the variables value but will create a local variable that stores the value of `x` at that point in time.

```py
funcs = []
for x in range(7):
    def some_func(x=x):
        return x
    funcs.append(some_func)
```

**Output:**

```py
>>> funcs_results = [func() for func in funcs]
>>> funcs_results
[0, 1, 2, 3, 4, 5, 6]
```

It is not longer using the `x` in the global scope:

```py
>>> inspect.getclosurevars(funcs[0])
ClosureVars(nonlocals={}, globals={}, builtins={}, unbound=set())
```