from flask import Flask, render_template, redirect, url_for, request, flash
from config import Config
from models import db, Teacher, Subject, Student, Grade
from forms import TeacherForm, SubjectForm, StudentForm, GradeForm

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/teachers', methods=['GET', 'POST'])
def manage_teachers():
    form = TeacherForm()
    form.subject_id.choices = [(subject.id, subject.name) for subject in Subject.query.all()]
    if form.validate_on_submit():
        teacher = Teacher(name=form.name.data, subject_id=form.subject_id.data)
        db.session.add(teacher)
        db.session.commit()
        return redirect(url_for('manage_teachers'))
    teachers = Teacher.query.all()
    return render_template('teacher.html', form=form, teachers=teachers)

@app.route('/teachers/edit/<int:id>', methods=['GET', 'POST'])
def edit_teacher(id):
    teacher = Teacher.query.get_or_404(id)
    form = TeacherForm(obj=teacher)
    form.subject_id.choices = [(subject.id, subject.name) for subject in Subject.query.all()]
    if form.validate_on_submit():
        teacher.name = form.name.data
        teacher.subject_id = form.subject_id.data
        db.session.commit()
        return redirect(url_for('manage_teachers'))
    return render_template('edit_teacher.html', form=form)

@app.route('/teachers/delete/<int:id>', methods=['POST'])
def delete_teacher(id):
    teacher = Teacher.query.get_or_404(id)
    db.session.delete(teacher)
    db.session.commit()
    return redirect(url_for('manage_teachers'))

@app.route('/subjects', methods=['GET', 'POST'])
def manage_subjects():
    form = SubjectForm()
    if form.validate_on_submit():
        subject = Subject(name=form.name.data)
        db.session.add(subject)
        db.session.commit()
        return redirect(url_for('manage_subjects'))
    subjects = Subject.query.all()
    return render_template('subject.html', form=form, subjects=subjects)

@app.route('/subjects/edit/<int:id>', methods=['GET', 'POST'])
def edit_subject(id):
    subject = Subject.query.get_or_404(id)
    form = SubjectForm(obj=subject)
    if form.validate_on_submit():
        subject.name = form.name.data
        db.session.commit()
        return redirect(url_for('manage_subjects'))
    return render_template('edit_subject.html', form=form)

@app.route('/subjects/delete/<int:id>', methods=['POST'])
def delete_subject(id):
    subject = Subject.query.get_or_404(id)
    db.session.delete(subject)
    db.session.commit()
    return redirect(url_for('manage_subjects'))

@app.route('/students', methods=['GET', 'POST'])
def manage_students():
    form = StudentForm()
    if form.validate_on_submit():
        student = Student(name=form.name.data)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('manage_students'))
    students = Student.query.all()
    return render_template('student.html', form=form, students=students)

@app.route('/students/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    student = Student.query.get_or_404(id)
    form = StudentForm(obj=student)
    if form.validate_on_submit():
        student.name = form.name.data
        db.session.commit()
        return redirect(url_for('manage_students'))
    return render_template('edit_student.html', form=form)

@app.route('/students/delete/<int:id>', methods=['POST'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('manage_students'))

@app.route('/grades', methods=['GET', 'POST'])
def manage_grades():
    form = GradeForm()
    form.student_id.choices = [(student.id, student.name) for student in Student.query.all()]
    form.subject_id.choices = [(subject.id, subject.name) for subject in Subject.query.all()]
    if form.validate_on_submit():
        grade = Grade(student_id=form.student_id.data, subject_id=form.subject_id.data, grade=form.grade.data)
        db.session.add(grade)
        db.session.commit()
        return redirect(url_for('manage_grades'))
    grades = Grade.query.all()
    return render_template('grade.html', form=form, grades=grades)

@app.route('/grades/edit/<int:id>', methods=['GET', 'POST'])
def edit_grade(id):
    grade = Grade.query.get_or_404(id)
    form = GradeForm(obj=grade)
    form.student_id.choices = [(student.id, student.name) for student in Student.query.all()]
    form.subject_id.choices = [(subject.id, subject.name) for subject in Subject.query.all()]
    if form.validate_on_submit():
        grade.student_id = form.student_id.data
        grade.subject_id = form.subject_id.data
        grade.grade = form.grade.data
        db.session.commit()
        return redirect(url_for('manage_grades'))
    return render_template('edit_grade.html', form=form)

@app.route('/grades/delete/<int:id>', methods=['POST'])
def delete_grade(id):
    grade = Grade.query.get_or_404(id)
    db.session.delete(grade)
    db.session.commit()
    return redirect(url_for('manage_grades'))

if __name__ == '__main__':
    app.run(debug=True)
