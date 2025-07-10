# Simple Notes API

This is a Python Flask API web app for managing notes. This is for HW 3.

## Features

- List all notes
- Add a new note
- Retrieve a note by ID

## Setup Instructions

1. **Clone the repository**

    ```bash
    git clone https://github.com/sirvin703/simple-notes-api.git
    cd simple_notes_api
    ```

2. **Create a virtual environment (recommended)**

    ```bash
    python -m venv venv
    source venv/bin/activate       # On Linux/Mac
    venv\Scripts\activate          # On Windows
    ```

3. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the app**

    ```bash
    python app.py
    ```

    The API will be available at:

    ```
    http://127.0.0.1:5000
    ```

5. **Run the tests**

    ```bash
    pytest
    ```

---

## Endpoints

### `GET /notes`

- Returns list of all notes.

### `POST /notes`

- Adds a new note.
- JSON body:

    ```json
    {
      "title": "Title of Note",
      "content": "Content of Note"
    }
    ```

### `GET /notes/<id>`

- Retrieves details of a single note.

---
