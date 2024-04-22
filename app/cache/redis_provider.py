import redis

import config
from app.cache.base_cache_provider import BaseCacheProvider
from app.logs.sentry import sentry_client

REDIS_HOST: str = config.REDIS_HOST
REDIS_PORT: str = config.REDIS_PORT
REDIS_PASSWORD: str = config.REDIS_PASSWORD


# Redis cache provider
class RedisCacheProvider(BaseCacheProvider):
    def __init__(self):
        try:
            self.redis_client = redis.StrictRedis(
                host=config.REDIS_HOST,
                port=config.REDIS_PORT,
                db=0,
                decode_responses=True,
                password=config.REDIS_PASSWORD,
            )
        except Exception as e:
            sentry_client.capture_exception(str(e))
            self.redis_client = None

    def exists(self, key):
        return self.redis_client.exists(key)

    def get(self, key):
        return self.redis_client.get(key)

    def set(self, key, value, expiry_time):
        self.redis_client.set(key, value, ex=expiry_time)

    def setex(self, name, time, value):
        return self.redis_client.setex(name, time, value)

    def delete(self, key):
        self.redis_client.delete(key)

    def ttl(self, key):
        return self.redis_client.ttl(key)
