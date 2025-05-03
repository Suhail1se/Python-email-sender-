import random
from collections import deque

WIDTH = 21
HEIGHT = 21

maze = [['#' for _ in range(WIDTH)] for _ in range(HEIGHT)]

def carve(x, y):
    dirs = [(0, -2), (2, 0), (0, 2), (-2, 0)]
    random.shuffle(dirs)
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 < nx < WIDTH and 0 < ny < HEIGHT and maze[ny][nx] == '#':
            maze[ny - dy // 2][nx - dx // 2] = ' '
            maze[ny][nx] = ' '
            carve(nx, ny)

def generate_maze():
    maze[1][1] = ' '
    carve(1, 1)
    maze[0][1] = 'S'
    maze[HEIGHT - 1][WIDTH - 2] = 'E'

generate_maze()

def print_maze():
    for row in maze:
        print(''.join(row))

def solve_maze():
    start = (0, 1)
    end = (HEIGHT - 1, WIDTH - 2)
    queue = deque([([start], start)])
    visited = set()
    while queue:
        path, (x, y) = queue.popleft()
        if (x, y) == end:
            return path
        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx, ny = x + dx, y + dy
            if 0 <= ny < HEIGHT and 0 <= nx < WIDTH:
                if maze[ny][nx] in (' ', 'E') and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((path + [(nx, ny)], (nx, ny)))
    return []

def mark_solution(path):
    for x, y in path:
        if maze[y][x] == ' ':
            maze[y][x] = '.'

solution = solve_maze()
mark_solution(solution)
print_maze()

def run_multiple_mazes(count):
    for _ in range(count):
        for y in range(HEIGHT):
            for x in range(WIDTH):
                maze[y][x] = '#'
        generate_maze()
        solution = solve_maze()
        mark_solution(solution)
        print_maze()
        print()

if __name__ == "__main__":
    run_multiple_mazes(3)
