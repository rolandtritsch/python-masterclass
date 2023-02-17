# truck.py
"""The inheritance example."""

from vehicle import Vehicle


class Truck(Vehicle):
    """The Truck class."""

    def __init__(self, bhp, max_load_lorry, max_load_trailer):
        """Return an initialzed Truck."""
        self.bhp = bhp
        self.max_load = max_load_lorry + max_load_trailer
