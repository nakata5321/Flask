FROM python:latest
RUN apt-get update
RUN mkdir flaskApp
WORKDIR /flaskApp
COPY requirements.txt /flaskApp/requirements.txt
COPY flaskproject/Hello.py /flaskApp/Hello.py
COPY flaskproject/templates /flaskApp/templates
RUN pip install -r requirements.txt
ENV FLASK_APP Hello.py
ENV FLASK_RUN_HOST 0.0.0.0
EXPOSE 5000
CMD flask run
