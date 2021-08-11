import random
from termcolor import colored
from noise import pnoise2


def generate_land(rows=10, cols=10, noise_level=10):
    data = ['!', '-', '.', '-', '.', ' ', '.', '#', '.', '-', '!']
    seed = random.randint(0, 100)
    land = ''
    print(f'we want to generate a landscape which is {cols} by {rows}')

    for row in range(rows):
        for col in range(cols):
            n = pnoise2(row / rows, col / cols, base=seed, octaves=5)
            n *= noise_level
            n = round(n)
            n = n % len(data)

            land += data[n]
        land += '\n'

    print('Finished generating landscape')
    return land


def ask_for_number(question):
    tries = 0

    while tries < 3:
        answer = input(colored(question + '\n', 'green'))
        if answer == 'quit':
            quit()
        elif answer.isnumeric():
            return int(answer)
        else:
            tries += 1
            print(colored("error", 'yellow'))

    print(colored('Quitting now', 'red'))
    quit()


if __name__ == '__main__':
    rows = ask_for_number("How many rows? ")
    cols = ask_for_number("How many cols? ")

    output = generate_land(cols, rows)
    print(output)
