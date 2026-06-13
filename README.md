# String Utils

A tiny collection of helper functions for working with strings.

## Functions

- `reverse_string(s)` - returns the reverse of a string.
- `is_palindrome(s)` - returns True if a string is a palindrome.
- `count_vowels(s)` - returns the number of vowels in a string.

## Todo API

A small Flask API for managing a todo list.

- `GET /todos` - list all todos
- `POST /todos` - create a todo (`{"title": "..."}`)
- `GET /todos/<id>` - get a single todo
- `PATCH /todos/<id>` - update a todo's title or done status
- `DELETE /todos/<id>` - delete a todo

Run it with:

```bash
pip install -r requirements.txt
python app.py
```

## Running Tests

```bash
pytest
```
