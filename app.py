from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow all origins (or restrict to your frontend domain)

tasks = []
task_id_counter = 1

@app.route('/')
def home():
    return "To-Do Manager API is running!"

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_counter
    data = request.json
    text = data.get('text')
    if not text:
        return jsonify({"error": "Task text required"}), 400
    task = {
        "id": task_id_counter,
        "text": text,
        "completed": False
    }
    tasks.append(task)
    task_id_counter += 1
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    for task in tasks:
        if task["id"] == task_id:
            task['text'] = data.get('text', task['text'])
            if 'completed' in data:
                task['completed'] = data['completed']
            return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({"message": "Task deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
