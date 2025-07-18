import argparse
import time
from password_loader import PasswordLoader
from hasher import Hasher
from brute_forcer import BruteForcer

def main():
    parser = argparse.ArgumentParser(description="Brute Force Password Cracker")
    parser.add_argument('--file', default='wordlists/leaked_passwords.txt', help='Path to the password file')
    parser.add_argument('--algo', default='sha256', help='Hashing algorithm to use (default: sha256)')
    parser.add_argument('--v', action='store_true', help='Enable progress output')
    args = parser.parse_args()

    # Load passwords from file
    password_loader = PasswordLoader(args.file)
    target_password = password_loader.get_random_password()
    hasher = Hasher(args.algo)
    target_hash = hasher.hash_password(target_password)

    print(f"Target hash: {args.algo} : {target_hash}")

    brute = BruteForcer(password_loader.get_all_passwords(), hasher, args.v)
    start_time = time.time()
    result, attempts = brute.crack_hash(target_hash)
    end_time = time.time()

    print("Result:")
    if result:
        print(f"Match found: {result} in {attempts} attempts")
    else:
        print("No match found")
    print(f"Time taken: {end_time - start_time:.3f} seconds")

if __name__ == "__main__":
    main()