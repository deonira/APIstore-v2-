FROM python:3.11

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

RUN pip install setuptools

COPY . /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]