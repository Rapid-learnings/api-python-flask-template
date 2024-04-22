import config
from app.cache.redis_provider import RedisCacheProvider

CACHE_PROVIDER: str = config.CACHE_PROVIDER


def get_cache_provider() -> RedisCacheProvider:

    if CACHE_PROVIDER == "redis":
        return RedisCacheProvider()
    # elif CACHE_PROVIDER == "inmemory":
    #     return InMemoryCacheProvider()
    else:
        raise ValueError(f"Unsupported cache provider type: {CACHE_PROVIDER}")
