# -*- coding: utf-8 -*
"""
Coding, decoding and correction of linear binary strings with the method of Hamming codes.
4x4 scenario (11 bit + 5 bits for parity check), maximal 2 errors.
"""
from functools import reduce


def youtube_3b1b_hamming_check(clist: list):
    """
    https://www.youtube.com/watch?v=b3NxrZOu_CE
    return the position of the error
    """
    return reduce(lambda x, y: x ^ y, [i for (i, bit) in enumerate(clist) if bit])


def ma_hamming_coding(clist: list):
    """
    add 5 parity codes in position of 1,2,3,5,9 (a1,a2,a3,b1,c1) in a 4x4 array
    """
    # add a2
    if sum([clist[0], clist[1], clist[3], clist[4], clist[6], clist[8], clist[10]]) % 2 == 0:
        clist.insert(0, 0)
    else:
        clist.insert(0, 1)

    # add a3
    if sum([clist[1], clist[3], clist[4], clist[6], clist[7], clist[10], clist[11]]) % 2 == 0:
        clist.insert(1, 0)
    else:
        clist.insert(1, 1)

    # add b1
    if sum([clist[3], clist[4], clist[5], clist[9], clist[10], clist[11], clist[12]]) % 2 == 0:
        clist.insert(3, 0)
    else:
        clist.insert(3, 1)

    # add c1
    if sum([clist[7], clist[8], clist[9], clist[10], clist[11], clist[12], clist[13]]) % 2 == 0:
        clist.insert(7, 0)
    else:
        clist.insert(7, 1)

    # add a1
    if sum(clist) % 2 == 0:
        clist.insert(0, 0)
    else:
        clist.insert(0, 1)

    return clist


def ma_hamming_decoding(dlist: list):
    """
    verify if error exists: if has 1 error then correct it, if has 2 then report
    """

    a2 = 0
    a3 = 0
    b1 = 0
    c1 = 0
    # check a2
    if sum([dlist[1], dlist[3], dlist[5], dlist[7], dlist[9], dlist[11], dlist[13], dlist[15]]) % 2 != 0:
        a2 = 1

    # check a3
    if sum([dlist[2], dlist[3], dlist[6], dlist[7], dlist[10], dlist[11], dlist[14], dlist[15]]) % 2 != 0:
        a3 = 1

    # check b1
    if sum([dlist[4], dlist[5], dlist[6], dlist[7], dlist[12], dlist[13], dlist[14], dlist[15]]) % 2 != 0:
        b1 = 1

    # check c1
    if sum([dlist[8], dlist[9], dlist[10], dlist[11], dlist[12], dlist[13], dlist[14], dlist[15]]) % 2 != 0:
        c1 = 1

    # check a1 and correct the error or report multiple errors
    if sum(dlist) % 2 != 0 and a2 + a3 + b1 + c1 == 0:
        dlist[0] = (dlist[0] + 1) % 2
    elif sum(dlist) % 2 == 0 and a2 + a3 + b1 + c1 == 1:
        print("\n2 errors occurred at (a1,a2) or (a1,a3) or (a1,b1) or (a1,c1) or (a3,a4) or (c1,d1).")
    elif sum(dlist) % 2 == 0 and a2 + a3 + b1 + c1 >= 2:
        print("\n2 errors occurred at unknown position.")
    elif sum(dlist) % 2 == 0 and a2 + a3 + b1 + c1 == 0:
        print("\nno error.")
    else:
        if a2 == 1 and a3 == 0 and b1 == 0 and c1 == 0:
            print('\nerror at a2.')
            dlist[1] = (dlist[1] + 1) % 2
        elif a2 == 0 and a3 == 1 and b1 == 0 and c1 == 0:
            print('\nerror at a3')
            dlist[2] = (dlist[2] + 1) % 2
        elif a2 == 1 and a3 == 1 and b1 == 0 and c1 == 0:
            print('\nerror at a4.')
            dlist[3] = (dlist[3] + 1) % 2
        elif a2 == 0 and a3 == 0 and b1 == 1 and c1 == 0:
            print('\nerror at b1.')
            dlist[4] = (dlist[4] + 1) % 2
        elif a2 == 1 and a3 == 0 and b1 == 1 and c1 == 0:
            print('\nerror at b2.')
            dlist[5] = (dlist[5] + 1) % 2
        elif a2 == 0 and a3 == 1 and b1 == 1 and c1 == 0:
            print('\nerror at b3')
            dlist[6] = (dlist[6] + 1) % 2
        elif a2 == 1 and a3 == 1 and b1 == 1 and c1 == 0:
            print('\nerror at b4')
            dlist[7] = (dlist[7] + 1) % 2
        elif a2 == 0 and a3 == 0 and b1 == 0 and c1 == 1:
            print('\nerror at c1')
            dlist[8] = (dlist[8] + 1) % 2
        elif a2 == 1 and a3 == 0 and b1 == 0 and c1 == 1:
            print('\nerror at c2')
            dlist[9] = (dlist[9] + 1) % 2
        elif a2 == 0 and a3 == 1 and b1 == 0 and c1 == 1:
            print('\nerror at c3')
            dlist[10] = (dlist[10] + 1) % 2
        elif a2 == 1 and a3 == 1 and b1 == 0 and c1 == 1:
            print('\nerror at c4')
            dlist[11] = (dlist[11] + 1) % 2
        elif a2 == 0 and a3 == 0 and b1 == 1 and c1 == 1:
            print('\nerror at d1')
            dlist[12] = (dlist[12] + 1) % 2
        elif a2 == 1 and a3 == 0 and b1 == 1 and c1 == 1:
            print('\nerror at d2')
            dlist[13] = (dlist[13] + 1) % 2
        elif a2 == 0 and a3 == 1 and b1 == 1 and c1 == 1:
            print('\nerror at d3')
            dlist[14] = (dlist[14] + 1) % 2
        else:
            print('\nerror at d4')
            dlist[15] = (dlist[15] + 1) % 2

    return dlist


if __name__ == "__main__":
    import random
    import time

    startt = time.time()
    # generate random 11 bits list
    created_list = []
    for i in range(11):
        created_list.append(random.choice([0, 1]))

    # display coded list in grid form
    coded_list = ma_hamming_coding(created_list)
    print('coded list:', coded_list)
    print(coded_list[0], '-', coded_list[1], '-', coded_list[2], '-', coded_list[3])
    print(coded_list[4], '-', coded_list[5], '-', coded_list[6], '-', coded_list[7])
    print(coded_list[8], '-', coded_list[9], '-', coded_list[10], '-', coded_list[11])
    print(coded_list[12], '-', coded_list[13], '-', coded_list[14], '-', coded_list[15], '\n')

    # generate random error(s)
    nerror = random.choice([0, 1, 2])
    print("error(s) number:", nerror)
    for i in range(nerror):
        lerror = random.randint(0, 15)
        print("error location:", lerror)
        coded_list[lerror] = (coded_list[lerror] + 1) % 2
    print(coded_list[0], '-', coded_list[1], '-', coded_list[2], '-', coded_list[3])
    print(coded_list[4], '-', coded_list[5], '-', coded_list[6], '-', coded_list[7])
    print(coded_list[8], '-', coded_list[9], '-', coded_list[10], '-', coded_list[11])
    print(coded_list[12], '-', coded_list[13], '-', coded_list[14], '-', coded_list[15])

    # display decoded list in grid form
    decoded_list = ma_hamming_decoding(coded_list)
    print('decoded list:', decoded_list)
    print(decoded_list[0], '-', decoded_list[1], '-', decoded_list[2], '-', decoded_list[3])
    print(decoded_list[4], '-', decoded_list[5], '-', decoded_list[6], '-', decoded_list[7])
    print(decoded_list[8], '-', decoded_list[9], '-', decoded_list[10], '-', decoded_list[11])
    print(decoded_list[12], '-', decoded_list[13], '-', decoded_list[14], '-', decoded_list[15], '\n')

    endt = time.time()
    print('time taken:', endt - startt)
