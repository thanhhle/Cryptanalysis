# CECS 378                               Spring 2019                            Project 1

# Name: Thanh Le
# Student ID: 015809792
# Start Date: 2-11-2019
# End Date: 3-6-2019

# -----------------------------------------------------------------------------------------
# Calculate gram probabilities
# -----------------------------------------------------------------------------------------

from math import log10

class GramScore:
    def __init__(self, file):
        self.dict = {}
        
        
        # Loop through the file to add the data to the dict
        for line in file:
            gram, count = line.lower().split(" ")
            self.dict[gram] = int(count)
         
            
        # Calulate number of characters in each gram
        self.gramLength = len(gram)
        
        
        # N = total number of grams
        self.N = sum(self.dict.values())
        
        
        # Get the list of all the grams in the dict
        grams = self.dict.keys()
        
        
        # Calculate Log probability of all the grams in the dictionary
        for gram in grams:
        
            # Probability P = number of times the gram occured/total number of grams
            P = float(self.dict[gram])/self.N
            
            # Store the log probability as the value of corresponding gram
            self.dict[gram] = log10(P)
           

        # Calculate floor probability
        self.floor = log10(0.01/self.N)


    #-------------------------------------------------------------------------------------
    # Calculate score of the input text based on the Log probability store in dict
    def get_score(self, text):
        score = 0
        
        for i in range(len(text) - self.gramLength + 1):
            phrase = text[i:(i+self.gramLength)]
            
            if phrase in self.dict:
                score = score + self.dict[phrase]
            else:
                score = score + self.floor  
                
                
        return score


