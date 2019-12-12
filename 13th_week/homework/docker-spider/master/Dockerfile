FROM python:alpine
#COPY . /code
VOLUME ["/code"]

RUN pip install redis
WORKDIR /code
#EXPOSE 5000
CMD ["python", "load_cid_urls.py"]
