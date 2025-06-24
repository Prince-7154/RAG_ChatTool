
import redis
import os
from dotenv import load_dotenv

load_dotenv()

psw = os.getenv("Redis_password")
url = os.getenv("Redis_url")

redis_client = redis.Redis(
    host= url,
    port=15358,
    decode_responses=True,
    username="default",
    password=psw,
)



