# Python async comprehension

An async comprehension is an asynchronous version of a classical comprehension.
Asyncio supports two types of asynchronous comprehensions, they are the �~@~\async for�~@~] comprehension and the �~@~\await�~@~] comprehension.

Comprehensions allow data collections like lists, dicts, and sets to be created in a concise way.
Una comprensión de lista permite crear una lista a partir de una expresión for dentro de la nueva expresión de lista.

Por ejemplo:

...
# create a list using a list comprehension
result = [a*2 for a in range(100)]
También se admiten comprensiones para crear dictados y conjuntos.

Por ejemplo:

...
# create a dict using a comprehension
result = {a:i for a,i in zip(['a','b','c'],range(3))}
# create a set using a comprehension
result = {a for a in [1, 2, 3, 2, 3, 1, 5, 4]}
