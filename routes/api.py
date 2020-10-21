from flask import Blueprint, request
from json import dumps
from db.models.Todo import Todo
from db.store import todos

api_route = Blueprint('api_route', __name__)

@api_route.route('/', methods=['GET'])
def getTodos():
    return dumps([todo.serialize() for todo in todos.get()]), {'Content-Type': 'application/json'}


@api_route.route('/', methods=['POST'])
def addTodo():
    body = request.json
    newTodo = Todo(body['content'], body['date'])
    todos.add(newTodo)
    return dumps(newTodo.serialize()), {'Content-Type': 'application/json'}


@api_route.route('/update/<string:id>', methods=['PATCH'])
def updateTodo(id):
    todo = todos.updateOne(id)
    return dumps(todo.serialize()), {'Content-Type': 'application/json'}


@api_route.route('/delete/<string:id>', methods=['DELETE'])
def deleteTodo(id):
    deleted = todos.deleteOne(id)
    return dumps(deleted.serialize()), {'Content-Type': 'application/json'}
