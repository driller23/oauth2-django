# oauth2-client/Dockerfile
FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# oauth2-client/requirements.txt
Django==3.2.10
requests==2.26.0

# oauth2-server/Dockerfile
FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src .

CMD ["sh", "-c", "python manage.py migrate && python manage.py setup_oauth2 && python manage.py runserver 0.0.0.0:8000"]
