<!-- {% if False %} -->

# Temp-o-Rent

# Introduction

A Palestinian car rental website that connects renting agencies with users that wants to
rent cars , At any time of the year this website offers endless possibilities, of enjoyment
to travel with a rental car , With this website you can compare deals across 11 cities in west
bank.

![Default Home View](img/main.png?raw=true "Main Page")
![Default Home View](img/2.png?raw=true "#2 Page")
![Default Home View](img/3.png?raw=true "#3 Page")
![Default Home View](img/4.png?raw=true "#4 Page")
![Default Home View](img/5.png?raw=true "#5 Page")
![Default Home View](img/7.png?raw=true "#6 Page")
![Default Home View](img/9.png?raw=true "#7 Page")

### Main features

* Searsh Form in Main Page to filter Cars

* Responsive Design

* Bootstrap static files included

* User registration and logging in

* Car details and reserve time

* Separated requirements files

* About us page for more details about the website

# Usage

A~~~~~~~~~~~~~~~~~~~~~~~~A

### Existing virtualenv

If your project is already in an existing python3 virtualenv first install django by running

    $ pip install django
    
And then run the `django-admin.py` command to start the new project:

    $ django-admin.py startproject \
      --template=https://github.com/AwsRadwan/django-template/zipball/master \
      --extension=py,md \
      <project_name>
      
### No virtualenv

This assumes that `python3` is linked to valid installation of python 3 and that `pip` is installed and `pip3`is valid
for installing python 3 packages.

Installing inside virtualenv is recommended, however you can start your project without virtualenv too.

If you don't have django installed for python 3 then run:

    $ pip3 install django
    
And then:

    $ python3 -m django startproject \
      --template=https://github.com/AwsRadwan/django-template/zipball/master \
      --extension=py,md \
      <project_name>
      
      
After that just install the local dependencies, run migrations, and start the server.

{% endif %}

#  Temp-o-Rent | Car Rentals 

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/USERNAME/{{ project_name }}.git
    $ cd {{ project_name }}
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements/local.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver
