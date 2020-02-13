import random

def all_possibilities():
    lst1 = [1, 2, 3, 4, 5, 6]
    lst2 = [1, 2, 3, 4, 5, 6]
    lst3 = [1, 2, 3, 4, 5, 6]
    lst4 = [1, 2, 3, 4, 5, 6]

    all_pos = [[a, b, c, d] for a in lst1 for b in lst2
               for c in lst3 for d in lst4] # alle mogelijke 6**4 ofwel 1296 combinaties
    return all_pos

all_pos = all_possibilities()

def black_pins(guess, solution):
    counter = 0
    for pin in range(len(guess)):
        if guess[pin] == solution[pin]:
            counter += 1
    return counter


def white_pins(guess, solution):
    temp_solution = solution[:]
    counter = 0
    for pin in guess:
        if pin in temp_solution:
            temp_solution.remove(pin) # voorkomt dat er een witte pin wordt toegevoegd doordat een kleur die vaker
                                        # voorkomt in guess een kleur is die minder vaak voorkomt in de solution
            counter += 1
    return counter


def pins(guess, solution):
    white = white_pins(guess, solution)
    black = black_pins(guess, solution)
    white -= black  # als een pin zwart is hij in dit algoritme ook wit
    return [black, white]


def remover(all_pos, solution, guess):
    for i in all_pos[:]:
        if pins(guess, i) != pins(guess, solution):
            all_pos.remove(i)
    #print(len(all_pos))
    return all_pos


def play(all_pos):
    count = 0
    solution = []
    all_guesses = []
    all_pins = []
    for i in range(0, 4):
        solution.append(random.randrange(1, 7))
    guess = []
    while guess != solution:
        guess = []
        count += 1
        guess_input = input('Speler 2, doe een gok (vb. 2534): ')
        for i in guess_input:
            guess.append(int(i))

        all_guesses.append(guess)
        all_pins.append(pins(guess, solution))
        (remover(all_pos, solution, guess))
        #print(graph(remover(all_pos, solution, guess)))
        print('Je huidige bord ziet er zo uit:')
        for i, j in zip(all_guesses, all_pins):
            print('Kleuren: {} pinnen: {}'.format(i, j))
    print('In {} stappen.'.format(count))

play(all_pos)