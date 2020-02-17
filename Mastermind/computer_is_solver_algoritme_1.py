import random

steps = []
for i in range(1000):
    def all_possibilities():
        lst1 = [1, 2, 3, 4, 5, 6]

        all_pos = [[a, b, c, d] for a in lst1 for b in lst1
                   for c in lst1 for d in lst1] # alle mogelijke combinaties
        return all_pos

    all_pos1 = all_possibilities()

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
        #print(len(all_pos1))
        return all_pos1


    def play(all_pos1):
        count = 0
        solution = []
        for i in range(0, 4):
            solution.append(random.randrange(1, 7))
        guess = []
        while guess != solution:
            count += 1
            if len(all_pos1) == 2:
                guess = all_pos1[0]
            elif len(all_pos1) == 1:
                guess = all_pos1[0]
            else:
                guess = random.choice(all_pos1)

            pins(guess, solution)
            remover(all_pos1, solution, guess)

        return count

    steps.append(play(all_pos1))

print('minimale aantal stappen = ' + str(min(steps)))
print('maximale aantal stappen = ' + str(max(steps)))
print('gemiddeld aantal stappen = ' + str(sum(steps)/len(steps)))

print(pins([1, 1, 1, 2], [5, 2, 5, 5]))