#### Sub-phase 0.5 — Async, HTTP Requests, Logging, Basic Testing (Days 11-12)

**Learn:** `async`/`await` basics, making HTTP requests with `requests` (sync) and understanding why `httpx`/`aiohttp` exist for async, environment variables with `python-dotenv`, basic logging with the `logging` module, writing your first tests with `pytest`.

**Where exactly:**

- [Real Python — "Async IO in Python: A Complete Walkthrough"](https://realpython.com/async-io-python/) — read just the first half (concepts + basic example), skip the deep event-loop internals
- [Real Python — "Python's Requests Library"](https://realpython.com/python-requests/)
- [Real Python — "Getting Started With Testing in Python"](https://realpython.com/python-testing/) — pytest section only

**Assignment 0.5 — "GitHub Profile Fetcher"** *(this is your Phase 0 capstone — it directly sets up Phase 1's API work)*

*Problem statement:* Write a script that:

1. Takes a GitHub username as input
2. Calls the public GitHub API (`https://api.github.com/users/{username}`) using `requests`
3. Parses the JSON response and prints: name, bio, public repo count, follower count
4. Handles the case where the username doesn't exist (404) gracefully — print a friendly error, don't crash
5. Stores your API calls' results in a local `cache.json` so repeated lookups of the same user don't hit the API again

*Sub-assignments:*

- Sub-task A: Add logging (`logging.info`, `logging.error`) instead of `print()` for status messages, writing logs to a file `app.log`.
- Sub-task B: Write 2-3 `pytest` tests — e.g., test that your JSON-parsing function correctly extracts the fields from a sample response dictionary (you don't need to hit the real API in tests, just pass in a fake dict).
- Sub-task C (stretch): Rewrite the API call using `async`/`await` with `httpx`, and fetch 3 different usernames concurrently, printing how much faster it is than doing them one at a time.

*What "done" looks like:* You can run `python fetch_profile.py torvalds`, get correct real data back, get a clean error for a fake username, see logs written to a file, and have passing tests. This assignment is intentionally the bridge into Phase 1 — you're already doing "call an external API and handle the response," which is 80% of what an LLM API call looks like.