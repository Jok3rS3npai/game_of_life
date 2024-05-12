import pygame
from rules_of_life import rules_of_life
import sys 

# Init Pygame 
pygame.init()

# Set up display
WIDTH, HEIGHT = 1200, 800
CELL_SIZE = 25
GRID_WIDTH, GRID_HEIGHT = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Game of Life")

#Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

#Init empty grid
grid = [[0 for x in range(GRID_WIDTH)] for y in range(GRID_HEIGHT)]

# Draw the Grid
def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (WIDTH, y))

# Get the grid position of the mouse
def get_grid_pos(x, y):
    grid_x = x // CELL_SIZE
    grid_y = y // CELL_SIZE
    return grid_x, grid_y

# Get neigbors of a cell
def get_toggled_neighbors(pos_x, pos_y):
    neighbors = 0
    # Get top left neighbor cell
    neighbor_x = pos_x - 1
    neighbor_y = pos_y - 1
    # Checks if the neigbors are a 1 or a 0
    for i in range (1,10):
        print(neighbor_y)
        if 0 >= neighbor_x <= len(grid[0]) and 0 >= neighbor_y <= len(grid) - 1:
            if grid[neighbor_y][neighbor_x] == 1:
                neighbors += 1
        neighbor_y += 1
        # If the neighbor is at the end of the row, move to the next row
        if neighbor_x % 3 == 0:
            neighbor_x += 1
    # Return the number of neighbors - 1 because we don't want to count the cell itself 
    if neighbors > 0:
        return neighbors - 1
    else:
        return neighbors 

# Function to generate a sidebar with the control explanations
def sidebar(screen):
    # Create a new surface for the sidebar
    sidebar = pygame.Surface((200, HEIGHT))

    # Set the background color of the sidebar
    sidebar.fill((200, 200, 200))

    # Create a font object
    font = pygame.font.Font(None, 24)

    # Render the text onto the sidebar
    text = font.render('Controls:', True, (0, 0, 0))
    sidebar.blit(text, (10, 10))

    # List of controls
    controls = [
        'Left click: Toggle cell',
        'Right click: Clear cell',
        'Space: Start'
    ]

    # Render each control onto the sidebar
    for i, control in enumerate(controls):
        text = font.render(control, True, (0, 0, 0))
        sidebar.blit(text, (10, 40 + i * 30))

    # Blit the sidebar onto the main screen
    screen.blit(sidebar, (WIDTH - 200, 0))

def main():
    # Game Loop
    running = True
    while running:
        # Checks if the rules of life are being followed
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                neighbors = get_toggled_neighbors(y, x)
                grid[y][x] = rules_of_life(cell, neighbors)

        # Checks for events in the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Left click to toggle cell
                if event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    grid_x, grid_y = get_grid_pos(x, y)
                    # Toggle cell
                    grid[grid_y][grid_x] = 1

                # Right click to clear cell
                elif event.button == 3:
                    x, y = pygame.mouse.get_pos()
                    grid_x, grid_y = get_grid_pos(x, y)
                    # Clear cell
                    grid[grid_y][grid_x] = 0

        # Draw the sidebar
        sidebar(screen)

        # Clear the screen
        screen.fill(BLACK)

        # Draw the grid
        draw_grid()

        # Hihglight cell under mouse
        x, y = pygame.mouse.get_pos()
        grid_x, grid_y = get_grid_pos(x, y)
        pygame.draw.rect(screen, GREEN, (grid_x * CELL_SIZE, grid_y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        # Color clicked cells
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell == 1:
                    pygame.draw.rect(screen, GREEN, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    print(grid)
        pygame.display.flip()

# Game execution
main()
#print(grid[31][0])
print("rows:", len(grid), "columns:", len(grid[0]))
