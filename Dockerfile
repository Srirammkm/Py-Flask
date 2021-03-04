FROM python:3
USER root
COPY . /app/
WORKDIR /app/
RUN pip install --upgrade pip
RUN pip install flask
RUN pip install Flask-MySQLdb
EXPOSE 80
CMD [ "python","app.py"]

