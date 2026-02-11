FROM python:3.12.12-alpine3.23
# FROM nginx:mainline-alpine

ENV TZ=Europe/Warsaw

WORKDIR /app

RUN python -m venv /venv

ENV PATH="/venv/bin:$PATH"

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY templates ./templates

ENV PORT=5000
EXPOSE 5000

RUN adduser --disabled-password appuser
USER appuser

CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "app:app"]

## FLASK UNICORN DASHBOARD

# RUN rm /etc/nginx/conf.d/*
# ADD hello.conf /etc/nginx/conf.d/
# ADD index.html /usr/share/nginx/html/
