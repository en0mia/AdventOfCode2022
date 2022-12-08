import sys


def main():
    filename = sys.argv[1]
    f = open(filename, 'r')
    input_text = f.read().strip()
    f.close()

    i = 0
    while i < len(input_text):
        found = set()
        j = 0
        solution = -1
        while j < 4:
            if input_text[i + j] in found:
                break
            found.add(input_text[i + j])
            if len(found) == 4:
                solution = i + j + 1
                break
            j += 1
        if solution != -1:
            print(f'solution: %d' % solution)
            exit()
        i += 1


if __name__ == '__main__':
    main()
