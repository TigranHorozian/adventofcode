# -*- encoding: UTF-8 -*-
"""
Day4 source code

:Author: Tigran Horozian
:email: tigran.horozian@gmail.com
"""
import argparse

def is_valid_passphrase_1(passphrase):
    """
        Checks if there are duplicate words in the passphrases

        args: passphrase : a list of strings
        returns : True if no duplicates in the list, False otherwise
    """
    words = passphrase.split(" ")
    if len(words) == len(set(words)) : # set removes the duplicates
        return True

    return False

def is_valid_passphrase_2(passphrase):
    """
        Checks if there are duplicate words and anagrams in a passphrase

        args: passphrase : a list of strings
        returns : True if no duplicates/anagrams in the list, False otherwise
    """
    words = passphrase.split(" ")
    # sort every word of the passphrase in alphabetical order
    for word in range(0,len(words)):
        words[word] = ''.join(sorted(words[word]))

    #Look for duplicates (and anagrams too since you wors are sorted)
    if len(words) == len(set(words)) : # no duplicates
        return True

    return False

if __name__ == '__main__':

    # Parse the file as arg
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=file, help='the file to read')
    args = parser.parse_args()

    #Vars
    f = args.filename.readlines()
    result1 = 0
    result2 = 0

    #Calculate the results
    for _ in range(0,len(f)):
        f[_] = f[_].split("\n")[0]
        if is_valid_passphrase_1(f[_]):
            result1 += 1
            if is_valid_passphrase_2(f[_]): #Don't recheck if it had duplicates
                result2 += 1

    print("Number of correct passphrases for first half is : " + str(result1))
    print("Number of correct passphrases for second half is : " + str(result2))
