word = 'Chemistry on and On'

# COLORS
red = '\033[31m'
blue = '\033[34m'
green = '\033[32m'

RESET = '\033[0m'
YELLOW = '\033[33m'
underline = '\033[4m'
print(f'\033[92m {word} {RESET} lula')

print(red + 'hello')
print(green + 'Yes')

print(red + 'Error')
print(green + 'Sucess')

print(underline + word)

print(underline + YELLOW + word)
