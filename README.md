# AI Data Cleaning & Preprocessing Environment

This project simulates a real-world data cleaning environment using FastAPI.  
It is designed to mimic how data is cleaned step by step in practical scenarios.

## Features
- Reset the environment
- Perform cleaning actions (like handling missing values and duplicates)
- Track state changes
- Step-based environment simulation

## API Endpoints
- GET / → Home
- GET /reset → Reset environment
- POST /step → Perform action
- GET /state → Get current state

## How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Run the server:
uvicorn app:app --reload

3. Open in browser:
http://127.0.0.1:8000/docs

## Project Structure
- app.py → FastAPI app
- envs/ → environment logic
- requirements.txt → dependencies
- openenv.yaml → environment
