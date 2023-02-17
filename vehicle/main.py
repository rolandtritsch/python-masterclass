# main.py
"""The inheritance example."""

from car import Car
from truck import Truck

bmw = Car(100, 10)
print(bmw.top_speed())

smart = Car(10, 1)
print(smart.top_speed())

scania = Truck(10, 1, 2)
print(scania.top_speed())
