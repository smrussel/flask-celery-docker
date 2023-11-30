
# Flask + Celery + Flask-SQLAlchemy + Nginx + Docker  Example App

This sample application illustrates the creation of Celery tasks compatible with Flask and Flask-SQLAlchemy. Additionally, Nginx has been incorporated to facilitate deployment in a Dockerized production environment.


## Code characteristics

* Tested on Python 3.9

## Features

- Celery Task Integration: Easily incorporate Celery tasks into your Flask application for efficient task processing.
- Flask and Flask-SQLAlchemy Compatibility: Seamlessly work with Flask and Flask-SQLAlchemy to enhance the functionality of your application.
- Nginx Integration: Streamline deployment in a production environment using Docker with the added benefit of Nginx support.
- Asynchronous Database Operations: Run database operations asynchronously using Celery tasks, optimizing performance and responsiveness.


## Run with docker

For Developement

```bash
  docker-compose -f docker-compose.dev.yml up -d
```

For Production with Nginx

```bash
  docker-compose up --build -d
```

## License

The MIT License
