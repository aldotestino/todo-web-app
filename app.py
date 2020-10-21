from flask import Flask, render_template, url_for, request, redirect
from db.models.Todo import Todo
from routes.api import api_route
from db.store import todos

app = Flask(__name__)

app.register_blueprint(api_route, url_prefix='/api/v1/todos')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        todo_content = request.form['content']
        todo_date = request.form['date']
        newTodo = Todo(todo_content, todo_date)
        todos.add(newTodo)
        return redirect('/')
    else:
        return render_template('index.html', todos=todos.get())


@app.route('/update/<string:id>')
def update(id):
    todos.updateOne(id)
    return redirect('/')


@app.route('/delete/<string:id>')
def deleet(id):
    todos.deleteOne(id)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
