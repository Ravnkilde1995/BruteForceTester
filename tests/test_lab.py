from password_loader import PasswordLoader
from brute_forcer import BruteForcer
from hasher import Hasher

def test_hash_is_str():
    h = Hasher('sha256')
    assert isinstance(h.hash_password('test'), str)

def test_hashes_differ():
    h = Hasher('sha256')
    assert h.hash_password('a') != h.hash_password('b')

def test_payload_loads(tmp_path):
    file = tmp_path / "pwds.txt"
    file.write_text("a\nb\nc\n")
    loader = PasswordLoader(str(file))
    assert loader.get_all_passwords() == ['a', 'b', 'c']

def test_cracks_hash():
    pwds = ['a', 'b', 'secret', 'c']
    h = Hasher('sha256')
    target = 'secret'
    hashed = h.hash_password(target)
    brute = BruteForcer(pwds, h)
    cracked, index = brute.crack_hash(hashed)
    assert cracked == target
    assert index == 3
