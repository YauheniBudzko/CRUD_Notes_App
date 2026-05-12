# CRUD Notes App
![NotesAppLogo](/Docs/NotesApp.png)

## A web notes application, where you can create, access and delete notes. Made as a recruitment task

## Project description

**Tech Stack:** TypeScript · React · FastAPI · MongoDB · Jotai · Material UI

This project was created as part of a recruitment task and includes the following technologies and characteristics:
* Language:  TypeScript
* Frontend: React.js
* Backend: Python(FatsAPI framework)
* Database:  MongoDB
* Tools:  Jotai(state management),  Material-UI(UI)

## Project features
In this app you can:
* Read notes
* Create notes with title and description(createdAt attribute is added automatically) - after button "Add note" is pressed, the note is added to the notes list
* Delete notes - after button "Delete" is pressed, the note is deleted from the notes list

![demonstration](/Docs/demonstration.gif)

## Application deployment
The application's parts are deployed separately: 
- The database is on MongoDB Atlas 
- The backend is deployed on render.com 
- The frontend is deployed on GitHub Pages

## Installation and testing the app locally
Here are the steps for local testing of the application:
- Clone the project:
```bash
git clone https://github.com/Jackychan0201/CRUD_notes_app.git
```
- Navigate to the project directory:
```bash
cd CRUD_notes_app
```
- Navigate to the backend directory:
```bash
cd backend
```
- Set the environment variable:
    - create a .env file inside the backend directory:
    ```bash
    touch .env
    ```
    - insert there MongoDB URI and save the file. The example of the .env file is .env.example
- Install the requirements from the file requirements.txt
```bash
pip install -r requirements.txt
```
- Start the backend:
```bash
uvicorn main:app --reload
```
>[!NOTE]
>
>backend is running on http://127.0.0.1:8000
- Navigate to the frontend directory:
```bash
cd ../frontend
```
- Set the environment variables:
    - create a .env file inside the frontend directory:
    ```bash
    touch .env
    ```
    - insert there the React App API URLs and save the file. The example of the .env file is .env.example
- Install necessary dependencies:
```bash
npm install
```
- Start the frontend:
```bash
npm start
```
>[!NOTE]
>
>After you complete all these steps, you'll be able to access the application via http://localhost:3000/CRUD

## Deployed application
The application is already deployed. You can access it via:
https://yauhenibudzko.github.io/CRUD/
>[!WARNING]
>
>Since the free tier version of Render is used for the backend deployment, the backend might be inactive during the test. If this problem occurs, please feel free to contact me, I will restart the backend.

## Found a bug?
If you found an issue while testing the app or you would like to submit an improvement for the project, I encourage you to contact me via my email: zheniabudko@gmail.com

## Author

Created by Yauheni Budzko
