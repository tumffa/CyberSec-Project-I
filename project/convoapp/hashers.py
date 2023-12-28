from django.contrib.auth.hashers import BasePasswordHasher
from django.utils.crypto import constant_time_compare

class PlaintextPasswordHasher(BasePasswordHasher):
    algorithm = "plaintext"

    def salt(self):
        return ''

    def encode(self, password, salt):
        return self.algorithm + '$$' + password

    def verify(self, password, encoded):
        algorithm, salt, hash = encoded.split('$', 2)
        assert algorithm == self.algorithm
        return constant_time_compare(password, hash)