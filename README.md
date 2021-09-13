# Netflix-Backend-Django
## Set up on local machine

1. The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/chetan6780/Netflix-Backend-Django.git
$ cd Netflix-Backend-Django
```

2. Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv
$ .\Scripts\activate
```

3. install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
*Note: `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.
For pipenv you will not see any `(env)` in front of the propt.*

4. Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
(env)$ python manage.py runserver
```
The application should be running on `http://127.0.0.1:8000/`