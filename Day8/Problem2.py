import sys


def main():
    grid = []

    filename = sys.argv[1]
    f = open(filename, 'r')

    for line in f:
        grid.append(list(line.strip()))

    max_visibility = 0

    for r in range(1, len(grid) - 1):
        for c in range(1, len(grid[0]) - 1):
            current = grid[r][c]
            up = 0
            down = 0
            left = 0
            right = 0

            j = r - 1
            while j >= 0:
                up += 1

                if grid[j][c] >= current:
                    break
                j -= 1

            k = r + 1
            while k < len(grid):
                down += 1

                if grid[k][c] >= current:
                    break
                k += 1

            n = c - 1
            while n >= 0:
                left += 1

                if grid[r][n] >= current:
                    break
                n -= 1

            m = c + 1
            while m < len(grid[0]):
                right += 1

                if grid[r][m] >= current:
                    break
                m += 1

            visibility = up * down * right * left

            if visibility > max_visibility:
                max_visibility = visibility

    print(max_visibility)


if __name__ == '__main__':
    main()
