# Anthony Han 11/12/23
# Bubble sort visualizer with a cool custom touch

# Import pygame
import pygame

# Import random
import random

pygame.init()

# Set window size
win = pygame.display.set_mode((1280, 720))

# Add a title to the window
pygame.display.set_caption("Bubble Sort Visualizer")

# Load a custom image and make it the icon
img = pygame.image.load('Floppa.jpg')
pygame.display.set_icon(img)

# Initial position
x = 200
y = 0

# Bar width
width = 25

# Height of each bar in an array
height = [0] * 30

# Give random heights between 1 and 250 for bars
for i in range(len(height)):
    height[i] = random.randint(1, 250)

run = True

# Method used to show the list of the heights
def show(height):

    # Loop to iterate each item in the list
    for i in range(len(height)):

        # Draw each bar with spacing
        # Custom touch: Change the color for each bar rendered
        pygame.draw.rect(win, (i * 5 + 20, 0, 0), (x + 30 * i, y, width, height[i]))

while run:

    # Execute flag to start sorting
    execute = False

    # Time delay
    pygame.time.delay(10)

    # Getting keys pressed
    keys = pygame.key.get_pressed()

    # Iterating events
    for event in pygame.event.get():

        # If event quits
        if event.type == pygame.QUIT:

            run = False

    # If space bar is pressed
    if keys[pygame.K_SPACE]:

        execute = True

    # Check if execute flag is false
    if execute == False:

        # Fill window with black
        win.fill((0, 0, 0))

        # Call height method to render bars
        show(height)

        # Update the window
        pygame.display.update()

        # If execute flag is true
    else:

        # Start bubble sort technique
        for i in range(len(height) - 1):

            for j in range(len(height) - i - 1):
                
                # If starting is greater than the next element
                if height[j] > height[j + 1]:

                    # Save it in a temporary variable and swap them using the temporary variable
                    t = height[j]
                    height[j] = height[j + 1]
                    height[j + 1] = t

                    # Fill window with black background
                    win.fill((0, 0, 0))

                    # Call method to show the list again
                    show(height)

                    # Create a time delay
                    pygame.time.delay(50)

                    # Update the display
                    pygame.display.update()

# Exit the main window
pygame.quit()