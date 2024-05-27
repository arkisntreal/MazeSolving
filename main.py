from graphics import Window, Line, Point
from cell import Cell
from maze import Maze

def main():
    MazeWindow = Window(400, 400)

    maze = Maze(50, 50, 5, 5, 60, 60, MazeWindow)

    maze.solve()

    MazeWindow.wait_for_close()

if __name__ == "__main__":
    main()
