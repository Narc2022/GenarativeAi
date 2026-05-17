````markdown
# Python Data Structures: List, Tuple, Set, Dictionary

This document explains the four core Python data structures: **List, Tuple, Set, and Dictionary** with examples and key differences.

---

## 📌 1. List
- Ordered collection
- Mutable (can be changed)
- Allows duplicate values

### Example:
```python
my_list = [1, 2, 3, 2]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 2, 4]
````

### Use Case:

Use when you need a dynamic collection that can be modified.

---

## 📌 2. Tuple

* Ordered collection
* Immutable (cannot be changed)
* Allows duplicates

### Example:

```python
my_tuple = (1, 2, 3, 2)
# my_tuple[0] = 5  ❌ This will raise an error
```

### Use Case:

Use when data should remain constant (e.g., coordinates, fixed values).

---

## 📌 3. Set

* Unordered collection
* Mutable
* Does NOT allow duplicates

### Example:

```python
my_set = {1, 2, 3, 2}
print(my_set)  # Output: {1, 2, 3}
```

### Use Case:

Use for storing unique values and performing set operations (union, intersection).

---

## 📌 4. Dictionary

* Collection of key-value pairs
* Ordered (Python 3.7+)
* Mutable
* Keys must be unique

### Example:

```python
my_dict = {"name": "Alice", "age": 25}
print(my_dict["name"])  # Output: Alice
```

### Use Case:

Use for mapping data (like JSON objects or databases).

---

## 🔁 Comparison Table

| Feature    | List | Tuple | Set  | Dictionary  |
| ---------- | ---- | ----- | ---- | ----------- |
| Ordered    | ✅    | ✅     | ❌    | ✅           |
| Mutable    | ✅    | ❌     | ✅    | ✅           |
| Duplicates | ✅    | ✅     | ❌    | Keys ❌      |
| Syntax     | `[]` | `()`  | `{}` | `{key:val}` |

---

## 🚀 Summary

* **List** → Flexible & changeable collection
* **Tuple** → Fixed & unchangeable data
* **Set** → Unique elements only
* **Dictionary** → Key-value mapping

---

## 📚 Practice Tip

Try creating examples for each data structure and perform basic operations like:

* Adding/removing elements
* Iterating through data
* Accessing values

---

Happy Coding! 🎯

```

---

If you want, I can also **convert this into a GitHub-ready project README with badges, sections, and examples** or add **interview questions + answers**.
```
