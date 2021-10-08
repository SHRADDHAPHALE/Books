FROM python:3.6.9-alpine

WORKDIR /book/app

COPY . .

RUN pip3 install psycopg2
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python","app.py"]