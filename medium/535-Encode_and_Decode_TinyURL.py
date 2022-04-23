"""535: string operation
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl
 and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design a class to encode a URL and decode a tiny URL.

There is no restriction on how your encode/decode algorithm should work.
You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

Implement the Solution class:

- Solution() Initializes the object of the system.
- String encode(String longUrl) Returns a tiny URL for the given longUrl.
- String decode(String shortUrl) Returns the original long URL for the given shortUrl.
  It is guaranteed that the given shortUrl was encoded by the same object.
"""
from uuid import uuid4


class Codec:
    def __init__(self):
        self.baseurl = 'https://tinyurl.com/'
        self.memory = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        uid = str(uuid4()).split('-')[0]
        self.memory[uid] = longUrl
        return self.baseurl + uid

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        uid = shortUrl.rpartition('/')[-1]
        return self.memory[uid]
