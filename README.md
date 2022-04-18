# mysite_0412

git clone https://github.com/g00u00/mysite_0412.git

cd mysite_0412

python3 -m venv env

. env/bin/activate

pip install -r requirements.txt

python manage.py runserver 10.0.2.15:8000

------------

pip freeze > requirements.txt

pip install -r requirements.txt
