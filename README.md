# FYP_Prototype_Biometric_Authentication
This is a BSc ITMB Final Year Project Prototype, it is a functional biometric facial identification-based authentication system that recognises and tries to identify faces. 

In order to run a prototype, you must direct to the project folder on your terminal and ensure that all
Python and OpenCV packages are installed on your machine, please also refer to the Python scrypts for
any other modules or libraries that your machine might need to install (e.g. Pickle library).

Once that is done follow these steps on your terminal:

1. To run the prototype, enter on your terminal: "python app.py"
2. The local server will start and will be running on your machine. Go to the "localhost:5050" on your default browser.
3. You can start using the prototype! However, due to the model not being trained on your face, the system won't
recognize your face and will try to identify with other people's faces within the project folder 'images'.
4. To add your face to the local database, you mustr train the model. For that within 'images' folder create a folder
with your name and add 9 portrait photos of your face.
5. After the photos have been added to the folder named by your name in the 'images' folder, go to terminal and type:
"python faces-train.py" - after this is finished the system will have trained to recognize your face too.
6. To test that, on your terminal type: "python faceRecognitionTest.py", this will open the img window and will try
to identify you. If it doesn't better photos and more training is needed to improve the quality of identification.

It is important to mention that this is a prototype which is not linked to the authentication systems' backend
at the University of Manchester.

Enjoy!

Liutauras Mazonas Copyright, 2020 04 24, Manchester
