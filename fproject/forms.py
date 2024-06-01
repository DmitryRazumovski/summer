from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired
from models import Subject, Student

class TeacherForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    subject_id = SelectField('Предмет', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Ок')

class SubjectForm(FlaskForm):
    name = StringField('Предмет', validators=[DataRequired()])
    submit = SubmitField('Ок')

class StudentForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    submit = SubmitField('Ок')

class GradeForm(FlaskForm):
    student_id = SelectField('Ученик', coerce=int, validators=[DataRequired()])
    subject_id = SelectField('Предмет', coerce=int, validators=[DataRequired()])
    grade = IntegerField('Оценка', validators=[DataRequired()])
    submit = SubmitField('Ок')
