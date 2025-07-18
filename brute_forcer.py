class BruteForcer:
    def __init__(self, password_payload: list, hasher, verbose = False):
        self.passwords = password_payload
        self.hasher = hasher
        self.verbose = verbose

    def crack_hash(self, target_hash: str):
        attempts = 0
        for pw in self.passwords:
            attempts += 1
            hashed = self.hasher.hash_password(pw)
            if self.verbose and attempts % 50 == 0:
                print(f"Trying password #{attempts}: {pw}")
            if hashed == target_hash:
                return pw, attempts
        return None, attempts