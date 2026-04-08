give_n = 11
user_n = 0

while user_n < give_n:
    try:
        user_n = int(input('Enter a number: '))    
    except ValueError:
        print('Not a number') 
