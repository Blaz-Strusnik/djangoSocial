### djangoSocial

Simple setup for the Django social media project.

### Clone the repo:

git clone https://github.com/Blaz-Strusnik/djangoSocial.git  
cd djangoSocial

### Create and activate a virtual environment:

python -m venv venv  
source venv/bin/activate  
On Windows use: venv\Scripts\activate  

### Install dependencies:

pip install -r requirements.txt

### Run migrations and start server:

python manage.py migrate  
python manage.py runserver  
Visit http://127.0.0.1:8000 in your browser.  
