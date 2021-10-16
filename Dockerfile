FROM python:3.8-slim-buster

# We copy just the requirements.txt first to leverage Docker cache
COPY requirements.txt requirements.txt

WORKDIR .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]