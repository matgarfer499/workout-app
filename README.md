# Workout Api

This is an api made with django that will handle requests from another frontend app with NextJS.

## Development setup

Steps to get the api up and running (make sure to have installed python and pip)

```sh
 git clone https://github.com/matgarfer499/workout-app.git
 cd workout-app
```
We create the virtual environment and install the dependencies
```sh
  pip install virtualenv
  python -m venv venv   
  pip install -r .\requirements.txt
```
Finally we run migrations
```sh
  py .\manage.py makemigrations
  py .\manage.py migrate
```
## How to use

To be able to keep track of our tables and data we have to do the following:
- Create an admin user
```sh
  py .\manage.py createsuperuser
```
- We start the server and go to the administration panel provided by django.
```sh
  py .\manage.py runserver
```
admin panel: `http://127.0.0.1:8000/admin/`

You also have a route to view the api documentation: `http://127.0.0.1:8000/api/docs/`


## Release History


## Meta

Matías José García Fernández – [Linkedin](www.linkedin.com/in/mgarfer) – matigarfer14@gmail.com

Distributed under the XYZ license. See ``LICENSE`` for more information.

[https://github.com/matgarfer499/](https://github.com/matgarfer499/)

## Contributing

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
