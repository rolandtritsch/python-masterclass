# bubble.py
"""A visualization of the bubble-sort algorithm."""

from bubblesort import BubbleSort
from constants import Constants
from threading import Thread
import logging
import pygame
import util


class Bubble(Thread):
    """The Bubble-Sort Visualizer."""

    def __show__(self, bars):
        """Draw all the bars."""
        logging.info("Drawing %s ...", bars)
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

    def __init__(self, initial):
        """Return an initialized visualizer."""
        Thread.__init__(self)
        self.initial = initial

        self.window = pygame.display.set_mode(
            (Constants.windowHeight, Constants.windowWidth)
        )
        pygame.display.set_caption(Constants.caption)

    def run(self):
        """Run the visualizer in a thread."""
        bars = BubbleSort(self.initial)
        while not bars.isSorted():
            self.window.fill(Constants.windowFillColor)
            self.__show__(bars.next())
            pygame.display.update()
            pygame.time.delay(Constants.delay)


logging.basicConfig()
logging.root.setLevel(logging.INFO)

logging.info("Init pygame ...")
pygame.init()

logging.info("Starting visualizer ...")
visualizer = Bubble(util.randlist(Constants.length, Constants.upper))
visualizer.start()
visualizer.join()
logging.info("... done!")
