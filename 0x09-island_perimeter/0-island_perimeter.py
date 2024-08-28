#!/usr/bin/python3
"""
This script calculates the perimeter of an island in a grid.

It takes a 2D grid as input and returns the total perimeter of the island
"""


def is_land(row, column, grid):
    """
    Checks if a cell in the grid at given indices is land (1) and within grid
    bounds.

    Parameters:
    row (int): Row index of the cell.
    column (int): Column index of the cell.
    grid (list of list of int): 2D grid where 0 represents water and 1
    represents land.

    Returns:
    bool: `True` if the cell is land and within bounds, `False` otherwise.
    """

    if 0 <= row < len(grid) and 0 <= column < len(grid[0]):
        return grid[row][column] == 1
    return False


def cell_perimeter(row, column, grid):
    """
    Calculate the perimeter of a cell in a grid based on its adjacent cells.

    Parameters:
    row (int): The row index of the cell.
    column (int): The column index of the cell.
    grid (list of list of int): The 2D grid (1 represents land, 0 represents
    water).

    Returns:
    int: The calculated perimeter of the cell.
    """

    perimeter = 4
    if is_land(row - 1, column, grid):
        perimeter -= 1
    if is_land(row+1, column, grid):
        perimeter -= 1
    if is_land(row, column - 1, grid):
        perimeter -= 1
    if is_land(row, column + 1, grid):
        perimeter -= 1
    return perimeter


def island_perimeter(grid):
    """
    Calculate the total perimeter of the islands in a grid.

    Args:
        grid: 2D list representing the map (1 for land, 0 for water).

    Returns:
        int: Total perimeter of the island(s).
    """
    if not grid or not grid[0]:
        return 0
    perimeter = 0

    rows = len(grid)
    columns = len(grid[0])

    for row in range(rows):
        for col in range(columns):
            if grid[row][col] == 1:
                perimeter += cell_perimeter(row, col, grid)

    return perimeter
