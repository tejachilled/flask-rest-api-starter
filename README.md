# Flask REST API Example

This is a simple REST API built with **Python Flask** and **SQLite**, designed for beginners to learn how to build and test APIs locally.

## 🚀 What This Project Does

- Creates a REST API using Flask
- Connects to a SQLite database
- Provides a single endpoint: `GET /items`
- Returns a list of items as JSON
- Includes automated tests using Python's `unittest`

## 📁 Project Structure

```
flask_api_project/
├── app.py           # Main Flask app
├── test_app.py      # Unit tests for the API
└── requirements.txt # Python dependencies
```

## 📦 Requirements

- Python 3.x
- Flask (`pip install flask`)

Install dependencies with:

```bash
pip install -r requirements.txt
```

## ▶️ How to Run

Start the API locally:

```bash
python app.py
```

Visit: [http://127.0.0.1:5000/items](http://127.0.0.1:5000/items)

You should see JSON output like:

```json
[
  {"id": 1, "name": "Sample Item 1"},
  {"id": 2, "name": "Sample Item 2"}
]
```

## 🧪 How to Run Tests

Make sure the Flask server is **not running**, then run:

```bash
python test_app.py
```

You should see all tests pass with output like:

```
....
----------------------------------------------------------------------
Ran 4 tests in 0.01s

OK
```

## 📌 Notes

- This project uses SQLite as the backend database.
- You can easily extend this with more endpoints like POST, PUT, and DELETE.
