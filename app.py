from flask import Flask, jsonify, request, abort

app = Flask(__name__)

todos = []
next_id = 1


@app.route("/todos", methods=["GET"])
def list_todos():
    return jsonify(todos)


@app.route("/todos", methods=["POST"])
def create_todo():
    global next_id
    data = request.get_json(silent=True) or {}
    title = data.get("title")
    if not title:
        abort(400, description="title is required")

    todo = {"id": next_id, "title": title, "done": False}
    todos.append(todo)
    next_id += 1
    return jsonify(todo), 201


@app.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    todo = next((t for t in todos if t["id"] == todo_id), None)
    if todo is None:
        abort(404, description="todo not found")
    return jsonify(todo)


@app.route("/todos/<int:todo_id>", methods=["PATCH"])
def update_todo(todo_id):
    todo = next((t for t in todos if t["id"] == todo_id), None)
    if todo is None:
        abort(404, description="todo not found")

    data = request.get_json(silent=True) or {}
    if "done" in data:
        todo["done"] = bool(data["done"])
    if "title" in data:
        todo["title"] = data["title"]
    return jsonify(todo)


@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    todo = next((t for t in todos if t["id"] == todo_id), None)
    if todo is None:
        abort(404, description="todo not found")
    todos.remove(todo)
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)
