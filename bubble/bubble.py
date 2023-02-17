# bubble.py
"""A visualization of the bubble-sort algorithm."""

from constants import Constants
from threading import Thread
import pygame


class Bubble(Thread):
    """The Bubble-Sort Visualizer."""

    def __show__(self, bars):
        """Draw all the bars."""
        for i in range(len(bars)):
            pygame.draw.rect(
                self.window,
                Constants.barColor,
                (
                    Constants.xPos + Constants.barGap * i,
                    Constants.yPos,
                    Constants.barWidth,
                    bars[i]
                )
            )

    def __init__(self):
        """Return an initialized visualizer."""
        self.window = pygame.display.set_mode(
            (Constants.windowHeight, Constants.windowWidth)
        )
        pygame.display.set_caption(Constants.caption)

    def run(self):
        """Run the visualizer in a thread."""
        bars = [90, 80, 70, 60, 50, 40, 30, 20, 10]
        self.__show__(bars)


pygame.init()

visualizer = Bubble()
visualizer.start()
