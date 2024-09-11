# oauth2-client/Dockerfile
FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# oauth2-client/requirements.txt
Django==4.2.3
requests==2.31.0

# oauth2-server/Dockerfile
FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src .

CMD ["sh", "-c", "python manage.py migrate && python manage.py setup_oauth2 && python manage.py runserver 0.0.0.0:8000"]
