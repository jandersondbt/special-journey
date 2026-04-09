guess = ['1', '0', '3']
secretNum = 1

try:
    count = 0 # Initialize counter before the loop
    while guess != secretNum:
        count += 1 # Increment at the start of each iteration
        print(secretNum)
        # ... rest of loop code ...
        secretNum += 1

except KeyboardInterrupt:
    print(f'Noooo! Loop ran {count} times')
