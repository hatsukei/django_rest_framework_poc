# django_rest_framework_poc
This project is a poc for django framework and django rest framework simulating server inventory management with authentication for user access.

It includes :
* database for testing
* data models for database construction
* view creation
* serialization of data
* urls patterns creations
* authentication of users for access

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Here is a list of all the installation you need to do :
* Python 3
* pip (usually comes with python 3.4 and higher 
* cloning the project

### Setting up a new environment

For the project to work, we need to set up a django environment.
*Note: you can store this environment in either the project directory or your own env directory.*

open up a command line interface and write : 

```
virtualenv env
source env/bin/activate // "env\Scripts\activate" for Windows
```
this will activate (env) on your CLI.

*Note : you should be in the same directory when activating the env."*

Next, install these two framework to the environment :
```
pip install django
pip install djangorestframework
```
*Note : At any time, you can deactivate the environment by typing "deactivate"*

### Starting the Project

navigate to the django_rest_framework_poc > django_poc directory and start the project with this command :

```
python manage.py runserver
```
This will fire up the web app and the browser API can be access through 
the local address indicated on your CLI.

*Note : make sure you are in your env activation mode when you do this.*

### Here are the different API available as well as Login access.

**Access through Log in**

Username: admin
Password : password123

**Access to server inventory API**

your_local_url/serverinvent/

**Access to User API**

your_local_url/users/

**Managing Users**

your_local_url/admin/
