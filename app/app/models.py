from . import db

class Classroom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    capacity = db.Column(db.Integer)

class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    subject = db.Column(db.String(100))
    max_classes_per_day = db.Column(db.Integer)

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    weekly_sessions = db.Column(db.Integer)

class Batch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    subjects = db.relationship('Subject', secondary='batch_subject')

batch_subject = db.Table('batch_subject',
    db.Column('batch_id', db.Integer, db.ForeignKey('batch.id')),
    db.Column('subject_id', db.Integer, db.ForeignKey('subject.id'))
)
