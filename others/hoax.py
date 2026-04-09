import random
import time

def getSecretNum():
    l = [1, 2, 3, 4, 5]
    s_num = []
    for i in range(0, 3):
        s_num += str(l[i])
    
    random.shuffle(s_num)
    return s_num

print(getSecretNum())

guess = ['1', '1', '2']
secretNum = getSecretNum()


if guess == secretNum:
    print('You got it!!!!!!!!!!')

count = 0
start = time.time()
try:
    while guess != secretNum:
        count += 1
        secretNum = getSecretNum()
        print(secretNum)

except KeyboardInterrupt:
    elapsed = time.time() - start
    print('Nooooo')
    print(f"Looped about {count} times")
    print(f"time elapsed: {elapsed:.2f} seconds")
