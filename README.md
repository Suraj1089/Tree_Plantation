# Tree_Plantation
project for tree planting

# Installation

pip install django
python -m venv venv
pip install mysqlclient


# For Windows

GROW_GREEN->venv\scripts\activate

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate  # migrate the changes in model to database

python manage.py runserver #to run website in browser


GROW_GREEN/static/:-
put all required static material in folder present in GROW_GREEN/static/
and then use :

python manage.py collectstatic

templates:-
put all the required html templates in folder templates with proper names

*********************************************************************

update this document as you find something missing.