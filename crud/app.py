from flask import Flask, render_template, request, redirect, url_for, g, flash
import sqlite3
import os

BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, 'database.db')

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DB_PATH)
        db.row_factory = sqlite3.Row
    return db

app = Flask(__name__)
app.secret_key = 'dev-secret-itla'

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    db = get_db()
    cur = db.execute('SELECT id, nombre, correo, nota FROM students ORDER BY id')
    students = cur.fetchall()
    return render_template('list.html', students=students)

@app.route('/create', methods=('GET','POST'))
def create():
    if request.method == 'POST':
        nombre = request.form.get('nombre','').strip()
        correo = request.form.get('correo','').strip()
        nota = request.form.get('nota','').strip()
        if not nombre:
            flash('El nombre es requerido.')
            return render_template('form.html', student={})
        db = get_db()
        db.execute('INSERT INTO students (nombre, correo, nota) VALUES (?, ?, ?)', (nombre, correo or None, nota or None))
        db.commit()
        flash('Estudiante creado.')
        return redirect(url_for('index'))
    return render_template('form.html', student={})

@app.route('/edit/<int:id>', methods=('GET','POST'))
def edit(id):
    db = get_db()
    cur = db.execute('SELECT id, nombre, correo, nota FROM students WHERE id=?', (id,))
    student = cur.fetchone()
    if not student:
        flash('Estudiante no encontrado.')
        return redirect(url_for('index'))
    if request.method == 'POST':
        nombre = request.form.get('nombre','').strip()
        correo = request.form.get('correo','').strip()
        nota = request.form.get('nota','').strip()
        if not nombre:
            flash('El nombre es requerido.')
            return render_template('form.html', student=student)
        db.execute('UPDATE students SET nombre=?, correo=?, nota=? WHERE id=?', (nombre, correo or None, nota or None, id))
        db.commit()
        flash('Estudiante actualizado.')
        return redirect(url_for('index'))
    return render_template('form.html', student=student)

@app.route('/delete/<int:id>', methods=('POST',))
def delete(id):
    db = get_db()
    db.execute('DELETE FROM students WHERE id=?', (id,))
    db.commit()
    flash('Estudiante eliminado.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    if not os.path.exists(DB_PATH):
        from db_init import init_db
        init_db(DB_PATH)
    app.run(debug=True, host='0.0.0.0', port=5000)
