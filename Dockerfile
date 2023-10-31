FROM python:3.10

WORKDIR /py/src/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN ["chmod", "+x", "entrypoint.sh"]

ENTRYPOINT ["./entrypoint.sh"]

#CMD ["python", "manage.py", "runserver"]xtentrypoint