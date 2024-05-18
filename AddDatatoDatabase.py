import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': ""
})

ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Abhay Pandey",
            "major": "AI-DS",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Virat Kohli",
            "major": "Cricketer",
            "starting_year": 2007,
            "total_attendance": 0,
            "standing": "B",
            "year": 17,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2015,
            "total_attendance": 0,
            "standing": "G",
            "year": 9,
            "last_attendance_time": "2022-12-11 00:54:34"
        },

    "123456":
        {
            "name": "Prashant Chaudhary",
            "major": "AI-DS",
            "starting_year": 2018,
            "total_attendance": 0,
            "standing": "G",
            "year": 8,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "007":
        {
            "name": "Cristiano Ronaldo",
            "major": "Football",
            "starting_year": 2005,
            "total_attendance": 0,
            "standing": "G",
            "year": 19,
            "last_attendance_time": "2022-12-11 00:54:34"
        }

}

for key, value in data.items():
    ref.child(key).set(value)