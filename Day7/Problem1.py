import sys


def main():
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
                path = '/'.join(stack[0:i + 1])
                if path in sizes:
                    sizes[path] += size
                else:
                    sizes[path] = size
    result = sum(size for size in sizes.values() if size < 10**5)
    print(f'Result: %d' % result)


if __name__ == '__main__':
    main()
