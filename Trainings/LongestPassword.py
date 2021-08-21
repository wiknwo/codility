# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    """
    You would like to set a password for a bank account. However,
    there are three restrictions on the format of the password:
    - it has to contain only alphanumerical characters (a-z, A-Z,
    0-9);
    - there should be an even number of letters;
    - there should be an odd number of digits.

    You are given a string S consisting of N characters. String S
    can be divided into words by splitting it at, and removing, 
    the spaces. The goal is to choose the longest word that is a
    valid password. You can assume that if there are K spaces in
    string S then there are exactly K + 1 words.

    Write a function: that, given a non-empty string S consisting
    of N characters, returns the length of the longest word from
    the string that is a valid password. If there is no such 
    word, your function should return -1.
    """
    # write your code in Python 3.6
    passwords = S.split(' ') # Split the string about spaces
    longest_password = -1
    letter_count, digit_count = 0, 0
    # Iterate through tokens and find valid passwords
    for password in passwords:
        for char in password:
            if char.isalnum():
                if char.islower() or char.isupper():
                    letter_count += 1
                elif char.isdigit():
                    digit_count += 1
            elif not char.isalnum():
                letter_count, digit_count = 0, 0
                break # password is not valid
        # Found valid password
        if letter_count % 2 == 0 and digit_count % 2 == 1:
            # Check if valid password is longer than longest
            if letter_count + digit_count > longest_password:
                longest_password = letter_count + digit_count
        letter_count, digit_count = 0, 0 # Reset counts
    return longest_password