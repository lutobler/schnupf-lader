FROM python:3-alpine
COPY . /app
WORKDIR /app
RUN pip3 install flask gunicorn
CMD [ "gunicorn", "-b", "0.0.0.0:8000", "--workers=4", "schnupf:app" ]
