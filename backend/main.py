from fastapi import FastAPI, HTTPException, status
from bson import ObjectId
import pymongo
from pymongo import MongoClient
from pymongo.mongo_client import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure, PyMongoError
from pymongo.server_api import ServerApi
from models import Note 
import certifi
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv 
from typing import List
from datetime import datetime


load_dotenv()

app = FastAPI()

MONGODB_URI = os.getenv("MONGODB_URI")#"mongodb+srv://yauhenibudzko:pGh8YjGcCo9u2Qp3@cluster-notes.pcpzzww.mongodb.net/?retryWrites=true&w=majority&appName=Cluster-notes"

client = MongoClient(MONGODB_URI, tlsCAFile=certifi.where())
db = client["notes_db"]
collection = db["notes"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yauhenibudzko.github.io",
                   "http://localhost:3000",
                   "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def note_serializer(note) -> dict:
    try:
        return {
            "id": str(note["_id"]),
            "title": note["title"],
            "description": note["description"],
            "createdAt": note["createdAt"]
        }
    except KeyError as e:
        raise ValueError(f"Missing field: {str(e)}")

@app.get("/", status_code=status.HTTP_200_OK)
async def root():
    return {"status": "ok", "message": "Notes API is running"}

@app.get("/notes", response_model=List[dict])
async def get_notes():
    try:
        notes = collection.find()
        return [note_serializer(note) for note in notes]
    except PyMongoError as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Database: {str(e)}"
        )

@app.post("/notes", status_code=status.HTTP_201_CREATED)
async def add_note(note: Note):
    try:
        note_data = note.dict()   
        result = collection.insert_one(note_data)
        return {
            "id": str(result.inserted_id),
            "createdAt": note_data['createdAt'],
            "message": "Note added successfully"
        }
    except OperationFailure as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Database operation failed: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Unexpected error: {str(e)}"
        )

@app.delete("/notes/{note_id}", status_code=status.HTTP_200_OK)
async def delete_note(note_id: str):
    try:
        if not ObjectId.is_valid(note_id):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid note ID format"
            )
        result = collection.delete_one({"_id": ObjectId(note_id)})
        if result.deleted_count == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Note not found"
            ) 
        return {"message": "Note deleted successfully"}
    except PyMongoError as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Database error: {str(e)}"
        )
