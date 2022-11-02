from typing import Any
from app.application import app
from app.application.controllers import Controller
from flask import request, render_template, redirect, url_for

controller: Controller = Controller()


@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    print(request.form)
    if request.method == "POST":
        if request.form["task"]:
            controller.insert(request.form["task"])
    return redirect(url_for('index'))


@app.route('/remove_task/', methods=["GET", "POST"])
def remove_task():
    wanted = -1
    for k, v in request.form.items():
        wanted = k
    if wanted != -1:
        controller.remove(int(wanted))
    return redirect(url_for('index'))


def select() -> Any:
    return controller.select()


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', tasks=select(), phrase=controller.random_phrases())
