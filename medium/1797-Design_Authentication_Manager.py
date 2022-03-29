"""1797: class and hashmap
There is an authentication system that works with authentication tokens.
For each session, the user will receive a new authentication token that will expire timeToLive seconds after the currentTime.
If the token is renewed, the expiry time will be extended to expire timeToLive seconds after the (potentially different) currentTime.

Implement the AuthenticationManager class:

* AuthenticationManager(int timeToLive) constructs the AuthenticationManager and sets the timeToLive.
* generate(string tokenId, int currentTime) generates a new token with the given tokenId at the given currentTime in seconds.
* renew(string tokenId, int currentTime) renews the unexpired token with the given tokenId at the given currentTime in seconds. If there are no unexpired tokens with the given tokenId, the request is ignored, and nothing happens.
* countUnexpiredTokens(int currentTime) returns the number of unexpired tokens at the given currentTime.

Note that if a token expires at time t, and another action happens on time t (renew or countUnexpiredTokens), the expiration takes place before the other actions.
"""


class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.t = timeToLive
        self.tokens = dict()

    def generate(self, tokenId: str, currentTime: int) -> None:
        time_to_expire = currentTime + self.t
        self.tokens[tokenId] = time_to_expire

    def renew(self, tokenId: str, currentTime: int) -> None:
        # token in memory and not expired
        if tokenId in self.tokens and self.tokens[tokenId] > currentTime:
            self.tokens[tokenId] = currentTime + self.t

    def countUnexpiredTokens(self, currentTime: int) -> int:
        n = 0
        for tokenId, expire_time in self.tokens.items():
            if currentTime < expire_time:
                n += 1
        return n
