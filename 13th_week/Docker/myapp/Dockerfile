FROM alpine
LABEL version="1.0"
LABEL description="my first docker image"
RUN apk update && apk add python3
COPY . /code
WORKDIR /code
CMD ["python3", "app.py"]
