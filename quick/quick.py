# quick.py
"""
A quick-sort visualizer.

This code was generate by ChatGPT and then
(just) polished/refactored by me.
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the width and height of the screen [width, height]
WIDTH = 700
HEIGHT = 500
FPS = 60

# Initialize pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quick-Sort Visualization")
clock = pygame.time.Clock()

# Function to draw the array on the screen
def draw_array(arr, left_index, right_index, current_index):    
    screen.fill(WHITE)
    bar_width = WIDTH // len(arr)
    for i, value in enumerate(arr):
        color = BLACK
        if i == current_index:
            color = GREEN
        elif i < left_index or i > right_index:
            color = RED
        pygame.draw.rect(screen, color, (i * bar_width, HEIGHT - value, bar_width, value))
    pygame.display.update()

# Quick-Sort Algorithm
def quicksort(arr, left, right):
    if left >= right:
        return
    pivot = arr[random.randint(left, right)]
    i, j = left, right
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            draw_array(arr, left, right, j)
            i += 1
            j -= 1
        else:
            draw_array(arr, left, right, i)
        clock.tick(FPS)
    quicksort(arr, left, j)
    quicksort(arr, i, right)

# Example usage
arr = [3, 7, 1, 2, 8, 4, 5]
quicksort(arr, 0, len(arr) - 1)

# Quit pygame
pygame.quit()
