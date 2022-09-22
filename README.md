# Assignment Documentation
## About
This readme file contains the documentation for the project submission of a simple web application assignment given as part of the recruitment process.
The web aplication allows authentication and keep track of users(customer), allows users to send HTTP request to place order for available products, allow users edit provided informations like password, First name and Last name, and simulate a payment process to make payments for orders and generate unique reference Number for each payment. Also provides an Admin user(Super User) the ability to view all Payment Records and all Order Records.

## Note:
This project focus on supplying APIs needed for the backend functionality of the project, with basic frotend pages designed and  used to visualized how the whole process work, little attention was placed on the frontend design and All contents are Arbitrary.

### Install Dependencies


1. **Python 3.10** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

- Python 3.10 upward is required

2. **Virtual Environment** - I recommend working within a virtual environment whenever using Python for projects, in order to keep the dependency separate and well organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Activate the virtual enviromen and install dependencies using the following commands:

- **Start and activate your virtual environment**


```bash
# Mac and Linux users

python3 -m venv env
source env/bin/activate

# Windows users
> py -3 -m venv env
> env\Scripts\activate

# Windows git bash users
python3 -m venv env
source env/bin/activate
```

Run This command to install the required project dependencies e.g Django. All the dependecies used have been pip freezed into the requirements.txt file which is located at the base of the project

```bash
pip install -r requirements.txt
```

### Database

for this test assesment, the default sqlite database that come preinstalled with django was used due to the light weight of the project. In bigger projects, more bigger database like MySQL or Postgress SQL will be used for relational database
### Database Schema:
The database schedule can be accessed via the link below or in the schema.png file in the root directory of the project
```bash
https://dbdiagram.io/d/632c4cf07b3d2034ff8c6bb5
```
make migrations with
```bash
python manage.py makemigrations
```
 and migrate with
```bash
python manage.py migrate
```



### Run the Server

After successfully setting up and installing the dependencies and setting up the Database start your backend Django server by running the command below from the `Data2bots_assesment` directory.

```bash
python manage.py runserver
```
This will start the development server which can be accessed at http://127.0.0.1:8000/ or http://localhost:8000/
### API Usage
The project has been done with little improvised frotend to practicalize how the API calls can be made with the proper URL Routing. The Views for the Authentication and the urls are located in the auth apploication.

Social login couldn't be used in the project simple because it will require the input of secret details which if kept in a virtual enviroment, wint be made available outside my local machine for others to use.


For each http response to requests, the conventional correspomding status code is returned. such as:
200 for success
302 for redirect
404 for not found
500 for server error

### Reserved Calls

Only a superuser account is allowed to maake a post request creating product, and a get request to view all payments history and order history. As this mimick the activity of he Admin staff of the Client's company

To create a super user account please use the following code on your terminal and input the needed information

```bash
python manage.py createsuperuser
```
A super user account is needed from start to provide Products to display for users as none has been hardcoded expect a default picture for the products
### Testing

the project consists of two apps, authz for authentication and business for everyother thing outside authentication. To run the test on the two apps together, use the command below:

```bash
python manage.py test authz business
```
To run test on the business app only, use:

```bash
python manage.py test business
```
to run test on the authz app only, use:
```bash
python manage.py test authz
```

### Commenting
Comments are provided within the projects to explain the thought process without over-loading