import sys


# Problem link: https://adventofcode.com/2022/day/2
def main():
    filename = sys.argv[1]
    f = open(filename, 'r')
    my_points = 0

    # Points for each move
    points = {'X': 1, 'Y': 2, 'Z': 3, 'A': 1, 'B': 2, 'C': 3}

    # What move should I choose to win?
    moves_winners = {'A': 'Y', 'B': 'Z', 'C': 'X'}

    # What move should I choose to lose?
    moves_losers = {'A': 'Z', 'B': 'X', 'C': 'Y'}
    for line in f:
        line = line.strip()
        if line == '':
            break
        moves = line.split(' ')
        round_end = moves[1]

        if round_end == 'X':
            # I need to lose
            my_points += 0 + points[moves_losers[moves[0]]]
        elif round_end == 'Y':
            # We need to end in a draw
            my_points += 3 + points[moves[0]]
        else:
            # I need to win
            my_points += 6 + points[moves_winners[moves[0]]]

    f.close()
    print(f'The final result is: %d' % my_points)


if __name__ == '__main__':
    main()
