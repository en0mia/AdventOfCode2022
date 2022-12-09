import sys


def main():
    grid = []

    filename = sys.argv[1]
    f = open(filename, 'r')

    for line in f:
        grid.append(list(line.strip()))

    result = 0

    for r in range(1, len(grid) - 1):
        for c in range(1, len(grid[0]) - 1):
            current = grid[r][c]
            up_visible = True
            down_visible = True
            left_visible = True
            right_visible = True

            for j in range(r):
                if grid[j][c] >= current:
                    up_visible = False
                    break
            for k in range(r + 1, len(grid)):
                if grid[k][c] >= current:
                    down_visible = False
                    break
            for l in range(c):
                if grid[r][l] >= current:
                    left_visible = False
                    break
            for m in range(c + 1, len(grid[0])):
                if grid[r][m] >= current:
                    right_visible = False
                    break

            if up_visible or down_visible or left_visible or right_visible:
                result += 1
    result += len(grid) * 4 - 4
    print(result)


if __name__ == '__main__':
    main()
