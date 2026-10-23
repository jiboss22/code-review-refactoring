# Design Decisions

The biggest problem with the original script was that its names didn't
explain anything. Names like `do_math_stuff`, `x`, and `list1` force a
reader to read every line of code just to figure out what is going on.
I renamed things based on what they actually do or hold. For example,
`transform_numbers` tells you the function changes numbers, and
`format_words` tells you it formats words. I also used `number` and `word`
instead of short names like `num` and `s`, so the code reads almost like a
sentence. I followed PEP 8 for all names, using lowercase with underscores
for functions and variables and all caps for the constant. This way the
code looks like other professional Python code, and another developer
would know what to expect.

To make the functions shorter and clearer, I used a list comprehension in
`transform_numbers` and `" ".join()` in `format_words`. The original loops
needed several steps: create an empty list or string, loop through the
items, check a condition, and add each result. The new versions show the
whole rule in one expression, so you can see exactly what happens to each
item. Using `join()` was especially helpful, because it only puts spaces
between words. That removed the extra trailing space and the `strip()`
call that the original needed to clean it up. I didn't try to make the
code as short as possible, though. I split each expression across a few
lines so it stays easy to read and fits PEP 8's line length limit.

These changes also make the program easier to maintain. Every function
now has a docstring that explains what goes in and what comes out, so
someone can use it without reading the code inside. I moved the number 5
into a named constant, `LONG_WORD_LENGTH`. If someone needs to change the
rule later, they only have to update one clearly labeled line, instead of
searching for a number with no explanation. I only added comments where
they explain *why* something is done, not *what* the code does, because
comments that repeat the code just get out of date. Finally, I tested the
new version against the original with several different inputs to make
sure it still works exactly the same. A refactor should improve the code
without changing what it does.
