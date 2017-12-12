# -*- encoding: UTF-8 -*-
"""
Day5 source code

:Author: Tigran Horozian
:email: tigran.horozian@gmail.com
"""
import argparse
import math
import IPython

def compute_part1(mylist):
    """
    Computes the number of jump to get out of the list

    args: mylist : a list of integers
    returns : The number of jumps
    """
    # Variables
    index = 0
    result = 0
    while index < len(mylist):
        jump = mylist[index]
        mylist[index] += 1
        index += jump
        result +=1

    return result

def compute_part2(mylist):
    """
    Computes the number of jump to get out of the list

    args: mylist : a list of integers
    returns : The number of jumps
    """
    index = 0
    result = 0
    while index < len(mylist):
        jump = mylist[index]
        if jump >= 3:
            mylist[index] -= 1
        else:
            mylist[index] += 1
        index += jump
        result +=1

    return result


if __name__ == '__main__':

    # Parse the file as arg
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=file, help='the file to read')
    args = parser.parse_args()

    #Vars
    f = args.filename.readlines()

    #Create a correct list from what is read
    for _ in range(0,len(f)):
        f[_] = f[_].split("\n")[0]
        f[_] = int(f[_])

    print("first half answer is : " + str(compute_part1(f)))
    print("second half answer is : " + str(compute_part2(f)))
