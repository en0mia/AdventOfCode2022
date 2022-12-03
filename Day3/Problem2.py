import sys


# Problem link: https://adventofcode.com/2022/day/3
def main():
    filename = sys.argv[1]
    f = open(filename, 'r')

    final_value = 0

    lines = f.readlines()

    i = 0
    while i < len(lines) - 2:
        duplicate = find_duplicates(lines, i)
        final_value += get_priority(duplicate)

        i += 3

    print(f'Final priority: %d' % final_value)


def find_duplicates(lines, index):
    for char in lines[index]:
        if char in lines[index + 1] and char in lines[index + 2]:
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
