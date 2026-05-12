import axios from "axios";

const API_URL = window.location.hostname === 'yauhenibudzko.github.io' 
  ? process.env.REACT_APP_API_URL_PROD
  :  process.env.REACT_APP_API_URL_DEV;

export const fetchNotes = async () => {
  const response = await axios.get(`${API_URL}/notes`);
  return response.data;
};

export const addNote = async (title: string, description: string, createdAt: string) => {
  const response = await axios.post(`${API_URL}/notes`, { title, description, createdAt });
  return response.data;
};

export const deleteNote = async (noteId: string) => {
  const response = await axios.delete(`${API_URL}/notes/${noteId}`);
  return response.data;
};
