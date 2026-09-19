#### Sub-phase 0.1 — Core Python Syntax (Days 1-3)

**Learn:** variables, data types, `if`/`elif`/`else`, `for`/`while` loops, functions, `return`, `break`/`continue`, lists, tuples, dictionaries, sets, strings, string formatting (f-strings).

**Where exactly:**

- [Python Official Tutorial — Sections 3-5](https://docs.python.org/3/tutorial/introduction.html) (free, authoritative)
- Corey Schafer's YouTube playlist "Python Beginner Tutorials" — watch the videos on lists/dicts/tuples/sets and string formatting specifically (free)

**Assignment 0.1 — "Word Frequency Counter"**

*Problem statement:* You're given a `.txt` file containing a paragraph of text (any article or essay — grab one from Wikipedia). Write a Python script that:

1. Reads the file
2. Cleans the text (lowercase everything, strip punctuation)
3. Splits it into words
4. Counts how many times each word appears
5. Prints the top 10 most frequent words, sorted by count descending, in the format: `word: count`

*Sub-assignments (do these as extensions once the base version works):*

- Sub-task A: Exclude common "stopwords" (the, is, a, an, and, etc.) from the count — hardcode a list of \~15 stopwords yourself.
- Sub-task B: Instead of printing, write the results to a new file called `word_counts.txt`.
- Sub-task C: Make it accept the filename as a command-line argument (`python word_count.py myfile.txt`) instead of hardcoding it.

*What "done" looks like:* Running `python word_count.py article.txt` produces a correct, sorted word-count file with no crashes on edge cases (empty lines, punctuation attached to words like "end.").