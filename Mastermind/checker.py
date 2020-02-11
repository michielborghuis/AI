def count_white(ans, guess):
    temp_ans = ans[:]
    pegs = 0
    for i in guess:
        if i in temp_ans:
            temp_ans.remove(i)
            pegs += 1
    return pegs

def count_black(ans, guess):
    return sum([ans[i] == guess[i] for i in range(len(ans))])

def check(ans, guess):
    white = count_white(ans, guess)
    black = count_black(ans, guess)
    white -= black

    print(black,"black pegs")
    print(white,"white pegs")

    return black == 4
ans = [1, 2, 3, 4]
guess = [6, 6, 6, 6]

check(ans, guess)