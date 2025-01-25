# Live Face Detection and Recognition System
This project is a face detection and recognition system built using Python and OpenCV. It captures face images from a webcam, trains a face recognizer using the Local Binary Patterns Histogram (LBPH) algorithm, and saves the trained model for future use.

# Features
**.**Detects faces in real-time using a webcam and draws bounding boxes around detected faces.
**.**Captures face images and saves them in a labeled dataset (dataset folder).
**.**Extracts user IDs from image filenames and trains an LBPH face recognizer.
**.**Saves the trained model as trainingdata.yml for efficient recognition.

# Technologies Used
**.**Python: Core programming language.
**.**OpenCV: For face detection and recognition.
**.**NumPy: For array operations.

# How It Works
**.** Face Data Collection: Uses Haar cascade classifier (haarcascade_frontalface_default.xml) to detect faces from the webcam.
**.**Captures 20 grayscale images of each user and saves them in the dataset folder.

# Training the Recognizer:
**.**Reads the saved images from the dataset.
**.**Extracts user IDs from filenames (e.g., user.ID.xxx.jpg).
**.**Trains the LBPH face recognizer using these images and IDs.

# Saving the Model:
**.**Saves the trained model as recognizer/trainingdata.yml for future recognition tasks.


Feel free to use or improve this project! 😊
