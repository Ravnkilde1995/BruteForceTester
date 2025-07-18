import random

class PasswordLoader:
    def __init__(self, file_path=str):
        with open(file_path, 'r') as file:
            self.passwords = [line.strip() for line in file if line.strip()]
        
    def get_random_password(self):
        return random.choice(self.passwords)
    
    def get_all_passwords(self):
        return self.passwords