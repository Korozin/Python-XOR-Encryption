import string 
import secrets
import base64
import hashlib

class XorCryption:
    def __init__(self, encryption_key=None):
        self.alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

        if encryption_key == None:
            self.encryption_key_bytes = self.generate_encryption_key()
        else:
            self.encryption_key_bytes = encryption_key.encode()
        
    def remove_special_chars(self, string):
        special_chars = ["'", '"', '\\']
        for char in special_chars:
            string = string.replace(char, '')
        return string

    def generate_encryption_key(self):     
        encryption_key = ''.join(secrets.choice(self.alphabet) for i in range(94))
        encryption_key = self.remove_special_chars(encryption_key)
        self.encryption_key_bytes = encryption_key.encode()
        return self.encryption_key_bytes

    def encrypt(self, message):
        self.message = message
        message_bytes = message.encode()
        key_bytes = self.encryption_key_bytes

        initialization_vector = secrets.token_bytes(16)

        ciphertext_bytes = bytes([
            message_bytes[i] ^ key_bytes[i % len(key_bytes)]
            for i in range(len(message_bytes))
        ])

        ciphertext_bytes = bytes([
            ciphertext_bytes[i] ^ initialization_vector[i % len(initialization_vector)]
            for i in range(len(ciphertext_bytes))
        ])

        checksum = hashlib.sha256(key_bytes).digest()
        ciphertext_bytes_with_checksum = checksum + ciphertext_bytes

        ciphertext = base64.b64encode(ciphertext_bytes_with_checksum).decode()
        initialization_vector = base64.b64encode(initialization_vector).decode()

        return ciphertext, initialization_vector

    def decrypt(self, ciphertext, initialization_vector):
        key_bytes = self.encryption_key_bytes

        ciphertext_bytes_with_checksum = base64.b64decode(ciphertext.encode())
        initialization_vector_bytes = base64.b64decode(initialization_vector.encode())

        checksum = ciphertext_bytes_with_checksum[:32]
        ciphertext_bytes = ciphertext_bytes_with_checksum[32:]

        if hashlib.sha256(key_bytes).digest() != checksum:
            print('Incorrect encryption key\n')

        plaintext_bytes = bytes([
            ciphertext_bytes[i] ^ initialization_vector_bytes[i % len(initialization_vector_bytes)]
            for i in range(len(ciphertext_bytes))
        ])

        plaintext_bytes = bytes([
            plaintext_bytes[i] ^ key_bytes[i % len(key_bytes)]
            for i in range(len(plaintext_bytes))
        ])

        try:
            plaintext = plaintext_bytes.decode()
            return plaintext
        except Exception:
            print('Incorrect initialization vector\n')
