from random import seed
from random import random
from time import time

"""
    BIM-Simple-Captcha

    written to beat simple bots if possible

    Solution:
        Come up with a string of characters that the user can select (buttons) to verify some
        semblance of non-web crawling or non-bot parsing of a form page

        Generate 3 strings, a question, and a solution
            - One string containing only numbers
            - One string containing only letters
            - One string containing only punctuations
            - The solution is a random number between 0-2
            - The Question reflects what the expected answer should be
    
    Random Number Generation:
        This is done by taking SEED(1) and multiplying as well as adding time() to it, rounding, then modding.
        This gives a random number from 0 to the modded number.  
        
        This random number is used to select static values from arrays.  These static values are created and 
            randomly selected to give the process variation.  The numbers, letters, and symbols are picked
            using the random number generation.
"""


def generate_captcha():
    # determine if we want alpha, numeric, or punctuation for the answer
    seed(1)
    challengeSolution = round(random() * time() + time()) % 6

    # make the 3 strings to be used in the interface
    challengeStrings = build_challenge_strings(challengeSolution)

    # set the qusetion for the appropriate key, the key, and the single concatenated captcha string
    challengeQuestion = ''
    if((challengeSolution is 0) or (challengeSolution is 4)):
        challengeQuestion = 'Select the string that contains only NUMBERS.'
    if((challengeSolution is 1) or (challengeSolution is 5)):
        challengeQuestion = 'Select the string that contains only LETTERS.'
    if((challengeSolution is 2) or (challengeSolution is 3)):
        challengeQuestion = 'Select the string that contains only PUNCTUATION.'

    return challengeQuestion, challengeSolution, challengeStrings

def generate_number_string():
    options = ['34225', '12939', '15236', '27865', '95053', '23426', '12334', '23610', '95043', '72934']
    selector = round(random() * time() + time()) % 10
    return options[selector]

def generate_alpha_string():
    options = ['ABESR', 'DRUDR', 'POEMS', 'CMNES', 'XIEMD', 'YIESO', 'QERSN', 'PDRMR', 'CSREY', 'MERXT']
    selector = round(random() * time() + time()) % 10
    return options[selector]

def generate_punc_string():
    options = [',.!!?', '?!.,?', '!?.,.','?!??!']
    selector = round(random() * time() + time()) % 4
    return options[selector]

def build_challenge_strings(variant):
    if(variant < 3):
        return {'0': generate_number_string(), '1': generate_alpha_string(), '2': generate_punc_string()}
    else:
        return {'3': generate_punc_string(), '4': generate_number_string(), '5': generate_alpha_string()}


