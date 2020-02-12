FROM python:latest
COPY requirements.txt .
COPY flaskproject/Hello.py .
RUN pip install -r requirements.txt
CMD export FLASK_APP=Hello.py && flask run --host=0.0.0.0 
