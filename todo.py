from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app= Flask(__name__, template_folder="templates")

todos = [{"task":"Sample Todo", "done": False}]


@app.route("/")
def index():
    return render_template("index.html", todos=todos)



@app.route("/add", methods=["POST"])
def add():
    todo = request.form['todo']
    
    alarm = request.form['alarm']
    
    # Save task and alarm time (alarm is optional)
    if alarm:
        # Convert datetime string to datetime object if an alarm is set
        alarm_time = datetime.strptime(alarm, '%Y-%m-%dT%H:%M')
    else:
        alarm_time = None

    # Add the task with its alarm time to the todos list
    todos.append({"task": todo, "alarm": alarm_time, "done": False})

    return redirect(url_for('index'))


@app.route("/edit/<int:index>", methods=["GET","POST"])
def edit(index):
    todo = todos[index]
    if request.method =="POST":
        todo['task'] = request.form["todo"]
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", todo=todo, index=index)

@app.route("/check/<int:index>")
def check(index):
    todos[index]['done']= not todos[index]['done']
    return redirect(url_for("index"))


@app.route("/delete/<int:index>")
def delete(index):
    del todos[index]
    return redirect(url_for("index"))

if __name__=='__main__':
    app.run(debug=True)





