from flask import Flask, jsonify, request, abort

app = Flask(__name__)

notes = []
next_id = 1

# Mapping the endpoints
@app.route('/notes', methods=['GET'])
# list all notes
def get_notes():
    return jsonify(notes)

@app.route('/notes', methods=['POST'])
# add a new note
def create_note():
    global next_id

    data = request.get_json()
    if not data or 'title' not in data or 'content' not in data:
        abort(400, description="Missing note title or content")

    note = {
        'id': next_id,
        'title': data['title'],
        'content': data['content']
    }
    notes.append(note)
    next_id += 1

    return jsonify(note), 201

@app.route('/notes/<int:note_id>', methods=['GET'])
# retrieve a note by ID
def get_note(note_id):
    note = next((n for n in notes if n['id'] == note_id), None)
    if note is None:
        abort(404, description="Note not found")
    return jsonify(note)

def broken_func():
print("oops bad indent")

if __name__ == '__main__':
    app.run(debug=True)
