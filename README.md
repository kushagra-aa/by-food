# By Food

By Food is a Django Application,
A Food Ordering Web Application

Built with 🤍 For You!

## Features

- User Authentication
- User Registration
- Order Database
- Camera Intigration

> user nees to click an image before confirming the order

## Made Using

- Python
- Django
- HTML
- CSS
- JS

- ### Tools

  - VS Code

- ### Concepts

  - Templates
  - CSS Animations
  - Custom Models
  - Django Authentication
  - Login-Logout
  - Django Admin

## Run Locally

Clone the project

```bash
  git clone https://github.com/kushagra-aa/by-food.git
```

Go to the project directory

```bash
  cd by-food
```

Install dependencies

```bash
  pip install -r requirements.txt
```

then run

```bash
python manage.py migrate
```

create admin account

```bash
python manage.py createsuperuser
```

then

```bash
python manage.py makemigrations
```

to makemigrations for the app

then again run

```bash
python manage.py migrate
```

to start the development server

```bash
python manage.py runserver
```

and open localhost:8000 on your browser to view the app.

> Debug is set to false, may need to run `py manage.py runserver --insecure`
