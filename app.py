from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import credentials, db, storage
import numpy as np
import cv2
import base64

app = Flask(__name__)

# Initialize Firebase Admin SDK
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "",
    'storageBucket': ""
})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_student', methods=['POST'])
def add_student():
    student_id = request.form['student_id']
    name = request.form['name']
    major = request.form['major']
    starting_year = request.form['starting_year']
    standing = request.form['standing']
    year = request.form['year']
    last_attendance_time = request.form['last_attendance_time']

    ref = db.reference(f'Students/{student_id}')
    ref.set({
        'id': student_id,
        'name': name,
        'major': major,
        'starting_year': starting_year,
        'total_attendance': 0,
        'standing': standing,
        'year': year,
        'last_attendance_time': last_attendance_time
    })

    return render_template('index.html', message="Student added successfully!")

@app.route('/search', methods=['POST'])
def search():
    student_id = request.form['student_id']
    ref = db.reference(f'Students/{student_id}')
    student_info = ref.get()

    if student_info:
        bucket = storage.bucket()
        blob = bucket.blob(f'Images/{student_id}.png')
        img_array = np.frombuffer(blob.download_as_string(), np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        _, buffer = cv2.imencode('.png', img)
        img_str = base64.b64encode(buffer).decode('utf-8')
        return render_template('index.html', student_info=student_info, img_str=img_str)
    else:
        error = "Student ID not found"
        return render_template('index.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
rahi vapis