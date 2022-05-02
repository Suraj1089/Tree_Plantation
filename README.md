# Tree_Plantation<br>
project for tree planting<br>

# Installation<br>

pip install django<br>
python -m venv venv<br>
pip install mysqlclient<br>


# For Windows<br>

GROW_GREEN->venv\scripts\activate<br>

pip install -r requirements.txt<br>

python manage.py makemigrations<br>

python manage.py migrate  # migrate the changes in model to database<br>

python manage.py runserver #to run website in browser<br>


GROW_GREEN/static/:-<br>
put all required static material in folder present in GROW_GREEN/static/<br>
and then use :<br>

python manage.py collectstatic<br>

templates:-<br>
put all the required html templates in folder templates with proper names<br>

*********************************************************************<br>

update this document as you find something missing.<br>


# INSTRUCTIONS TO CREATE DATABASE AND SETUP<br>
--create database with name "grow_green"<br>
--downlaod mysqlclient in project(pip install mysqlclient)<br>
--go to django project and setup (DATABASES) in setting.py <br>
--use python manage.py makemigration &<br>
--python manage.py migrate <br>
--comands to fetch changes/tables in your database<br>
--use show tables comand to display tables<br>