FROM python:alpine
COPY . /code

RUN pip install flask redis
WORKDIR /code
EXPOSE 5000
CMD ["python", "app.py"]
