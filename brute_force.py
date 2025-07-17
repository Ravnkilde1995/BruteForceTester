from hash_utils import HashUtils

class BruteForcer:
    def __init__(self, wordlist_path: str, algo: str = 'sha256'):
        self.wordlist_path = wordlist_path
        self.algo = algo

    def brute_force(self, target_hash: str) -> str | None:
        try:
            with open(self.wordlist_path, 'r') as file:
                for word in file:
                    word = word.strip()
                    if HashUtils.verify(word, target_hash, self.algo):
                        return word
        except FileNotFoundError:
            print(f"Wordlist file not found: {self.wordlist_path}")
        except Exception as e:
            print(f"An error occurred: {e}")