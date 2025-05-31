import random
import sqlite3
import io
import qrcode
from flask import Flask, redirect, render_template, request, jsonify, send_file
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

app = Flask(__name__, template_folder='templates')

def randomString(length=6):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    while True:
        result_str = ''.join(random.choice(letters) for i in range(length))
        db = sqlite3.connect('data.db')
        cursor = db.cursor()
        cursor.execute('SELECT shorturl FROM urls WHERE shorturl = ?', (result_str,))
        existing_url = cursor.fetchone()
        if not existing_url:
            return result_str

def get_db():
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    shorturl = None
    feedback_error = None
    feedback_success = None

    if request.method == 'POST':
        if 'longurl' in request.form:
            longurl = request.form.get('longurl')
            if longurl == '':
                error = 'Please enter a URL'
            else:
                db = get_db()
                cursor = db.cursor()
                cursor.execute('CREATE TABLE IF NOT EXISTS urls (id INTEGER PRIMARY KEY, longurl TEXT, shorturl TEXT UNIQUE)')
                cursor.execute('SELECT shorturl FROM urls WHERE longurl = ?', (longurl,))
                result = cursor.fetchone()

                if result:
                    shorturl = result['shorturl']
                else:
                    shorturl = randomString(6)
                    cursor.execute('INSERT INTO urls (longurl, shorturl) VALUES (?, ?)', (longurl, shorturl))
                    db.commit()

        elif 'feedback' in request.form:
            user_feedback = request.form.get('feedback', '').strip()
            if not user_feedback:
                feedback_error = "Feedback cannot be empty."
            else:
                db = get_db()
                cursor = db.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS feedback (
                        id INTEGER PRIMARY KEY,
                        message TEXT NOT NULL
                    )
                ''')
                cursor.execute('INSERT INTO feedback (message) VALUES (?)', (user_feedback,))
                db.commit()
                feedback_success = True

    return render_template('index.html',
                           error=error,
                           shorturl=shorturl,
                           host=request.host_url,
                           feedback_error=feedback_error,
                           feedback_success=feedback_success
                          )

@app.route('/<shorturl>')
def redirect_shorturl(shorturl):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT longurl FROM urls WHERE shorturl = ?', (shorturl,))
    result = cursor.fetchone()
    if result:
        return redirect(result['longurl'])
    else:
        return "URL does not exist"

@app.route('/dashboard')
def dashboard():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT id, longurl, shorturl FROM urls')
    urls = cursor.fetchall()
    host = request.host_url
    return render_template('dashboard.html', urls=urls, host=host)

@app.route('/edit/<int:id>', methods=['POST'])
def edit_url(id):
    data = request.get_json()
    new_longurl = data.get('original_url')
    if not new_longurl:
        return jsonify({'error': 'URL is required'}), 400
    db = get_db()
    cursor = db.cursor()
    cursor.execute('UPDATE urls SET longurl = ? WHERE id = ?', (new_longurl, id))
    db.commit()
    return jsonify({'success': True})

@app.route('/delete/<int:id>', methods=['POST'])
def delete_url(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('DELETE FROM urls WHERE id = ?', (id,))
    db.commit()
    return jsonify({'success': True})

@app.route('/qr/<shorturl>')
def qr_code(shorturl):
    qr_data = request.host_url + shorturl
    qr = qrcode.make(qr_data)
    buffer = io.BytesIO()
    qr.save(buffer, format="PNG")
    buffer.seek(0)
    return send_file(buffer, mimetype='image/png')

@app.route('/export/pdf')
def export_pdf():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT longurl, shorturl FROM urls')
    urls = cursor.fetchall()

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    y = height - 50
    p.setFont("Helvetica", 12)
    p.drawString(50, y, "URL Shortener Dashboard Export")
    y -= 30

    for url in urls:
        line = f"Original: {url['longurl']}  |  Short: {request.host_url}{url['shorturl']}"
        p.drawString(50, y, line)
        y -= 20
        if y < 50:
            p.showPage()
            y = height - 50

    p.save()
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name="url_dashboard.pdf", mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True)
