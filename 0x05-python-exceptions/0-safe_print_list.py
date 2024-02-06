#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    total_num = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            total_num += 1
        except IndexError:
            break
    print()
    return(total_num)
