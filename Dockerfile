FROM jazzdd/alpine-flask
USER root
COPY . /app/
WORKDIR /app/
RUN pip install --upgrade pip
RUN pip install Flask-MySQLdb
EXPOSE 80
CMD [ "python","app.py"]

