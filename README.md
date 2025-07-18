# 🔐 BruteLearn (CLI Tool)

A CLI-based Python tool that simulates a brute-force attack to crack a hashed password. The project demonstrates object-oriented programming, hashing algorithms, CLI interaction, and performance tracking.

## 🧠 What does it do?

1. Randomly selects a password from a text file (`payload`).
2. Hashes the password using a specified algorithm (`sha256` by default).
3. Iterates through a wordlist, hashing each password to find a match.
4. Displays the cracked password, time taken, and number of attempts.
5. Supports verbose output to show progress.

## ▶️ Examples

### 🔹 Use default wordlist and sha256
```python main.py```

### 🔹Use a different hash algorithm and wordlist
```python main.py --file path/to/your/wordlist.txt --algo sha1```

### 🔹Enable verbose output
```python main.py --v```

### ⚠️ Disclaimer
This project is strictly for educational purposes.
Do not use this tool for unauthorized access, malicious purposes, or any unethical activities.
