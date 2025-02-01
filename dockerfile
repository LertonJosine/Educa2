FROM python:3.10-slim

WORKDIR /Educa

COPY requirements.txt .

RUN pip install -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . .

CMD ["sh", "-c", " python manage.py migrate && gunicorn --bind 0.0.0.0:8000 educa.wsgi:application"]
