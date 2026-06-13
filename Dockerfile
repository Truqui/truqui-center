FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ARG SECRET_KEY=build-time-dummy-key
RUN SECRET_KEY=${SECRET_KEY} python manage.py collectstatic --noinput

CMD ["gunicorn", "truqui_center.wsgi:application", "--bind", "0.0.0.0:8000"]