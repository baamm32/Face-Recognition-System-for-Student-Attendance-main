import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("Face-Recognition-System-for-Student-Attendance-main/serviceAccountKey.json")
firebase_admin.initialize_app(
    cred,
    {
        "databaseURL": "https://faceattendacerealtime-6254e-default-rtdb.firebaseio.com/",
        # database URL
    },
)

ref = db.reference(
    "Students"
)  # reference path to our database... will create student directory in the database

data = {
    "004223": {  # id of student which is a key
        "id": "004223",
        "name": "Kim Companero",
        "password": "004223Kim",
        "dob": "2000-11-01",
        "address": "Bpook, Laguna",
        "phone": "09876543219",
        "email": "kimcompanero@gmail.com",
        "major": "Information Technology",
        "starting_year": 2020,
        "standing": "G",
        "total_attendance": 4,
        "year": 4,
        "last_attendance_time": "2023-11-04 12:33:10",
        "content": "This section aims to offer essential guidance for students to successfully complete the course. It will be regularly updated \
                to ensure its relevance and usefulness. Stay tuned for valuable \
                insights and tips that will help you excel in your studies.",
    },
}


for key, value in data.items():
    ref.child(key).set(value)
