from app import app


# Test 1
def test_get_notes_initially_empty():
    # creates test client and checks for empty list; expects 200
    client = app.test_client()
    response = client.get('/notes')
    assert response.status_code == 200
    assert response.get_json() == []


# Test 2
def test_create_note():
    # posts JSON payload and checks returned fields; expects 201
    client = app.test_client()
    payload = {
        "title": "Test Note",
        "content": "This is a test note."
    }
    response = client.post('/notes', json=payload)
    json_data = response.get_json()

    assert response.status_code == 201
    assert json_data['title'] == "Test Note"
    assert json_data['content'] == "This is a test note."
    assert 'id' in json_data


# Test 3
def test_get_notes_after_creation():
    # adds a note, gets /notes and checks the note is there; expects 200
    client = app.test_client()
    payload = {
        "title": "Note 1",
        "content": "Content 1"
    }
    client.post('/notes', json=payload)

    response = client.get('/notes')
    notes = response.get_json()
    assert response.status_code == 200
    assert any(note["title"] == "Note 1" for note in notes)


# Test 4
def test_get_single_note():
    # posts a note, then fetches it by its ID; expects 200
    client = app.test_client()
    payload = {
        "title": "Single Note",
        "content": "Content"
    }
    post_response = client.post('/notes', json=payload)
    note_id = post_response.get_json()["id"]

    response = client.get(f'/notes/{note_id}')
    json_data = response.get_json()

    assert response.status_code == 200
    assert json_data["title"] == "Single Note"


# Test 5
def test_get_nonexistent_note():
    # tries to retrieve a note that doesn't exist; expects 404
    client = app.test_client()
    response = client.get('/notes/9999')
    assert response.status_code == 404


# Failure Test
def test_intentional_failure():
    assert 1 == 2
