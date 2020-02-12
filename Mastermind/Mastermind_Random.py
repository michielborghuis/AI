import random

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


aantal_runs = 1000
solution_input = input('Speler 1, geef de oplossing (vb. 2 5 3 4): ')
stappen_counter = 0
for i in range(aantal_runs):
    solution = []
    for i in solution_input:
        solution.append(int(i))
    guess = []
    count = 0
    while guess != solution:
        count += 1
        guess = []
        for i in range(0, 4):
            guess.append(random.randrange(1, 7))
        pins(guess, solution)
    stappen_counter += count

gem = stappen_counter/aantal_runs
print(gem)

#gemiddeld ongeveer 1300 stappen