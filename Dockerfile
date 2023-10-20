FROM python:3.10.11-slim-buster

WORKDIR /src

RUN pip install Flask-DotEnv==0.1.2
RUN pip install python-dotenv==1.0.0
RUN pip install Flask==2.3.2
RUN pip install networkx==3.1
RUN pip install SQLAlchemy==2.0.15
RUN pip install gunicorn==20.1.0

EXPOSE 5000/tcp

# ENV FLASK_APP=app.py
# ENV FLASK_DEBUG=1

# ENTRYPOINT flask run --host=0.0.0.0 --port=5000

ENTRYPOINT gunicorn --bind 0.0.0.0:5000 wsgi:app
