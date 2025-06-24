
import redis
import os
from dotenv import load_dotenv

load_dotenv()

psw = os.getenv("Redis_password")

redis_client = redis.Redis(
    host='redis-15358.c283.us-east-1-4.ec2.redns.redis-cloud.com',
    port=15358,
    decode_responses=True,
    username="default",
    password=psw,
)



