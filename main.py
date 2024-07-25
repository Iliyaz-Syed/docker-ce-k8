from flask import Flask, jsonify
from pymongo import MongoClient
import redis

app = Flask(__name__)

# MongoDB setup
mongo_client = MongoClient('mongodb://mongo:27017/')
db = mongo_client.mydatabase

# Redis setup
redis_client = redis.Redis(host='redis', port=6379)

@app.route('/')
def index():
    # MongoDB operation
    db.test_collection.insert_one({"message": "Hello from MongoDB!"})
    mongo_message = db.test_collection.find_one({"message": "Hello from MongoDB!"})["message"]

    # Redis operation
    redis_client.set('message', 'Hello from Redis!')
    redis_message = redis_client.get('message').decode('utf-8')

    return jsonify({
        'mongo_message': mongo_message,
        'redis_message': redis_message
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0')