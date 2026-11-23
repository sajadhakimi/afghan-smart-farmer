Clone the GitHub repository.

Open the project folder and enter the backend directory.

Create a Python virtual environment:
python -m venv venv

Activate it:
.\venv\Scripts\Activate.ps1

Install dependencies:
pip install -r requirements.txt

Copy .env.example to .env:
Copy-Item .env.example .env

Add the Supabase Project URL and Publishable key to .env.

Test the connection:
python test_supabase.py

Run the backend:
uvicorn app.main:app --reload

Then open http://127.0.0.1:8000/docs to see the API.

Remember, do not push your .env file to GitHub.