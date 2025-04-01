# Movie Management Platform

## Overview
This project is a **user-friendly movie management platform** designed for efficient **movie cataloging and retrieval**. It provides seamless integration between the **frontend (Streamlit UI)** and **backend (FastAPI, Python, and MySQL)** to handle large movie datasets efficiently.

## Features
- **Movie Cataloging:** Add, update, and delete movies from the database.
- **Fast Retrieval:** Optimized queries for quick search and filtering.
- **Scalable Architecture:** Handles large datasets smoothly.
- **API Integration:** FastAPI ensures seamless communication between UI and backend.
- **User-Friendly UI:** Built with Streamlit for easy interaction.

## Tech Stack
- **Frontend:** Streamlit (UI)
- **Backend API:** FastAPI
- **Business Logic & Data Processing:** Python
- **Database:** MySQL

## Installation
### Prerequisites
Ensure you have the following installed:
- Python (>=3.8)
- MySQL
- pip (Python package manager)
- Docker (optional for containerized deployment)

### Setup
1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/movie-management-platform.git
   cd movie-management-platform
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up the MySQL database:**
   - Create a new database:
     ```sql
     CREATE DATABASE movie_db;
     ```
   - Update `config.py` with your MySQL credentials.
   - Run migrations (if applicable).

4. **Run the FastAPI backend:**
   ```sh
   uvicorn api:app --reload
   ```

5. **Run the Streamlit UI:**
   ```sh
   streamlit run app.py
   ```

## API Documentation
Once the FastAPI server is running, access the API docs at:
- **Swagger UI:** `http://127.0.0.1:8000/docs`
- **ReDoc:** `http://127.0.0.1:8000/redoc`

## Deployment
### Using Docker
1. **Build the Docker image:**
   ```sh
   docker build -t movie-management .
   ```
2. **Run the container:**
   ```sh
   docker run -p 8000:8000 movie-management
   ```

### Manual Deployment
- Deploy FastAPI on a cloud server (AWS, GCP, DigitalOcean, etc.).
- Use MySQL hosting services for database management.
- Deploy Streamlit UI using Streamlit Sharing or other hosting options.



