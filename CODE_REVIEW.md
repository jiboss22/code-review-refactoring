# Code Review: undocumented_script.py

## Initial Review

I ran the original script and it printed:

```
Processed Numbers: [3, 4, 9, 8, 15, 12, 21]
Processed Strings: apple BANANA kiwi GRAPEFRUIT CHERRY
```

The script works, but I found three main areas to improve.

### 1. Unclear function and variable names
The names `do_math_stuff` and `do_string_stuff` don't say what the
functions actually do. Inside them, `x`, `s`, and `result` are vague, and
in `main()` the lists are just called `list1` and `list2`. A reader has to
trace through every line to figure out what each name means. Clear names
would let someone understand the code at a glance.

### 2. No documentation
None of the functions have docstrings, and there are no comments. Someone
new to the code wouldn't know what kind of input each function expects,
what it returns, or why the number 5 is used in `do_string_stuff`. This
makes the code harder to use and harder to change safely.

### 3. Loops that could be simpler
Both functions start with an empty list or string and build it up one item
at a time in a `for` loop. `do_string_stuff` also adds a space after every
word and then has to call `strip()` to remove the extra space at the end.
These patterns take more lines than needed and hide the main idea of each
function. List comprehensions and `" ".join()` can do the same work more
clearly.

## Final Review

**Did I address the three issues I originally identified?**
Yes. Each issue is covered below.

**Are the function and variable names now clear and descriptive?**
Yes. Every function and variable name now describes what it holds or does,
and all of them follow PEP 8 (lowercase with underscores, and an uppercase
name for the constant).

**Does each function contain appropriate documentation?**
Yes. All three functions, plus the module itself, have docstrings that
follow PEP 257. Each function docstring has a one-line summary, and the
two helper functions also describe their arguments and return value.

**Did my changes improve readability or maintainability?**
Yes. Each helper function is now a single, clearly documented expression,
and the length rule for words is stored in one named constant that is easy
to find and change.

**Does the program still produce the expected output?**
Yes. I ran the refactored script and compared its output with the
original's. They match exactly.

### Issue 1: Unclear names – Fixed
**What I changed:**

| Original | New |
|---|---|
| `do_math_stuff` | `transform_numbers` |
| `do_string_stuff` | `format_words` |
| `list_of_nums` | `numbers` |
| `list_of_strings` | `words` |
| `num` / `s` | `number` / `word` |
| `result` / `x` | removed (the function returns the result directly) |
| `list1` / `list2` | `sample_numbers` / `sample_words` |
| `processed_nums` / `processed_strings` | `transformed_numbers` / `formatted_words` |

**How I verified it:** I read through `main()` and confirmed that each line
can be understood without looking inside the helper functions. I also ran
the `pycodestyle` checker, which reported no PEP 8 problems.

### Issue 2: No documentation – Fixed
**What I changed:** I added a module docstring and a docstring to every
function. I added a named constant, `LONG_WORD_LENGTH`, with a comment
explaining it, and a comment in `format_words` explaining why `strip()` is
no longer needed. I didn't add comments that just repeat what the code
already says.

**How I verified it:** I ran `help(transform_numbers)` and
`help(format_words)` in Python to confirm the docstrings show up correctly
and clearly describe each function's input and output.

### Issue 3: Loops that could be simpler – Fixed
**What I changed:** I replaced the loop in `transform_numbers` with a list
comprehension. In `format_words`, I replaced the loop and string
concatenation with `" ".join()` and a generator expression, which also
removed the need for `strip()`.

**How I verified it:** I ran both the original and refactored scripts and
compared their output, and it matched exactly. I also tested both versions
with extra inputs, including empty lists, negative numbers, and mixed-case
words, and they gave the same results every time.
