# Fluent Python: chapter exercises

My notes and runnable exercises while working through *Fluent Python* by Luciano Ramalho (O'Reilly), to understand how Python's data model makes user-defined objects behave like built-in types.

## Chapter 1: The Python Data Model

| File | What it demonstrates |
|---|---|
| `a_pythonic_card_deck.py` | A `FrenchDeck` class that only implements `__len__` and `__getitem__`, yet supports `len()`, indexing, slicing, iteration and `random.choice`. Cards are `collections.namedtuple` instances. |
| `named_tuple_example.py` | Defining and using a `namedtuple` (`Person`) with named fields instead of positional indexes. |
| `two_dimensional_vector_class.py` | A `Vector` class using `__repr__`, `__abs__`, `__bool__`, `__add__` and `__mul__` so vectors can be printed, measured, added and scaled with normal operators. |

## Run an example

```powershell
python chapter_1_the_python_data_model/a_pythonic_card_deck.py
```

Each script is self-contained and uses only the standard library.

## Plan

I add a folder per chapter as I finish it.
