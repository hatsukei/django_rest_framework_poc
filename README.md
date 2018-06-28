
# Server Inventory Management 

## Description

This project is a server inventory management webapp with a secure administration zone.
The server exposes a web service  with a REST architecture using Django REST Framework.

It includes :
* database for testing
* data models for database construction
* view creation
* serialization of data
* urls pattern creations
* authentication of users for access

## API List


With this project, you will be able to list , add, change or delete servers. It will also be possible to list users for testing purpose!

Here is the API List :
```
serverinvent: {
        list([page])
        create([server_name], [domain_name], [ip_address], [location], [operating_system], [status])
        read(id)
        update(id, [server_name], [domain_name], [ip_address], [location], [operating_system], [status])
        partial_update(id, [server_name], [domain_name], [ip_address], [location], [operating_system], [status])
        delete(id)
    }
```
There is two ways to test and check the api :

The first way is to use the command line client CoreAPI.
The second way is by browser. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Here is a list of all the installations you need to do :
* Python 3
* pip (usually comes with python 3.4 and higher )
* cloning the project

### Cloning the repo

Now that you are ready to get started, let's clone this repository to get up and running!

To clone this repository, you will need to have git on your machine. If you don't have it , I recommend going to this website and installing it : https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

Now that it is installed, head to a directory where you want to clone this repository with your command line interface and type :

```
git clone https://github.com/starlion10/django_rest_framework_poc.git
```
A folder django_rest_framework_poc should appear in your directory.
Next, we will set up an environment for the project to work.

### Setting up a new environment

For the project to work, we need to set up a django environment.
*Note: you can store this environment in either the project directory or your own env directory.*


open up a command line interface and write : 

```
pip install virtualenv
virtualenv env
source env/bin/activate  # use "env\Scripts\activate" instead for Windows
```
this will activate (env) on your CLI.

*Note : you should be in the same directory when activating the env."*

Next, install these two frameworks to the environment :
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
This will fire up the web app and the browser API can be accessed through 
the local address indicated on your CLI.

*Note : make sure you are in your env activation mode when you do this.*


## Using a simple command line client to use the API

We will use CoreAPI which is a simple command line client to use the API

Simply install it with this command : 

```
pip install coreapi-cli
```
And you are ready to go !

### Authenticating

Since this project include a secure administration zone, you will need to authenticate yourself.
```
coreapi credentials add 127.0.0.1 admin:password123 --auth basic
coreapi reload
```
The reload commands will reload the coreapi to recognize the credentials you just add.

*Note: Here, I use 127.0.0.1 since it is the URL my server is giving me. Please do change it to you URL.*

### Loading a Schema

coreapi uses a schema to be able to interact with an API so you need it load it by typing this in ur command line client:
```
coreapi get http://127.0.0.1:8000/schema/
```
### Listing of the servers

Now that you have loaded the schema. Let's start diving into the API!

For the listing type this command : 
```
coreapi get http://127.0.0.1:8000/serverinvent/
```

### Adding a server

to add a server, there is many info that can be added. But for the sake of this tutorial. Simply add a server name and a location with this command :
```
coreapi action serverinvent create --param server_name="Example_db" --param location="Montreal"
```
To see if you have added your server correctly, Head back to the listing and you will see your new server added correctly.

### Changing a server

To update of change a server info, you need to specify the id number of the server. In my case, it is the id number 7 for the example I just created in the "Adding a server" section.
```
coreapi action serverinvent update --param id=7 --param server_name="example_db_99"
```
### Deleting a server

To delete a server, simply point to the right id with this command :
```
coreapi action serverinvent delete --param id=7
```
Check your listing again to verify if your command work!

## Using the API with Browser

### Authentication 

Since this project include a secure administration zone, you will need to authenticate yourself.

Head to the "log in" in your browser and enter these credentials :

```
Username: admin
Password : password123
```

### Listing Servers

*Make sure your server is running on your machine with the 'python manage.py runserver' command*

Fire up your favorite browser and enter the following URL, that you see on your command line interface after running the runserver command.
It will look like something like this : "Starting development server at http://127.0.0.1:8000/"

To open up the server list, head to the url and add '/serverinvent/ to your url.
It should look like this 
```
http://127.0.0.1:8000/serverinvent/
```
This should let you see a list of the servers I created.

if you encounter this : 

```
"detail": "Authentication credentials were not provided."
```
Don't worry, it only means you need to access the api through a user since this project include a secure administration zone.

Head down to the section " Authentication " and follow the log in instruction then come back up.

### Adding a Server

To add a server is fairly easy using your browser. 
Head to the list of the servers as described in the section "listing a server" above.

Then scroll down the page and you should see an empty Html form to fill.
Fill it with whatever you want and click POST.

Head back to the server list and it should be there.

### Change a Server

To change a server, you need to head to the list of server and find the servers you want to delete.

When you find the one you want to change, take his 'id' number and put it in your url. 

Your URL should look like this : 
```
http://127.0.0.1:8000/serverinvent/3
```
with 3 being the number of the id of the server you want to change. 

On this page, you can just head down and changes the info of the server and click on the 'PUT' button and it will be changed.

### Delete a server

Deleting a server is the same as changing a server.

Head to the URL of the server you want to delete and just as the section "Change a Server" take the id number and put it in your URL.

Then click on the red 'DELETE' button and this should do delete your server.
