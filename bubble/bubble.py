# bubble.py
"""A visualization of the bubble-sort algorithm."""

from constants import Constants
from threading import Thread
import pygame


class Bubble(Thread):
    """The Bubble-Sort Visualizer."""

    def __init__(self):
        """Return an initialized visualizer."""
        self.window = pygame.display.window(
            Constants.windowHeight, Constants.windowWidth
        )
        pygame.display.caption(Constants.caption)

    def run():
        """Run the visualizer in a thread."""
        Bubble()


pygame.init()

Bubble.start()
