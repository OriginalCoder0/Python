from flask import Flask
import redis

app = Flask(__name__)
# host='redis' 的名字通过 docker --name 指定
rd = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = rd.incr("hits")
    return "Hello World! {}".format(count)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
