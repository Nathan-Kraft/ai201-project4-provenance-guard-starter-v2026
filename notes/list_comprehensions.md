List comprehensions - notes

A list comprehension is a compressed way to write a for loop that builds
a new list. General shape:

    [expression for item in iterable if condition]

The "if condition" part is optional. Read it as: loop over iterable,
optionally skip items that fail condition, then compute expression for
each one kept, and collect the results into a new list.

Example 1 - no filter

    lengths = [len(words(s)) for s in sentences(text)]

Same as:

    lengths = []
    for s in sentences(text):
        lengths.append(len(words(s)))

Step by step:
  1. for s in sentences(text) - loop over each sentence string
  2. len(words(s)) - for each one, split into words and count them
  3. [...] - collect all the counts into a new list

Example 2 - with a filter

    lengths = [n for n in lengths if n > 0]

Same as:

    filtered = []
    for n in lengths:
        if n > 0:
            filtered.append(n)
    lengths = filtered

Step by step:
  1. for n in lengths - loop over the numbers
  2. if n > 0 - skip any that are not positive
  3. n - the expression is just n itself, unchanged, so this filters
     without transforming

How to read any list comprehension:
  - find the "for ... in ..." part first - that's the loop
  - find the "if ..." part next, if there is one - that's the filter
  - whatever is left, at the very front, is what gets computed and
    collected for each item that survives
