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
    print(len(all_pos))
    return all_pos


#def most(all_pos, guess):
#    counter_dict = {}
#    for i in all_possibilities():
#        counter = 0
#        for j in all_pos:
#            if pins(i, guess) != pins(j, guess):
#                counter += 1
#            dict_update = {str(j) : counter}
#            counter_dict.update(dict_update)
#    return counter_dict

#print(most(all_pos, [1, 1, 2, 3]))
#counters_listt = most(all_pos, [1, 1, 2, 3])
#print(min(x[1] for x in counters_listt))


def play(all_pos):
    count = 0
    if len(all_pos) < 2:
        return count

    else:
        #solution = []
        #solution_input = input('Speler 1, geef de oplossing (vb. 2534): ')
        #for i in solution_input:
        #    solution.append(int(i))
        solution = [5, 6, 1, 2]
        guess = []
        while guess != solution:
            guess = []
            count += 1

            #for i in range(0, 4):
            #    guess.append(random.randrange(1, 7))

            guess_input = input('Speler 2, doe een gok (vb. 2534): ')
            for i in guess_input:
                guess.append(int(i))

            print(pins(guess, solution))
            print(remover(all_pos, solution, guess))
            #print(graph(remover(all_pos, solution, guess)))

        print('In {} stappen.'.format(count))

play(all_pos)