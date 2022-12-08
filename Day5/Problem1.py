import sys


def main():
    filename = sys.argv[1]
    f = open(filename, 'r')

    stacks = []
    lines = f.readlines()
    line_counter = 0
    for line in lines:
        if line.strip() == '':
            break
        i = 0
        stack_counter = 0
        while i < len(line):
            current = line[i:i + 3]
            if len(stacks) <= stack_counter:
                stacks.append([])
            if '[' in current:
                element = current[1]
                stacks[stack_counter].append(element)
            stack_counter += 1
            i += 4
        line_counter += 1

    for stack in stacks:
        stack.reverse()

    for i in range(line_counter + 1, len(lines)):
        split = lines[i].split(' ')
        qty = int(split[1])
        from_stack = int(split[3]) - 1
        to_stack = int(split[5]) - 1

        for j in range(qty):
            stacks[to_stack].append(stacks[from_stack].pop())
    result = ''
    for stack in stacks:
        result += stack.pop()
    print(result)


if __name__ == '__main__':
    main()
