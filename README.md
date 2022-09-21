# Data2Bots_assesment

## Setting up the Backend

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

Run This command to install the required project dependencies e.g Django

```bash
pip install -r requirements.txt
```


### Set up the Database

for this text assesment, the default sqlite database that come preinstalled with django was used due to the light weight of the project. In bigger projects, more bigger database like MySQL or Postgress SQL will be used for relational database

```bash
python manage.py migrate
python makemigrations metadata
```

### Run the Server

After successfully setting up and installing the dependencies and setting up the Database start your backend Django server by running the command below from the `Data2bots_assesment` directory.

```bash
python manage.py runserver
```
### Run the Server

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
