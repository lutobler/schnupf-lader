FROM archlinux/base
RUN yes | pacman -Syyuu
RUN yes | pacman -S python python-flask gunicorn sqlite
COPY . /app
WORKDIR /app
CMD [ "/usr/bin/gunicorn", "-b", "0.0.0.0:8000", "--workers=4", "schnupf:app" ]

