import sys


def main():
    GOAL = 30000000
    TOTAL_SPACE = 70000000
    ROOT = 'ROOT'
    filename = sys.argv[1]
    f = open(filename, 'r')

    sizes = {}
    stack = []

    for line in f:
        if line.startswith('$ cd'):
            directory = line.split(' ')[2].strip()
            if directory == '..':
                stack.pop()
            else:
                if directory == '/':
                    stack.append(ROOT)
                else:
                    stack.append(directory)
        elif line[0].strip().isnumeric():
            size = int(line.split(' ')[0])
            for i in range(len(stack) - 1, -1, -1):
                path = '/'.join(stack[0:i+1])
                if path in sizes:
                    sizes[path] += size
                else:
                    sizes[path] = size
    sorted_sizes = list(sizes.values())
    sorted_sizes.sort()
    amount_need = GOAL - (TOTAL_SPACE - sizes[ROOT])

    for size in sorted_sizes:
        if size >= amount_need:
            print(size)
            break


if __name__ == '__main__':
    main()
