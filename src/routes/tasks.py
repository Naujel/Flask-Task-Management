from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.tasks_model import Task
from database.db import db
from uuid import uuid4
from datetime import datetime

main = Blueprint('task_blueprint', __name__)

@main.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@main.route('/new', methods=['POST'])
def newTask():
    id = uuid4()
    task_name = request.form['task_name']
    description = request.form['description']
    date = datetime.now()

    new_task = Task(id, task_name, description, date)
    db.session.add(new_task)
    db.session.commit()
    flash(new_task.task_name, 'added')
    return redirect(url_for('task_blueprint.index'))

@main.route('/delete/<id>')
def deleteTask(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()

    flash(task.task_name, 'deleted')
    return redirect(url_for('task_blueprint.index'))

@main.route('/update/<id>', methods=['POST'])
def updateTask(id):
    task = Task.query.get(id)
    task.task_name = request.form['task_name']
    task.description = request.form['description']
    db.session.commit()

    flash(task.task_name, 'updated')
    return redirect(url_for('task_blueprint.index'))
