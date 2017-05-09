from flask import Flask
from redis import StrictRedis
import os

app = Flask(__name__)

redis = StrictRedis(host=os.environ['REDIS_HOST'])


@app.route('/')
def hello_world():
  return 'Hello, {} World!'.format(redis.info()['executable'])
