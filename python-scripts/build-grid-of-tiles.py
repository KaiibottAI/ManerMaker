import os
import random

# Define the path to your tiles folder
TILE_FOLDER = "D:\house-on-the-hill\pre-done-house-tiles - resized"
GRID_SIZE = 5

# Parse tile data from filenames
class Tile:
    def __init__(self, filename):
        self.filename = filename
        parts = filename.split('-')
        self.id = parts[1]
        self.type = parts[2]
        self.doors_str = parts[3].split('.')[0]
        self.doors = {
            'N': int(self.doors_str[0]),
            'E': int(self.doors_str[1]),
            'S': int(self.doors_str[2]),
            'W': int(self.doors_str[3])
        }

    def __repr__(self):
        return f"{self.filename}({self.doors_str})"

# Load and parse all tile files
def load_tiles(folder):
    return [Tile(f) for f in os.listdir(folder) if f.endswith(".PNG")]

# Check if a tile fits at (row, col) based on neighbors
def fits_constraints(grid, row, col, tile):
    if row > 0:
        neighbor_above = grid[row - 1][col]
        if neighbor_above:
            if neighbor_above.doors['S'] != tile.doors['N']:
                return False
            if neighbor_above.doors['S'] + tile.doors['N'] == 1:
                return False
    if col > 0:
        neighbor_left = grid[row][col - 1]
        if neighbor_left:
            if neighbor_left.doors['E'] != tile.doors['W']:
                return False
            if neighbor_left.doors['E'] + tile.doors['W'] == 1:
                return False
    return True

# Recursive backtracking placement
def place_tiles(grid, row, col, tiles):
    if row == GRID_SIZE:
        return True  # finished

    for tile in random.sample(tiles, len(tiles)):
        if fits_constraints(grid, row, col, tile):
            grid[row][col] = tile
            next_row, next_col = (row, col + 1) if col + 1 < GRID_SIZE else (row + 1, 0)
            if place_tiles(grid, next_row, next_col, tiles):
                return True
            grid[row][col] = None  # backtrack

    return False

# Main function
def build_tile_grid():
    tiles = load_tiles(TILE_FOLDER)
    grid = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    
    success = place_tiles(grid, 0, 0, tiles)
    if success:
        print("✅ Tile Grid Built Successfully:")
        for r, row in enumerate(grid):
            print(f"Row {r}: {[str(tile) for tile in row]}")
    else:
        print("❌ Failed to build a valid grid with current constraints.")

if __name__ == "__main__":
    build_tile_grid()
