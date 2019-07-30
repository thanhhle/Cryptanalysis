# CECS 378                               Spring 2019                            Project 1

# Name: Thanh Le
# Student ID: 015809792
# Start Date: 2-11-2019
# End Date: 3-6-2019

# -----------------------------------------------------------------------------------------
# Subsitution Cipher
# -----------------------------------------------------------------------------------------

class SubstitutionCipher:
    def __init__(self, secret_key):
        # Create list of alphabelt character
        alphabelt = list('abcdefghijklmnopqrstuvwxyz')
        
        
        # Create list of key character
        secret_key = secret_key.lower()
        secret_key = list(secret_key)
        
        
        # Create encrypt_map dictionary
        # Key is alphabelt character
        # Value is corresponding secret_key character to be replaced in encryption
        self.encrypt_map = dict(zip(alphabelt, secret_key))
        
        
        # Create decrypt_map dictionary
        # Key is secret_key character
        # Value is corresponding alphabelt to be replaced in decryption
        self.decrypt_map = dict(zip(secret_key, alphabelt))


    
    #-------------------------------------------------------------------------------------
    # Encrypt plain_text and return cipher_text
    def encrypt(self, plain_text):
        cipher_text = ''
        plain_text = plain_text.replace(' ', '').replace('\n', '').lower()
        
        for c in plain_text:
            cipher_text = cipher_text + self.encrypt_map[c]
        
        return cipher_text
            
    #-------------------------------------------------------------------------------------
    #Decrypt cipher_text and return plain_text
    def decrypt(self, cipher_text):
        plain_text = ''
        cipher_text = cipher_text.replace(' ', '').replace('\n', '').lower()
        
        for c in cipher_text:
            plain_text = plain_text + self.decrypt_map[c]
        
        return plain_text
