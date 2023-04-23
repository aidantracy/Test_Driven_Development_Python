# Test_Driven_Development_Python
This is a small project focused on test driven development in Python with Django. 

<!-- Setting up Django -->

Create and navigate to a folder named my_environments and run the appropriate commands to create a virtual environment and then install Django:

Create your environment:

------------------------------------------------------------------
| Mac/Linux: | python3 -m venv djangoPy3Env 
-------------+----------------------------------------------------
| Windows (command prompt): | python -m venv djangoPy3Env
>------------------------------------------------------------------

Activate your environment:

------------------------------------------------------------------
| Mac/Linux: | source djangoPy3Env/bin/activate                         
------------------------------------------------------------------
| Windows (command prompt): | call djangoPy3Env\Scripts\activate       
------------------------------------------------------------------
| Windows (git bash) : | source djangoPy3Env/Scripts/activate         
------------------------------------------------------------------

Install Django:

(djangoPy3Env) Windows/Mac:| pip install Django==2.2.4

<!-- ---------------------------------------------------------- -->
<!-- Creating a Django Folder Structure (MTV) -->

1. With our Django virtual environment activated, create a new Django project. First navigate to where you want the project to be saved (for these first few assignments, that will be the python_stack/django/django_intro folder). Then run this command, specifying a project name of our choosing:

> cd python_stack/django/django_intro
django_intro> django-admin startproject your_project_name_herecopy
Let's test this out:

Navigate into the folder that was just created. A new Django project has just been created--let's run it!

django_intro> cd your_project_name_here
your_project_name_here> python manage.py runserver
Open localhost:8000 in a browser window. Hooray for CLIs (command-line interfaces)!

(Don't worry about the warning about unapplied migrations. It won't affect us for now, and we'll address it soon enough.)

Press ctrl-c to stop the server. Open up the project folder in your text editor. (Take note of the folder structure so far!) We'll be updating some of these files shortly.

2. For every app we want to add to our project, we'll do the following:
2a. your_project_name_here> python manage.py startapp your_app_name_herecopy
The apps in a project CANNOT have the same name as the project.

2b. In the text editor, find the settings.py file. It should be in a folder with the same name as our project. Find the variable INSTALLED_APPS, and let's add our newly created app:

your_project_name_here/your_project_name_here/settings.py

   INSTALLED_APPS = [
       'your_app_name_here', # added this line. Don't forget the comma!!
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
   ]    # the trailing comma after the last item in a list, tuple, or dictionary is commonly accepted in Pythoncopy
   
2c. For these next few steps, we are creating the route "/" to be associated with a specific function. Trust for now--we'll break this down in greater detail in the next tab. In the urls.py file, add a URL pattern for your new app. (You can delete the current admin pattern, or just ignore it for now). You will need to add an import for your views file.

your_project_name_here/your_project_name_here/urls.py

from django.urls import path, include           # import include
# from django.contrib import admin              # comment out, or just delete
urlpatterns = [
    path('', include('your_app_name_here.urls')),	   
    # path('admin/', admin.sites.urls)         # comment out, or just delete
]

2d. Next, let's create a new urls.py file in the your_app_name_here folder. Put the following code

your_project_name_here/your_app_name_here/urls.py

from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	   
]

And then actually put a function called index in our app's views.py file:

your_project_name_here/your_app_name_here/views.py
from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")
    
3. Let's run our app again and check it out at localhost:8000/. Whew. We've done it!

your_project_name_here> python manage.py runservercopy

Note: Do not manually change the name of any of your folders after creation!

<!-- --------------------------------------------------------------------------------- -->

<!-- Example of how routing works -->

some_project/some_app/urls.py

urlpatterns = [
        path('bears', views.one_method),                        # would only match localhost:8000/bears
        path('bears/<int:my_val>', views.another_method),       # would match localhost:8000/bears/23
        path('bears/<str:name>/poke', views.yet_another),       # would match localhost:8000/bears/pooh/poke
    	path('<int:id>/<str:color>', views.one_more),           # would match localhost:8000/17/brown
]

The corresponding functions would then look like this:

some_project/some_app/views.py

def one_method(request):                # no values passed via URL
    pass                                
    
def another_method(request, my_val):	# my_val would be a number from the URL
    pass                                # given the example above, my_val would be 23
    
def yet_another(request, name):	        # name would be a string from the URL
    pass                                # given the example above, name would be 'pooh'
    
def one_more(request, id, color): 	# id would be a number, and color a string from the URL
    pass                                # given the example above, id would be 17 and color would be 'brown'

<!-- --------------------------------------------------------------------------------------------------------------------- -->


<!-- TO RUN APPLICATION -->
1. In Gitbash, make sure you are cd in the folder that contains the manage.py file. 
2. run command: python manage.py runserver    OR     python manage.py startapp your_app_name_here
This should be listening on http://localhost:8000/



