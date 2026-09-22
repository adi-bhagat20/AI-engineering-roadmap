#### Sub-phase 0.2 — Functions, OOP, Comprehensions, Exceptions (Days 4-6)

**Learn:** writing reusable functions with default/keyword args, classes and objects (`__init__`, methods, attributes), list/dict comprehensions, `try`/`except`/`finally`, custom exceptions, file handling (`with open(...)`).
**Where exactly:**

- [Python Official Tutorial — Sections 6, 8, 9](https://docs.python.org/3/tutorial/classes.html) (classes)
- Object Oriented Programming in Python by not your college (https://www.youtube.com/watch?v=IhG3UJzkjnw&t=380s)
- [Real Python — "Python Exceptions: An Introduction"](https://realpython.com/python-exceptions/) (free)

**Assignment 0.2 — "Personal Expense Tracker (CLI, in-memory)"**
*Problem statement:* Build a command-line expense tracker using a class called `ExpenseTracker`. It should support:

1. Adding an expense: description, amount, category (e.g., "Food", "Transport")
2. Listing all expenses
3. Showing total spent per category
4. Showing overall total

Use a menu loop (`while True`) that lets the user type `add`, `list`, `summary`, or `exit`.
*Sub-assignments:*

- Sub-task A: Raise and handle a custom exception `InvalidAmountError` if the user enters a negative or non-numeric amount.
- Sub-task B: Rewrite the "summary per category" logic using a dictionary comprehension instead of a manual loop.
- Sub-task C: Add a `save_to_file()` method that writes all expenses to a `.txt` or `.csv` file, and a `load_from_file()` method that reads them back in on startup.

*What "done" looks like:* You can add 5+ expenses across 3+ categories, see a correct summary, close the program, reopen it, and your expenses are still there (because of save/load).
