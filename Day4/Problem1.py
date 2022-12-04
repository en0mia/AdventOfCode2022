import sys


def main():
    filename = sys.argv[1]
    f = open(filename, 'r')

    full_overlaps = 0

    for line in f:
        pairs = line.strip().split(',')
        pair1 = (int(pairs[0].split('-')[0]), int(pairs[0].split('-')[1]))
        pair2 = (int(pairs[1].split('-')[0]), int(pairs[1].split('-')[1]))

        if full_overlap(pair1, pair2):
            full_overlaps += 1

    print(f'Full overlaps: %d' % full_overlaps)


def full_overlap(pair1, pair2):
    if pair1[0] <= pair2[0] and pair1[1] >= pair2[1]:
        longest = pair1
        shortest = pair2
    else:
        longest = pair2
        shortest = pair1

    # Check if the longest contains the shortest
    if longest[0] <= shortest[0] and longest[1] >= shortest[1]:
        return True
    return False


if __name__ == '__main__':
    main()
