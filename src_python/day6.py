# -*- encoding: UTF-8 -*-
"""
Day6 source code

:Author: Tigran Horozian
:email: tigran.horozian@gmail.com
"""

puzzle = [11,11,13,7,0,15,5,5,4,4,1,1,7,1,15,11]

def detect_already_seen_state(states):
    states_set = set(map(tuple,states))  #need to convert the inner lists to tuples so they are hashable
    no_duplicates = map(list,states_set)
    if len(states) != len(no_duplicates):
        return True
    return False

def reallocate_banks(input_puzzle):
    states = [input_puzzle]
    result = 0
    nextstate = []

    while not detect_already_seen_state(states):
        nextstate = list(states[-1]) #copy the last list

        #determine max in list and get index
        m = max(states[-1])
        maxpos = [i for i, j in enumerate(nextstate) if j == m]
        index = maxpos[0]

        #reallocate
        nextstate[index] = 0
        for _ in range(1, m+1):
            if index + _ < len(nextstate):
                nextstate[index + _] += 1
            else:
                nextstate[index + _ - len(nextstate)] += 1

        #save state, increment result
        states.append(nextstate)
        result +=1

    return result

if __name__ == '__main__':
        print("Answer for first half is : " + str(reallocate_banks(puzzle)))
