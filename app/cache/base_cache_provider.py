# Base cache provider interface
from abc import ABC, abstractmethod


class BaseCacheProvider(ABC):

    @abstractmethod
    def exists(self, key):
        pass

    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def set(self, key, value, expiry_time):
        pass

    @abstractmethod
    def setex(self, name, time, value):
        pass

    @abstractmethod
    def delete(self, key):
        pass

    @abstractmethod
    def ttl(self, key):
        pass
