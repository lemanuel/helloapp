FROM python:3.7-slim

RUN apt-get update && apt-get install -y curl

RUN pip install flask

COPY app.py app.py

EXPOSE 5000

CMD python app.py
