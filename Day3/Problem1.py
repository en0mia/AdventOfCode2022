import sys


# Problem link: https://adventofcode.com/2022/day/3
def main():
    filename = sys.argv[1]
    f = open(filename, 'r')

    final_value = 0

    for line in f:
        line = line.strip()
        duplicate = find_duplicates(line)

        final_value += get_priority(duplicate)

    print(f'Final priority: %d' % final_value)


def find_duplicates(line):
    length = len(line)
    first = line[0:int(length/2)]
    second = line[int(length/2):length]

    for char in first:
        if char in second:
            return char
    return None


def get_priority(char):
    LOWERCASE_OFFSET = 1
    UPPERCASE_OFFSET = 27

    priority = 0

    if char is None:
        priority = 0
    elif char.islower():
        priority = ord(char) - ord('a') + LOWERCASE_OFFSET
    elif char.isupper():
        priority = ord(char) - ord('A') + UPPERCASE_OFFSET
    return priority


if __name__ == '__main__':
    main()
