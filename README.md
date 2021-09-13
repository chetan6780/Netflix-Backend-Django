# Netflix-Backend-Django

![image](https://user-images.githubusercontent.com/62825092/133116839-17201a14-a2c2-4c59-b2e5-1a2a8f4904f7.png)
## Set up on local machine

1. Clone the repository
> For contribution fork and then clone your own repository.

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
(venv)$ pip install -r requirements.txt
```
*Note: `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.
For pipenv you will not see any `(venv)` in front of the propt.*

4. Once `pip` has finished downloading the dependencies:
```sh
(venv)$ python manage.py makemigrations
(venv)$ python manage.py migrate
(venv)$ python manage.py runserver
```
The application should be running on [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


