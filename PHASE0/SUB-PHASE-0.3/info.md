#### Sub-phase 0.3 — JSON, Type Hints, Modules, Virtual Envs (Days 7-8)

**Learn:** reading/writing JSON with the `json` module, type hints (`def foo(x: int) -> str:`), organizing code into multiple files/modules, creating and using a virtual environment (`venv`), installing packages with `pip`.

**Where exactly:**

- [Real Python — "Working With JSON Data in Python"](https://realpython.com/python-json/) (free)
- [Real Python — "Python Type Checking"](https://realpython.com/python-type-checking/) — just the intro section on type hints, skip the mypy-deep-dive part (free)
- [Python Official Docs — venv](https://docs.python.org/3/library/venv.html)

**Assignment 0.3 — "Convert the Expense Tracker to JSON + Split into Modules"**

*Problem statement:* Take your Assignment 0.2 project and refactor it:

1. Change file storage from `.txt`/`.csv` to `.json` (each expense is a JSON object with `description`, `amount`, `category` keys)
2. Split the code into at least 2 files: `tracker.py` (the `ExpenseTracker` class) and `main.py` (the menu loop that imports and uses it)
3. Add type hints to every function signature in `tracker.py`
4. Create a virtual environment for this project and generate a `requirements.txt`

*What "done" looks like:* Your project folder has `tracker.py`, `main.py`, `expenses.json`, `requirements.txt`, and a `venv/` folder (that you `.gitignore` — see next sub-phase). Running `main.py` still works exactly as before, just cleaner.