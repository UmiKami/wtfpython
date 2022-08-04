# `01.28` The disappearing variable from outer scope
* Source: https://docs.python.org/3/reference/compound_stmts.html#except

  When an exception has been assigned using `as` target, it is cleared at the end of the `except` clause. This is as if

  ```py
  except E as N:
      foo
  ```

  was translated into

  ```py
  except E as N:
      try:
          foo
      finally:
          del N
  ```

  This means the exception must be assigned to a different name to be able to refer to it after the except clause. Exceptions are cleared because, with the traceback attached to them, they form a reference cycle with the stack frame, keeping all locals in that frame alive until the next garbage collection occurs.

* The clauses are not scoped in Python. Everything in the example is present in the same scope, and the variable `e` got removed due to the execution of the `except` clause. The same is not the case with functions that have their separate inner-scopes. The example below illustrates this:

     ```py
     def f(x):
         del(x)
         print(x)

     x = 5
     y = [5, 4, 3]
     ```

     **Output:**
     ```py
     >>> f(x)
     UnboundLocalError: local variable 'x' referenced before assignment
     >>> f(y)
     UnboundLocalError: local variable 'x' referenced before assignment
     >>> x
     5
     >>> y
     [5, 4, 3]
     ```

* In Python 2.x, the variable name `e` gets assigned to `Exception()` instance, so when you try to print, it prints nothing.

    **Output (Python 2.x):**
    ```py
    >>> e
    Exception()
    >>> print e
    # Nothing is printed!
    ```
