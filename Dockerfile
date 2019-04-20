FROM python:3.7-alpine
WORKDIR /usr/src/app

COPY requirements.txt /
RUN pip install -r /requirements.txt

ENV PORT 8080
ENV HOST 0.0.0.0

COPY . /usr/src/app

EXPOSE 8080

CMD ["python", "server.py"]