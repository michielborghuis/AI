import random


steps = []
for plays in range(1):
    def all_possibilities():
        lst1 = [1, 2, 3, 4, 5, 6]

        all_pos = [[a, b, c, d] for a in lst1 for b in lst1
                   for c in lst1 for d in lst1] # alle mogelijke combinaties
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


    def feedback(guess, solution):
        white = white_pins(guess, solution)
        black = black_pins(guess, solution)
        white -= black  # als een pin zwart is hij in dit algoritme ook wit
        return [black, white]


    def remover(all_pos1, solution, guess):
        for i in all_pos1[:]:
            if feedback(guess, i) != feedback(guess, solution):
                all_pos1.remove(i)
        print(len(all_pos1))
        return all_pos1


    def graph(all_pos1, all_pos2):
        maximum = {}
        for i in all_pos2:
            nul_nul = 0
            nul_een = 0
            nul_twee = 0
            nul_drie = 0
            nul_vier = 0
            een_nul = 0
            een_een = 0
            een_twee = 0
            een_drie = 0
            twee_nul = 0
            twee_een = 0
            twee_twee = 0
            drie_nul = 0
            vier_nul = 0
            for j in all_pos1:
                if feedback(i, j) == [0, 0]:
                    nul_nul += 1
                if feedback(i, j) == [0, 1]:
                    nul_een += 1
                if feedback(i, j) == [0, 2]:
                    nul_twee += 1
                if feedback(i, j) == [0, 3]:
                    nul_drie += 1
                if feedback(i, j) == [0, 4]:
                    nul_vier += 1
                if feedback(i, j) == [1, 0]:
                    een_nul += 1
                if feedback(i, j) == [1, 1]:
                    een_een += 1
                if feedback(i, j) == [1, 2]:
                    een_twee += 1
                if feedback(i, j) == [1, 3]:
                    een_drie += 1
                if feedback(i, j) == [2, 0]:
                    twee_nul += 1
                if feedback(i, j) == [2, 1]:
                    twee_een += 1
                if feedback(i, j) == [2, 2]:
                    twee_twee += 1
                if feedback(i, j) == [3, 0]:
                    drie_nul += 1
                if feedback(i, j) == [4, 0]:
                    vier_nul += 1
            #temp_lijst = [str(i), nul_nul, nul_een, nul_twee, nul_drie, nul_vier, een_nul, een_een, een_twee, een_drie, twee_nul, twee_een, twee_twee, drie_nul, vier_nul]
            update = {tuple(i) : max(nul_nul, nul_een, nul_twee, nul_drie, nul_vier, een_nul, een_een, een_twee, een_drie, twee_nul, twee_een, twee_twee, drie_nul, vier_nul)}
            maximum.update(update)
        next_guess = list(min(maximum, key=maximum.get))
        return next_guess



    def play(all_pos1, all_pos2):
        count = 0
        solution = []
        all_guesses = []
        all_pins = []
        for i in range(0, 4):
            solution.append(random.randrange(1, 7))
        print(solution)
        next_guess = [1, 1, 2, 2]
        while next_guess != solution:
            all_guesses.append(next_guess)
            all_pins.append(feedback(next_guess, solution))
            count += 1
            remover(all_pos1, solution, next_guess)

            if len(all_pos1) == 1:
                next_guess = all_pos1[0]
            else:
                next_guess = graph(all_pos1, all_pos2)

            print('Je huidige bord ziet er zo uit:')
            for i, j in zip(all_guesses, all_pins):
                print('Kleuren: {} pinnen: {}'.format(i, j))
        print('Kleuren: {} pinnen: {}'.format(next_guess, feedback(next_guess, solution)))
        print('In {} stappen.'.format(count+1))
        return count+1

    steps.append(play(all_pos1, all_pos2))


print('minimale aantal stappen = ' + str(min(steps)))
print('maximale aantal stappen = ' + str(max(steps)))
print('gemiddeld aantal stappen = ' + str(sum(steps)/len(steps)))