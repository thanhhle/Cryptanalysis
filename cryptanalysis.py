# CECS 378                               Spring 2019                            Project 1

# Name: Thanh Le
# Student ID: 015809792
# Start Date: 2-11-2019
# End Date: 3-6-2019

# -----------------------------------------------------------------------------------------
# Cryptanalysis
# Sources: 
#   - quadgram statistics 'english_quadgrams.txt' from http://practicalcryptography.com/cryptanalysis/letter-frequencies-various-languages/english-letter-frequencies/#quadgram-frequencies
#   - wordsegment module from http://www.grantjenks.com/docs/wordsegment/ (Use this command line: "pip install wordsegment" to install wordsegment module)
#   - English dictionary 'dictionary.txt' from http://www.gwicks.net/dictionaries.htm
# -----------------------------------------------------------------------------------------

import random
import re
import time
from substitution_cipher import SubstitutionCipher
from gram_score import GramScore

# This module is used to divide a phrase into a list of English words
from wordsegment import segment, load        

    
class Cryptanalysis:
    
    def __init__(self):
        self.fitness = GramScore(open('english_quadgrams.txt', 'r'))

    
    # Decrypt the cipher_text without known secret_key
    def decrypt(self, cipher_text):
        start = time.time()
        print('Ciphertext:', cipher_text.replace('\n', ''))

        print('\nStart decryption... \n')
        
        # List of high_score key but decrypted text are not all Enlgish words
        excluded_keys = []

        while True:
            best_key = 'abcdefghijklmnopqrstuvwxyz'
            best_score = -99e99
    
            parent_key, parent_score = best_key, best_score
            
            # Looking for the fittest key in 60 seconds
            end_time = time.time() + 30
            while time.time() < end_time:
                # Generate random key called parent_key
                parent_key_list = list(parent_key)
                random.shuffle(parent_key_list)
                parent_key = "".join(parent_key_list)
                        
                        
                # Decrypt the cipher_text by the parent_key
                plain_text = SubstitutionCipher(parent_key).decrypt(cipher_text)
                        
                        
                # Calculate the score of the decrypted text
                parent_score = self.fitness.get_score(plain_text)
                        
                        
                # Generate child_key to decrypt the plain_text to compare with one decrypted from parent_key
                # Every time the child_key results in better fitness in plain_text, the parent_key is set to child_key
                count = 0
                while count < 1000:
                    # Generate child_key by randomly swapping 2 characters in parent_key
                    child_key = parent_key
                    while True:
                        position1 = random.randint(0, 25)
                        position2 = random.randint(0, 25)
                        child_key = swap(child_key, position1, position2)
                        if child_key not in excluded_keys:
                            break
                            
                            
                    # Decrypt Decrypt the cipher_text by the child_key
                    plain_text = SubstitutionCipher(child_key).decrypt(cipher_text)
                    
                             
                    # Calculate the score of the decrypted text
                    child_score = self.fitness.get_score(plain_text)
                    
    
                    # If the child_key results in better fitness, the parent_key is set to child_key
                    if child_score > parent_score:
                        parent_score = child_score
                        parent_key = child_key
                        count = 0
                    
                                
                    count = count + 1
                    
                        
                # If the parent_key results in better fitness than best_key, the best_key is set to parent_key
                if parent_score > best_score:
                    best_key, best_score = parent_key, parent_score
        
            
            # Decrypt the cipher_text by the best_key found so far
            plain_text = SubstitutionCipher(best_key).decrypt(cipher_text)
            
            # Check if the plain_text contains all English words
            if allAreEnglish(plain_text):
                break                                       # Stop the process if the plain_text is English
            else:
                excluded_keys.append(best_key)              # Add the best_key to excluded_key list
                
            
        #plain_text = fixSpacing(plain_text)                # Use segment function in wordsegment module to separate words
        print('Decryption time:', time.time()-start, '\n')
        return plain_text
               
    
    # Encrypt the plain_text by secret_key
    def encrypt(self, secret_key, plain_text):
        print('\nPlaintext:', plain_text.replace('\n', ''))
        print('\nStart encryption... \n')
        plain_text = re.sub(r'[^a-zA-Z0-9]+', '', plain_text)   # Strip out all special character other than alphabelt
        cipher_text = SubstitutionCipher(secret_key).encrypt(plain_text)
        return cipher_text
    
    
    
# Swap 2 characters at position1 and position2 of the string    
def swap(string, position1, position2):
    L = list(string)
    L[position1], L[position2] = L[position2], L[position1]
    return ''.join(L)



# Add appropriate space to separate words in the string
def fixSpacing(string):
    load()
    string = segment(string)
    return ' '.join(string)


# Check if the string contains all English words
def allAreEnglish(string):
    dict = open('dictionary.txt', 'r').read().lower().split('\n')
    load()
    string = segment(string)
    
    for word in string:
        if word not in dict:
            return False
        
    return True


    
    
    