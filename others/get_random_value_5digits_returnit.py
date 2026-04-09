'''
Retrieve the first three values from a specified list.    
'''

import random

def get_three(l):
    void = []

    for i in range(0, 3):
        void += str(l[i])

    random.shuffle(void)
    return void

print(get_three([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
