# def Generate_Grid(rows: int, cols: int) -> dict:
#     colors = ['pink', 'blue', 'red']
#     grid = {}
#     total = rows*cols
#     for t in range(total):
#         grid[t] = [colors[0]]
#         if t + 1 < cols:
#             grid[t].append(t + 1)
#         if t + cols < total:
#             grid[t].append(t + cols)
#
#     return grid

def main():
    # grid = Generate_Grid(3, 3)

    grid = {0: ['red', 1, 3], 1: ['red', 0, 2, 4], 2: ['pink', 1, 5], 3: ['purple', 0, 4, 6], 4: ['blue', 1, 3, 5, 7],
            5: ['purple', 4, 8], 6: ['purple', 3, 7], 7: ['purple', 4, 6, 8], 8: ['purple', 5, 7]}

    visited = [False for _ in range(len(grid.keys()))]


    color_count = {'red': 0, 'pink': 0, 'purple': 0, 'blue': 0}

    for i in grid.keys():
        print(i)

main()
