FROM python:3-alpine
RUN apk add --update curl && rm -rf /var/cache/apk/*
COPY . /app
WORKDIR /app
RUN pip3 install flask gunicorn --no-cache-dir
CMD [ "gunicorn", "-b", "0.0.0.0:8000", "--workers=4", "schnupf:app" ]
