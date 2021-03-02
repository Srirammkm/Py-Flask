FROM jazzdd/alpine-flask
USER root
COPY . /app/
WORKDIR /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 80
CMD [ "python","app.py"]

