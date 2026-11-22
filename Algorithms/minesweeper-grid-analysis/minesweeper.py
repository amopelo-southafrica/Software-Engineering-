def minesweeper(grid):
    rows = len(grid)
    cols = len(grid[0])

    # Directions for the 8 adjacent cells
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0), (1, 1)
    ]

    # Create a new grid for the result
    result = []

    for r in range(rows):
        result_row = []
        for c in range(cols):
            if grid[r][c] == "#":
                result_row.append("#")
            else:
                mine_count = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == "#":
                            mine_count += 1
                result_row.append(mine_count)
        result.append(result_row)

    return result


# Example usage (optional test)
if __name__ == "__main__":
    input_grid = [
        ["-", "-", "-", "#", "#"],
        ["-", "#", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "#", "#", "-", "-"],
        ["-", "-", "-", "-", "-"]
    ]

    output = minesweeper(input_grid)
    for row in output:
        print(row)

