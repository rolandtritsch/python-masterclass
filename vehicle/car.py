# car.py
"""The inheritance example."""

from vehicle import Vehicle


class Car(Vehicle):
    """The Car class."""

    def __init__(self, bhp, max_load):
        """Return an initialzed Car."""
        self.bhp = bhp
        self.max_load = max_load
