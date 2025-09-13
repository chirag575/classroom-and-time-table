from flask import Blueprint, render_template, request
from .models import Classroom, Faculty, Subject, Batch
from .scheduler import generate_timetable
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/generate', methods=['POST'])
def generate():
    data = request.form
    timetable = generate_timetable(data)
    return render_template('index.html', timetable=timetable)
