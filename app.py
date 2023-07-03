from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    college = db.Column(db.String(100), nullable=False)
    phone_no = db.Column(db.String(10),nullable=False)

    def __repr__(self):
        return f"Student(name='{self.name}', age={self.age}, college='{self.college}', phone_no='{self.phone_no}')"

db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        college = request.form['college']
        phone_no = request.form['phone_no']

        student = Student(name=name, age=age, college=college,phone_no=phone_no)
        db.session.add(student)
        db.session.commit()

        message = "Form submitted successfully!"

    return render_template('index.html',message=message)

@app.route('/form')
def form():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
