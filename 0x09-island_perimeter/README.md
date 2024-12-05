# Island Perimeter

This project calculates the perimeter of an island in a 2D grid.

## Requirements
- Python 3.4.3
- Ubuntu 20.04 LTS
- No external modules allowed

## Usage
To use the `island_perimeter` function, provide a grid (list of lists) where:
- `0` represents water.
- `1` represents land.

Example:
```python
grid = [
    [0, 1, 0],
    [1, 1, 0],
    [0, 1, 0]
]
print(island_perimeter(grid))  # Output: 8

