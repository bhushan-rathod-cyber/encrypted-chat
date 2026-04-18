import base64
import hashlib
from cryptography.fernet import Fernet

# Convert user key → valid Fernet key
def generate_fernet_key(user_key):
    key = hashlib.sha256(user_key.encode()).digest()
    return base64.urlsafe_b64encode(key)

def encrypt_message(message, user_key):
    key = generate_fernet_key(user_key)
    f = Fernet(key)
    return f.encrypt(message.encode()).decode()

def decrypt_message(encrypted_message, user_key):
    key = generate_fernet_key(user_key)
    f = Fernet(key)
    return f.decrypt(encrypted_message.encode()).decode()