from cryptography.fernet import Fernet

class Encryptor():

    def __init__(self, *args, **kwargs):
        self.fernet_obj = Fernet

    def generate_Key_file(self):
        key = self.fernet_obj.generate_key()
        with open('key.txt',"wb") as key_file:
            key_file.write(key)

    def load_key(self):
        key = ""
        with open('key.txt',"rb") as key_file:
            key = key_file.read()
        return key
    
    def encrypt_file(self,orig_file):
        key = self.load_key()
        f = self.fernet_obj(key)
        with open(orig_file,'rb') as fd:
            content = fd.read()
        encrypted = f.encrypt(content)
        with open (orig_file, 'wb') as fd:
            fd.write(encrypted)

    def decrypt_file(self,orig_file):
        key = self.load_key()
        f = self.fernet_obj(key)
        with open(orig_file,'rb') as fd:
            content = fd.read()
        decrypted = f.decrypt(content)
        with open (orig_file, 'wb') as fd:
            fd.write(decrypted)

















