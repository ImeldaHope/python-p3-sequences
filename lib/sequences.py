#!/usr/bin/env python3

def print_fibonacci(length):
    n1,n2 = 0,1    

    my_list = []
    for _ in range(0, length):
        my_list.append(n1)
        n1,n2 = n2, n1 + n2
            
    print(my_list)        

