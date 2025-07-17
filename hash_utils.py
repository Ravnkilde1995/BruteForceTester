import hashlib


class HashUtils:
    @staticmethod
    def generate_hash(text: str, algo: str = 'sha256') -> str:
        
        try:
            hash_string = getattr(hashlib, algo)
            return hash_string(text.encode()).hexdigest()
        except AttributeError:
            raise ValueError(f"Unsupported algorithm: {algo}")
        
    @staticmethod
    def verify(text: str, hash_bool: str, algo: str = 'sha256') -> bool:
        return HashUtils.generate_hash(text, algo) == hash_bool