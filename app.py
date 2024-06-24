from flask import Flask, render_template, request, redirect, url_for
import firebase_admin
from firebase_admin import credentials, db, storage
import os
import cv2
import base64
import numpy as np

app = Flask(__name__)

# Initialize Firebase Admin SDK
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-3ed7a-default-rtdb.firebaseio.com/",
    'storageBucket': "faceattendancerealtime-3ed7a.appspot.com"
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

    # Handling the image upload
    if 'image' not in request.files:
        return "No file part"
    file = request.files['image']
    if file.filename == '':
        return "No selected file"
    if file:
        # Save the file to the Images directory
        image_dir = os.path.join(os.getcwd(), 'Images')
        if not os.path.exists(image_dir):
            os.makedirs(image_dir)
        file_path = os.path.join(image_dir, f'{student_id}.png')
        file.save(file_path)

        # Resize the image to 216x216
        img = cv2.imread(file_path)
        img_resized = cv2.resize(img, (216, 216))
        cv2.imwrite(file_path, img_resized)

        # Upload the file to Firebase Storage
        bucket = storage.bucket()
        blob = bucket.blob(f'Images/{student_id}.png')
        blob.upload_from_filename(file_path)

    # Save student data to Firebase Database
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
        return render_template('index.html', error="Student not found")

if __name__ == '__main__':
    app.run(debug=True)
