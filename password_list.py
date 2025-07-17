import random

class Password:
    def __init__(self):
        self.passwords = [
            "qwert", "12345", "password", "letmein", "welcome",
            "admin", "user", "test", "abc123", "iloveyou",
            "monkey", "dragon", "sunshine", "trustno1",
            "qwertyuiop", "123456789", "football", "baseball"
            ]
        
    def get_random_password(self):
        return random.choice(self.passwords)
    
    def get_all_passwords(self):
        return self.passwords