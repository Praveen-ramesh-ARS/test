Weather Prediction 
## 🔍 Description
A Django-based weather prediction app using a machine learning model and OpenWeather API.

## 💡 Features
- Input a city and receive current weather
- ML model predicts weather condition (e.g. Rain Likely, Sunny)
- Logs each prediction to the database
- Deployable to Render.com

1️⃣ Project Setup

django-admin startproject project_name
cd project_name
python manage.py startapp app_name

2️⃣ Database & Migrations

python manage.py makemigrations
python manage.py migrate

3️⃣ Superuser Creation
python manage.py createsuperuser

Create a proper ML model and save it
Create a file called: create_model.py inside predictions/
Run the script
Run it from your terminal:
python predictions/create_model.py
This will create a valid model.pkl file.

4️⃣ Running Server (Local)
python manage.py runserver

5️⃣ Static Files (Before Deployment)
python manage.py collectstatic

6️⃣ Requirements File (For Deployment)
pip freeze > requirements.txt

7️⃣ Git & Deployment Commands
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin your_repo_url
git push -u origin main

8️⃣ Render/Deployment Extras
Install WhiteNoise
pip install whitenoise

Update settings.py with
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]
