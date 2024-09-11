# oauth2-server/Dockerfile

FROM python:3.11-alpine

WORKDIR /app

RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src .

# Ensure the template directory exists
RUN mkdir -p oauth_server/templates

CMD ["sh", "-c", "python manage.py migrate && python manage.py setup_oauth2 && python manage.py runserver 0.0.0.0:8000"]
