DJANGOLIFE-

is a simple video store project.This project keep a list of video and embed code.Any user can be create and login..Etc
In this project django beginners tropics was covered and django restframework basic also covered.

Installation :

     1--> Install python in your operating system. 
     Setup your project virtual environment. 
     Clone the project in your project directory.
     
     2--> Activate virtual environment and install the requirements.txt file using : 
     pip install -r requirements.txt   
     
     3--> Install and setup database Mysql. Change your settings.py file something like that :
     
     DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangolife',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
     }
    }

     4--> After that you have to makemigrations and migrate.Then run..
    * python manage.py makemigrations
    * python manage.py migrate
    * python manage.py runserver
    * open your browser and enter the url : http://127.0.0.1:8000/ and hit enter..that's all.


     Note : If you will get any import error then install it using pip..
            For windows users--install xamp or wamp server, create a database for your django project and edit settings.py file. 
            You have to need a databse connector(it's may be 'mysql-client') installation for python.But in requirements.txt file it is already included.
            Enjoy this project.Thank's
