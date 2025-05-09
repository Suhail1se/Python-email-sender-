import heapq
import random

# Constants
WIDTH = 20
HEIGHT = 20
WALL_PROB = 0.3

# Generate a random maze
def generate_maze(width, height, wall_prob):
    maze = []
    for y in range(height):
        row = []
        for x in range(width):
            if random.random() < wall_prob:
                row.append(1)
            else:
                row.append(0)
        maze.append(row)
    maze[0][0] = 0
    maze[height - 1][width - 1] = 0
    return maze

# Heuristic function: Manhattan distance
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* algorithm
def astar(maze, start, goal):
    neighbors = [(0,1), (1,0), (-1,0), (0,-1)]
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start, [start]))
    visited = set()
    
    while open_set:
        est_total_cost, cost, current, path = heapq.heappop(open_set)
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for dx, dy in neighbors:
            nx, ny = current[0] + dx, current[1] + dy
            if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze):
                if maze[ny][nx] == 0 and (nx, ny) not in visited:
                    new_cost = cost + 1
                    heapq.heappush(open_set, (
                        new_cost + heuristic((nx, ny), goal),
                        new_cost,
                        (nx, ny),
                        path + [(nx, ny)]
                    ))
    return None

# Print maze with path
def print_maze_with_path(maze, path):
    for y in range(len(maze)):
        row = ""
        for x in range(len(maze[0])):
            if (x, y) == (0, 0):
                row += "S "
            elif (x, y) == (len(maze[0]) - 1, len(maze) - 1):
                row += "G "
            elif (x, y) in path:
                row += "* "
            elif maze[y][x] == 1:
                row += "█ "
            else:
                row += ". "
        print(row)

# Main
def main():
    maze = generate_maze(WIDTH, HEIGHT, WALL_PROB)
    start = (0, 0)
    goal = (WIDTH - 1, HEIGHT - 1)
    path = astar(maze, start, goal)
    
    print("MazeSolverAI - A* Pathfinding\n")
    if path:
        print_maze_with_path(maze, path)
        print(f"\n✅ Path found! Steps: {len(path)}")
    else:
        print_maze_with_path(maze, [])
        print("\n❌ No path found.")

if __name__ == "__main__":
    main()
