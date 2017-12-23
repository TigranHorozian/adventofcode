# -*- encoding: UTF-8 -*-
"""
Day7 source code

:Author: Tigran Horozian
:email: tigran.horozian@gmail.com
"""

import argparse
import IPython

def find_bottom_program(mylist):
    """
    Finds the only string that does not appear in a disk (aka bottom program)
    args : mylist -> the input list of elements
    returns : string -> the bottom program name
    """
    remove_nonbase = [elem for elem in mylist if '->' in elem]
    programs = [remove_nonbase[_].split(" (")[0] for _ in range(0, len(remove_nonbase))]
    notbase = [remove_nonbase[_].split("-> ")[1].split(", ") for _ in range(0, len(remove_nonbase))]
    flat_notbase = [item for sublist in notbase for item in sublist]
    for program in programs:
        if program not in flat_notbase:
            return program

if __name__ == '__main__':

    # Parse the file as arg
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=file, help='the file to read')
    args = parser.parse_args()

    #Read file and remove \n
    f = args.filename.readlines()
    for _ in range(0,len(f)):
        f[_] = f[_].split("\n")[0]

    print("Answer for first half is : "+ find_bottom_program(f))
