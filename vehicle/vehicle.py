# vehicle.py
"""The inheritance example."""

from abc import ABC


class Vehicle(ABC):
    """The (abstract) Vehicle (base) class."""

    def top_speed(self):
        """Return the top_speed of the vehicle."""
        return self.bhp * self.max_load
