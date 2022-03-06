FROM python:slim-buster
WORKDIR /app
RUN python3 -m pip install --upgrade pip
COPY ./pyrogram.txt .
RUN python3 -m pip install -r pyrogram.txt
COPY ./postgres.txt .
RUN python3 -m pip install -r postgres.txt
COPY . .
CMD [ "python3", "app.py" ]
