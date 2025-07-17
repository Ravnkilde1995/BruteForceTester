from password_list import Password
from hash_utils import HashUtils
from brute_force import BruteForcer

class TestEnv:
    def __init__(self, wordlist_path="wordlists\common.txt", algo: str = 'sha256'):
        self.password_list = Password()
        self.wordlist_path = wordlist_path
        self.algo = algo

        self.original_password = None
        self.hashed_password = None
        self.brute = None
    
        def setup(self):
            self.original_password = self.password_list.get_random_password()
            self.hashed_password = HashUtils.generate_hash(self.original_password, self.algo)
            self.brute = BruteForcer(self.wordlist_path, self.algo)

        def teardown(self):
            self.original_password = None
            self.hashed_password = None
            self.brute = None