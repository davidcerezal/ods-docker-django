# Django - DDD with django-rest-framework, rest-registration, celery and prepared with Docker

### 1.- DDD skeleton
Bootstrap your new projects or be inspired by DDD and hexagonal architecture. 

### 2.- Django Rest Framework
Django REST framework is a powerful and flexible toolkit for building Web APIs.

Some reasons you might want to use REST framework:
- The Web browsable API is a huge usability win for your developers.
- Authentication policies including packages for OAuth1a and OAuth2.
- Serialization that supports both ORM and non-ORM data sources.
- Customizable all the way down - just use regular function-based views if you don't need the more powerful features.
- Extensive documentation, and great community support.
- Used and trusted by internationally recognised companies including Mozilla, Red Hat, Heroku, and Eventbrite.

Full documentation for the project is available at https://www.django-rest-framework.org/.


### 3.- Django Rest Registration
User registration REST API, based on Django REST Framework.

Full documentation for the project is available at https://django-rest-registration.readthedocs.io/.

### 4.- Celery
Celery is an asynchronous task queue/job queue based on distributed message passing. It is focused on real-time operation, but supports scheduling as well.

Full documentation for the project is available at http://www.celeryproject.org/.

### 5.- Docker
If you already doesn't know what it's docker, that place it's not for you.
Try with that: https://docs.docker.com/get-started/overview/

## Advantages
1. Ready to use with your django project.
2. Combined with NGINX, Redis, Celery to handle relevent things.
3. Now comes built it with Numpy, Scipy and Pandas support. So you can integrate your datascience projects with this. [Instructions](#now-featuring-numpy-scipy-and-pandas) for integrating these libraries are also shared in the `Dockerfile`.
4. With Numpy, Pandas and Scipy dependecies installed, the total size is 657MB(may differ if you have more packages). Without these, size reduces to 390MB.
5. Now comes with support to install [Pillow](https://pypi.org/project/Pillow/) using django.

## Now Featuring Numpy, Scipy and Pandas
In the [**`Dockerfile`**](https://github.com/ruddra/docker-django/blob/master/compose/django/Dockerfile), there are detailed instructions on how to install data science dependencies.

**PS:** Here is a [**__`gist`__**](https://gist.github.com/ruddra/870d7a51238ddfa4b50375086c12a4f5) which is more useful for Numpy, Pandas, Scipy etc. And it is usable with this project's [`docker-compose.yml`](https://github.com/ruddra/docker-django/blob/master/docker-compose.yml) file. Just you need to replace the `Dockerfile` from [*./compose*](https://github.com/ruddra/docker-django/blob/master/compose) directory with the one in the *gist*.

## Basic Usage
1. First run **`make build`** inside root directory.
2. Then run **`make up`** to start up the project for first time.
3. Use/update environment variables from [**`.envs`**](https://github.com/ruddra/docker-django/blob/master/.envs) folder.

Checkout the [commands](#commands) section for more usage.

## Preview
A default Django project resides in `src` directory. So, when you start the project, you will see the following screen in `8000` port:

![Demo One](https://github.com/ruddra/blog-images/raw/master/Demo%201.png)

Also when you access the django container log via `make log-web`, you will see the following:

![Demo Two](https://github.com/ruddra/blog-images/raw/master/Demo%202.png)

## Commands
To use this project, run this commands:

1. `make up` to build the project and starting containers.
2. `make build` to build the project.
3. `make start` to start containers if project has been up already.
4. `make stop` to stop containers.
5. `make shell-web` to shell access web container.
6. `make shell-db` to shell access db container.
7. `make shell-nginx` to shell access nginx container.
8. `make logs-web` to log access web container.
9. `make logs-db` to log access db container.
10. `make logs-nginx` to log access nginx container.
11. `make collectstatic` to put static files in static directory.
12. `make log-web` to log access web container.
13. `make log-db` to log access db container.
14. `make log-nginx` to log access nginx container.
15. `make restart` to restart containers.
