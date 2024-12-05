def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.

    Args:
        grid (list of list of int): A rectangular grid where
                                    0 represents water and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Land cell
                # Check all four sides
                # Check above
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Check below
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Check left
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Check right
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter

