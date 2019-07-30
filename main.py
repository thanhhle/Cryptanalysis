# CECS 378                               Spring 2019                            Project 1

# Name: Thanh Le
# Student ID: 015809792
# Start Date: 2-11-2019
# End Date: 3-6-2019

# -----------------------------------------------------------------------------------------
# PROJECT 1
# -----------------------------------------------------------------------------------------

from cryptanalysis import Cryptanalysis

def main():
    crypto = Cryptanalysis()


    # PART A: Decrypt the encrypted quotations saved in encrypted_quotations.txt
    print('\n--------------------------------------- PART A ----------------------------------------\n')
    file = open('encrypted_quotations.txt', 'r')
    for cipher_text in file:
        plain_text = crypto.decrypt(cipher_text)
        print('Plaintext:', plain_text)
        print('\n-----------------------------------------------------------------------\n')

    
    
    
    
    # PART B: Encrypt the text saved in pheases.txt with the input key
    print('\n--------------------------------------- PART B ----------------------------------------')
    secret_key = input('Enter the secret key: ')
    #secret_key = 'tkrqcujmhebdpnlwvifsyaxzgo'
    file = open('phrases.txt', 'r')
    
    print('\n-----------------------------------------------------------------------')
    
    for plain_text in file:
        cipher_text = crypto.encrypt(secret_key, plain_text)
        print('Ciphertext:', cipher_text)
        print('\n-----------------------------------------------------------------------')
    
    
main()