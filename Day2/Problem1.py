import sys


# Problem link: https://adventofcode.com/2022/day/2
def main():
    filename = sys.argv[1]
    f = open(filename, 'r')
    my_points = 0

    # Points for each move
    points = {'X': 1, 'Y': 2, 'Z': 3, 'A': 1, 'B': 2, 'C': 3}

    # What move wins?
    moves_winners = {'A': 'Y', 'B': 'Z', 'C': 'X'}

    for line in f:
        line = line.strip()
        if line == '':
            break
        moves = line.split(' ')
        my_points += points[moves[1]]

        if points[moves[1]] == points[moves[0]]:
            # The round was a draw
            my_points += 3
            continue

        if moves[1] == moves_winners[moves[0]]:
            # I won
            my_points += 6

    f.close()
    print(f'The final result is: %d' % my_points)


if __name__ == '__main__':
    main()
