### Instruction of Group 1 UYP Project
##### Yunzhe Liu / Calvin Tse / Fu Bo
#### github repo: https://github.com/Haizhepi/CompSci3335
#### Python 3.6 or above & virtual environment 
#### Django 1.9.9 
#### mysqlclient
#### django-import-export
#### django-bootstrap3
#### django-crispy-form
### The replacement of logical SQL schema
The django framework uses ORM to replace the SQL statements that creates the table, the class is in the models.py
of each directory, the django uses makemigrations [appname] to create and modify the tables in database and migrate 
command to set up the database

### How to install packages
##### All of the following software is free
pip3 install Django==1.9.9  
pip3 install mysqlclient  
pip3 install django-bootstrap3  
pip3 install django-import-export  
pip3 install django-bootstrap3  
pip3 install django-crispy-form  
### How to start the project
1: in learning_site.settings.py, change the DATABASES dictionary default to the mysql database name and password  
2: in root directory, run:  
    python manage.py makemigrations  
    python manage.py migrate  
    python manage.py runserver  
    go to the url it provides to access the website  
3: The admin page have no entry button on any pages, must type in /admin to access  
4: To create super user:  python manage.py createsuperuser  
   



 