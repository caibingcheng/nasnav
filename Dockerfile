FROM alpine:latest
RUN apk add --update --no-cache python3 py3-pip

COPY . /www
WORKDIR /www
RUN python3 -m pip install -r requirements.txt

CMD ["python3", "src/app.py"]