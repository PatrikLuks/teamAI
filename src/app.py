from typing import Any
from flask import Flask, request, jsonify

app = Flask(__name__)
todos: list[str] = []


@app.get("/todos")
def get_todos():
    return jsonify(todos)


@app.post("/todos")
def add_todo():
    data: dict[str, Any] = (request.get_json(silent=True) or {})  # type: ignore[assignment]
    task = str(data.get("task", ""))
    todos.append(task)
    return jsonify({"message": "Task added"}), 201


if __name__ == "__main__":  # pragma: no cover
    app.run(debug=True)
