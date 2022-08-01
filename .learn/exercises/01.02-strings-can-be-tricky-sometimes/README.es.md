# `01.02` Strings can be tricky sometimes
+ El comportamiento en la primera y segunda porción de código es debido a una optimización de CPython (llamada "string interning (internado)") que intenta usar objetos inmutables en algunos casos en vez de crear un nuevo objeto cada vez.
+ Luego de ser "internado" muchas variables pueden hacer referencia al mismo objeto string en memoria (salvando así memoria).
+ En las porciones de código de arriba, los strings son internados implícitamente. La decisión de cuando internar un string implícitamente depende de la implementación. Hay algunas reglas que se pueden usar para averiguar si un string será internado o no:
  * Todos los strings con longitud 0 y 1 son internados.
  * Los strings son internados en el tiempo de compilación (`wtf` será internado pero `''.join(['w', 't', 'f'])` no será internado).
  * Los strings que no están compuestos de letras ASCII, dígitos o pisos bajos no son internados. Esto explica porqué 'wtf!' no fue internado debido al !. La implementación de esta regla en CPython puede ser encontrada [aquí](https://github.com/python/cpython/blob/3.6/Objects/codeobject.c#L19).
  ![image](/images/string-intern/string_intern.png)
+ Cuando `a` y `b` son asignadas a "wtf! en la misma línea, el intérprete de Python crea un nuevo objeto, para luego hacer referencia a la segunda variable al mismo tiempo. Si lo haces en líneas separadas, Python "no sabe" que ya existe `"wft!"` como un objeto (porque `"wtf!"` no está implícitamente internado debido a lo mencionado arriba). Es una optimización en el tiempo de compilación. Esta optimización no aplica a las versiones 3.7.x de CPython (clickea este [issue](https://github.com/satwikkansal/wtfpython/issues/100) para ver una discusión sobre esto).
+ Una unidad de compilación en un ambiente interactivo (como IPython) consiste en una sola declaración, donde consiste en un módulo entero en caso de módulos. `a, b = "wtf!", "wtf!"` es una sola declaración, mientras que `a = "wtf!"; b = "wtf!"` son dos declaraciones en una misma línea. Esto explica por qué las identidades son diferentes en `a = "wtf!"; b = "wtf!"`, y también explica por qué son las mismas cuando son invocadas en `some_file.py`.
+ El cambio abrupto en el output de la cuarta porción de código es debido a la optimización peephole, técnica conocida como "Constant folding". Esto significa que la expresión `'a'*20` es reemplazada por `'aaaaaaaaaaaaaaaaaaaa'` durante la compilación para salvar algunos ciclos de reloj durante el tiempo de ejecución. "Constant folding" solo ocurre en strings que tienen una longitud menor a 21. (¿Por qué? Imagina el tamaño del archivo `.pyc` generado como resultado de la expresión `'a'*10**10`). Aquí está la implementación para esto mismo.

## Instrucciones 🗒
1. Crea una variable `a` y asignale el valor `"some_string"`
2. Imprime el id de la variable `a`
3. Imprime el id de la concatenación "some", "_", and "string"

>Hint 1: Deberias estar usando el metodo `id()`

  >Hint 2: La concatenación deberia tomar lugar dentro de la funcion `print()`