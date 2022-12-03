"""
Codebreaker
"""


def dr_test(x, y, box, code, old_guesses, count):
    for e in range(x):
        guess_code = []
        hint = []
        print('Pick from R, B, Y, G, O, or P')
        print('Type quit to end early')
        for i in range(y):
            guess = (input(f'Guess the {i + 1} position: ')).upper()
            if guess == 'QUIT':
                return print("You ended early, better luck next time")
            while guess not in set(box):
                print('Invalid input. Guess must be from R, B, Y, G, O or P')
                guess = (input(f'Guess the {i + 1} position: ')).upper()
            guess_code.append(guess)
        guess_copy = guess_code.copy()
        code_copy = code.copy()
        for i, e in enumerate(guess_copy):
            if guess_copy[i] == code_copy[i]:
                hint.append('Black')
            elif guess_copy[i] in code_copy:
                hint.append('White')
            else:
                hint.append('-')
        old_guesses.update({
            str(guess_code): hint
        })
        print('Hints: Black means a guess is correct AND in the correct position')
        print('Hints: White means a guess is correct BUT in the wrong position')
        for key, value in old_guesses.items():
            print(key, value)
        count += 1
        if guess_code == code:
            return print('Congrats! You correctly guessed',
                         f' {code} in {count} attempts!')
    return print(f'Unlucky! You failed to guess {code}',
                 f'in {count} attempts')


def codebreaker():
    import random
    x = 0
    y = 0
    count = 0
    code = []
    guess_code = []
    old_guesses = {}
    box = ['R', 'R', 'R', 'R', 'R', 'R',
           'R', 'R', 'R', 'R', 'R', 'R',
           'B', 'B', 'B', 'B', 'B', 'B',
           'B', 'B', 'B', 'B', 'B', 'B',
           'Y', 'Y', 'Y', 'Y', 'Y', 'Y',
           'Y', 'Y', 'Y', 'Y', 'Y', 'Y',
           'G', 'G', 'G', 'G', 'G', 'G',
           'G', 'G', 'G', 'G', 'G', 'G',
           'O', 'O', 'O', 'O', 'O', 'O',
           'O', 'O', 'O', 'O', 'O', 'O',
           'P', 'P', 'P', 'P', 'P', 'P',
           'P', 'P', 'P', 'P', 'P', 'P']
    random.shuffle(box)
    while x < 1:
        try:
            x = int(input('How many guesses would you like to attempt?: '))
        except ValueError:
            print(f'Invalid input, use an integer greater than 0')
    while y not in range(1, 72):
        try:
            y = int(input('How long do you want the code? (From 1 to 72): '))
        except ValueError:
            print(f'Invalid input, use an integer from 1 to 72')
    code = box[:y]
    dr_test(x,y,box,code,old_guesses,count)

if __name__ == '__main__':
    codebreaker()
