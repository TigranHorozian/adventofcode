# -*- encoding: UTF-8 -*-
"""
Day5 source code

:Author: Tigran Horozian
:email: tigran.horozian@gmail.com
"""
import argparse


if __name__ == '__main__':

    # Parse the file as arg
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=file, help='the file to read')
    args = parser.parse_args()

    #Vars
    f = args.filename.readlines()
    result1 = 0
    result2 = 0



    print("first half is : " + str(result1))
    print("second half is : " + str(result2))
