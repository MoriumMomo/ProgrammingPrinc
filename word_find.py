# Name:  Morium Mostafa Momo
# Student Number:  10492778

# This file is provided to you as a starting point for the "word_find.py" program of Assignment 2
# of Programming Principles in Semester 2, 2019.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis for your assignment work.
# You are not required to reference it.

# The "pass" command tells Python to do nothing.  It is simply a placeholder to ensure that the starter files run smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.


# Import the necessary modules.
import urllib.request # Used to send a request to the Wordnik API over the internet.
import json # Used to convert between JSON-formatted text and Python variables.
import string # Used to provide convenient access to a string variable containing all uppercase letters.
import random # Used to randomly select letters.



# This function generates and returns a list of 9 letters.  It has been completed for you.
# See Point 1 of the "Functions in word_find.py" section of the assignment brief.
def select_letters():
    # This tuple contains 26 numbers, representing the frequency of each letter of the alphabet in Scrabble.
    letter_weights = (9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1)

    # The letter_weights tuple is used in this call to the "random.choices()" function, along with
    # the pre-defined "string.ascii_uppercase" variable which contains the letters A to Z.
    chosen_letters = random.choices(string.ascii_uppercase, weights=letter_weights, k=9)

    # We've selected a list of 9 random letters using the specified letter frequencies, and now return it.
    return chosen_letters



# This function displays the 9 letters in a 3x3 grid.
# See Point 2 of the "Functions in word_find.py" section of the assignment brief.
def display_letters(letters): 
    print('               ' + letters[0] + ' | ' + letters[1] + ' | ' + letters[2])
    print('               ' + '-----------')
    print('               ' + letters[3] + ' | ' + letters[4] + ' | ' + letters[5])
    print('               ' + '-----------')
    print('               ' + letters[6] + ' | ' + letters[7] + ' | ' + letters[8])


# This function checks whether a word entered by the user contains appropriate letters.
# See Point 3 of the "Functions in word_find.py" section of the assignment brief.
def validate_word(word, letters):
    for i in word:
        if i not in letters:
            return False
    return True


# main body of code
API_key = 'nmksgth77736b9i01k7p1w281wpsug430pcofh994a37dl9hw'
# Welcome the user and create necessary variables (Requirement 1).
print('Welcome to Word Find.')


score = 0
user_words = []
letters = select_letters()

print('Came up with as many words as possible from the letters below!')

# Enter gameplay loop (Requirement 2).
while (True):

    # Display score, letter grid and prompt user for input (Requirement 2.1).
    print('Score ' + str(score) + '. Your letters are:')
    
    display_letters(letters)
    user_input = input('"Enter a word, [s]huffle letters, [l]ist words, or [e]nd game): ')
    word = user_input.upper()
    
    if word == 'E':
    # If input is "E",
        # End the game/loop (Requirement 2.2).
        print('Ending game...')
        break
    elif word == 'S':
    # Otherwise, if input is "S",
        # Shuffle the letters (Requirement 2.3).
        print('Shuffling letters...')
        random.shuffle(letters)
    elif word == 'L':
    # Otherwise, if input is "L",
        # List previously used words (Requirement 2.4).
        if len(user_words) == 0:
            print('The list is empty!')
        else:
            user_words.sort()
            print('Previously entered words: ')
            for i_word in user_words:
                print('- ' + i_word)
            
    elif len(word)<3:
    # Otherwise, if input is less than 3 characters long,
        # Show appropriate message (Requirement 2.5).
        print('The word is less than three characters!')

    elif word in user_words:
    # Otherwise, if input is in the used words list,
        # Show appropriate message (Requirement 2.6).
        print('The input word is already in the user list!')

    elif not validate_word(word, letters):
    # Otherwise, if input is not valid,
        # Show appropriate message (Requirement 2.7).
        print('Invalid character(s) used!')
        
    else:
    # Otherwise,
        # Request Scrabble score of input, etc. (Requirement 2.8).
        try:
            response = json.load(urllib.request.urlopen('https://api.wordnik.com/v4/word.json/'
        +  word.lower() + '/scrabbleScore?api_key=' + API_key))
            # print the Scrabble score of the word
            score += int(response['value'])
            user_words.append(word)
        except urllib.error.HTTPError as err:
            if err.code == 404:
                print('Word not regocnised!')
            elif err.code == 429:
                print('Try again soon!')

        

# Print final score and record log of game if it is above 50 (Requirement 3).
print('Your final score is ' + str(score))

if score>=50:
    print('Congratulations! You scored more than 50 points.')
    data = dict()
    data['letters'] = letters
    data['words'] = user_words
    data['score'] = score 
    try:
        with open("logs.txt", "r") as read_file:
            logs = json.load(read_file)
            read_file.close()
    except:
        logs = []
    logs.append(data)
    with open('logs.txt', 'w') as write_file:
        json.dump(logs, write_file)
        write_file.close()
# Print "Thank you for playing!" (Requirement 4).
print("Thank you for playing!") 

