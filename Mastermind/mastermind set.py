def all_possibilities():
    lst1 = [1, 2, 3, 4, 5, 6]
    lst2 = [1, 2, 3, 4, 5, 6]
    lst3 = [1, 2, 3, 4, 5, 6]
    lst4 = [1, 2, 3, 4, 5, 6]

    all_pos = [[a, b, c, d] for a in lst1 for b in lst2
               for c in lst3 for d in lst4] # alle mogelijke combinaties
    return all_pos

all_pos = all_possibilities()

def black_pins(guess, solution):
    counter = 0
    print(guess)
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
        if pins(i, solution) != pins(guess, solution):
            all_pos.remove(i)
    print(len(all_pos))
    return all_pos



def play():
    solution = []
    #solution_input = input('Speler 1, geef de oplossing (vb. 2 5 3 4): ')
    #for i in solution_input:
    #    solution.append(int(i))
    solution = [1, 2, 3, 4]
    guess = []
    while guess != solution:
        guess = []
        guess_input = input('Speler 2, doe een gok (vb. 2534): ')
        for i in guess_input:
            guess.append(int(i))
        print(pins(guess, solution))
        print(remover(all_pos, solution, guess))

play()