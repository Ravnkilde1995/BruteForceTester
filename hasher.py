import hashlib

class Hasher:
    def __init__(self, algorithm: str = 'sha256'):
        self.algorithm = algorithm

    def hash_password(self, password: str) -> str:
        hash_attr = getattr(hashlib, self.algorithm, None)
        if not hash_attr:
            raise ValueError(f"Unsupported hashing algorithm: {self.algorithm}")
        return hash_attr(password.encode()).hexdigest()