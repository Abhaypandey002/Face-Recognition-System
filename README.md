# Face-Recognition-System
The Student Face Recognition System is a comprehensive application designed to manage student records using facial recognition technology. 

# intall requirements.txt
# Image in folder Images should be of size 216x216 and in PNG form only.
# Steps to Run the Student Face Recognition System

1. Setup Firebase Realtime Database
   - Create a Firebase project.
   - Set up a Realtime Database.
   - Copy the Realtime Database URL and paste it into `databaseURL=""` in the configuration file.

2. Setup Firebase Storage Bucket
   - Create a Firebase Storage Bucket within your project.
   - Copy the Storage Bucket URL and paste it into `storageBucket=""` in the configuration file.

3. Download Firebase Secret Key 
   - Download the Firebase secret key JSON file from your project settings.
   - Place this secret key file (serviceAccountKey.json) in the project folder.

4. Add Student Data in AdddatatoDatabase file
   - Run `AddDatatoDatabase.py` to add initial student data to the Firebase database.

5. Generate Encoded Face Data(Run the EncodeGenrator.py)
   - Run `EncodeGenerator.py` to create the `EncodeFile.p` file which contains the encoded face data.

6. Start the Main Application
   - Run `main.py` to start the face recognition system.

7. Operate the Application
   - For adding new students and searching for existing students, run `app.py` in the terminal.
   - Use the terminal interface to interact with the system.

By following these steps, you will set up and run the Student Face Recognition System successfully.
