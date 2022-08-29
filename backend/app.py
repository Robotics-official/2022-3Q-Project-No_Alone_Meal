from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

import os

app = Flask(__name__)

# /// = relative path, //// = absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


@app.route("/")
def home():
    todo_list = Todo.query.all()
    try:
        todo = todo_list[-1]
    except:
        todo = todo_list[0]
    return render_template("base.html", todo=todo)


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    f = open("newquest.txt", 'w')
    f.close()
    return redirect(url_for("home"))

@app.route("/quest")
def quest():
    if os.path.exists('./newquest.txt'):
        return "ARRIVE"
    else:
        return "NOTHING"

@app.route("/update")
def update():
    todo_list = Todo.query.all()
    todo = todo_list[-1]
    todo.complete = not todo.complete
    db.session.commit()
    if os.path.exists('./newquest.txt'):
        os.remove('./newquest.txt')
    return redirect(url_for("home"))


@app.route("/delete")
def delete():
    todo_list = Todo.query.all()
    todo = todo_list[-1]
    db.session.delete(todo)
    db.session.commit()
    if os.path.exists('./newquest.txt'):
        os.remove('./newquest.txt')
    return redirect(url_for("home"))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
