import random

void = []
numbers = list('12320202020201')
print(numbers)

random.shuffle(numbers)

print(numbers)


#
#


# Get first symbols elements from list


for i in range(3): # For item till 3rd item
    void += str(numbers[i]) # Void add elements from first to third element

print(void)
