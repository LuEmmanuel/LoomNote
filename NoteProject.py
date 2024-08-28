from flask import Flask, render_template, request, redirect, url_for
import sqlite3

# Create a Flask application instance
app = Flask(__name__)

# Build the database
def create_database():
    conn = sqlite3.connect('loggedData.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS notes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    note TEXT NOT NULL)''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        note = request.form.get('note')
        if note:
            conn = sqlite3.connect('loggedData.db')
            c = conn.cursor()
            c.execute('INSERT INTO notes (note) VALUES (?)', (note,))
            conn.commit()
            conn.close()
            # Redirect after processing the POST request to avoid form resubmission
            return redirect(url_for('index'))

    conn = sqlite3.connect('loggedData.db')
    c = conn.cursor()
    c.execute('SELECT * FROM notes')
    notes = c.fetchall()
    conn.close()

    return render_template('index.html', notes=notes)

@app.route('/delete/<int:note_id>')
def delete(note_id):
    conn = sqlite3.connect('loggedData.db')
    c = conn.cursor()
    c.execute('DELETE FROM notes WHERE id = ?', (note_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == "__main__":
    create_database()
    app.run(debug=True)