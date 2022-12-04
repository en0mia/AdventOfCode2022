import sys


def main():
    filename = sys.argv[1]
    f = open(filename, 'r')

    overlaps = 0

    for line in f:
        pairs = line.strip().split(',')
        pair1 = (int(pairs[0].split('-')[0]), int(pairs[0].split('-')[1]))
        pair2 = (int(pairs[1].split('-')[0]), int(pairs[1].split('-')[1]))

        if overlap(pair1, pair2):
            overlaps += 1

    print(f'Full overlaps: %d' % overlaps)


def overlap(pair1, pair2):
    return pair1[0] <= pair2[1] and pair1[1] >= pair2[0]


if __name__ == '__main__':
    main()
