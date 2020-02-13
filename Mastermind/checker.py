import random


def all_possibilities():
    lst1 = [1, 2, 3, 4, 5, 6]
    lst2 = [1, 2, 3, 4, 5, 6]
    lst3 = [1, 2, 3, 4, 5, 6]
    lst4 = [1, 2, 3, 4, 5, 6]

    all_pos = [[a, b, c, d] for a in lst1 for b in lst2
               for c in lst3 for d in lst4] # alle mogelijke combinaties
    return all_pos

all_pos1 = all_possibilities()
all_pos2 = all_possibilities()

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


def remover(all_pos1, solution, guess):
    for i in all_pos1[:]:
        if pins(guess, i) != pins(guess, solution):
            all_pos1.remove(i)
    print(len(all_pos1))
    return all_pos1


def best_choise(all_pos1, all_pos2, guess):
    number_of_cancellations = {}
    for i in all_pos1:
        counter = 0
        for j in all_pos2:
            if pins(guess, i) != pins(guess, j):
                counter += 1
                update = {str(i) : counter}
                number_of_cancellations.update(update)
    return number_of_cancellations



def play(all_pos1):
    count = 0
    solution = []
    solution_input = input('Speler 1, geef de oplossing (vb. 2534): ')
    for i in solution_input:
        solution.append(int(i))
    guess = []
    while guess != solution:
        count += 1                                      #5656, 1122 geeft 256, 1333 geeft 81
        if len(all_pos1) == 2:
            guess = all_pos1[0]
        elif len(all_pos1) == 1:
            guess = all_pos1[0]
        else:
            guess = []
            #for i in range(0, 4):
            #    guess.append(random.randrange(1, 7))
            guess_input = input('Speler 2, doe een gok (vb. 2534): ')
            for i in guess_input:
                guess.append(int(i))

            temp_dict = best_choise(all_pos1, all_pos2, guess)

            print(best_choise(all_pos1, all_pos2, guess))
            print('------------------------------------------------')
            print(min(temp_dict, key=temp_dict.get))
            print('------------------------------------------------')
            next_guess = max(temp_dict, key=temp_dict.get)

            print(pins(next_guess, solution))
            print(remover(all_pos1, solution, guess))
            #print(graph(remover(all_pos1, solution, guess)))

    print('In {} stappen.'.format(count))

play(all_pos1)