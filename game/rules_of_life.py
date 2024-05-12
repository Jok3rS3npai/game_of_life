# In this file, we define the rules of the game of life.
# Rules are defined in the README.md file.

def rule_1(cell, neighbors):
    """
    Rule 1: Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    """
    if cell == 1 and neighbors < 2:
        return 0
    return cell

def rule_2(cell, neighbors):
    """
    Rule 2: Any live cell with two or three live neighbours lives on to the next generation.
    """
    if cell == 1 and (neighbors == 2 or neighbors == 3):
        return 1
    return cell

def rule_3(cell, neighbors):
    """
    Rule 3: Any live cell with more than three live neighbours dies, as if by overpopulation.
    """
    if cell == 1 and neighbors > 3:
        return 0
    return cell

def rule_4(cell, neighbors):
    """
    Rule 4: Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    """
    if cell == 0 and neighbors == 3:
        return 1
    return cell

def rules_of_life(cell, neighbors):
    """
    Apply all rules to a cell and its neighbors.
    """
    if rule_1(cell, neighbors) == 0:
        return 0
    if rule_2(cell, neighbors) == 1:
        return 1
    if rule_3(cell, neighbors) == 0:
        return 0
    if rule_4(cell, neighbors) == 1:
        return 1
