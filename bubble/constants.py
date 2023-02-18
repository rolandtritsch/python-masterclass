# constants.py
"""All the app-wide constants/config/defaults."""


class Constants:
    """The Constant class."""

    __black__ = (0, 0, 0)
    __red__ = (255, 0, 0)
    __white__ = (255, 255, 255)
    barColor = __red__
    barGap = 5
    barWidth = 10
    caption = "BubbleSort Visualizer"
    delay = 500
    numberOfBars = 50
    scaleOfBars = 10
    sizeOfBars = 40
    windowFillColor = __black__
    xMargin = 10
    yMargin = 10

    @classmethod
    def windowHeight(cls):
        """Return window height."""
        return (
            (cls.xMargin * 2) +
            (cls.numberOfBars * cls.barWidth) +
            ((cls.numberOfBars-1) * cls.barGap)
            )

    @classmethod
    def windowWidth(cls):
        """Return window width."""
        return (
            (cls.yMargin * 2) +
            (cls.sizeOfBars * cls.scaleOfBars)
            )
