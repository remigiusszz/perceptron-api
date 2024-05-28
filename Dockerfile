FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
COPY . /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install --upgrade werkzeug 

CMD ["python", "app.py"]
