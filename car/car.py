# car.py

class car:
    def __init__(self, bhp, max_load):
        self.bhp = bhp
        self.max_load = max_load

    def top_speed(self):
        return self.bhp * self.max_load

bmw = car(100, 10)
print(bmw.top_speed())

smart = car(10, 1)
print(smart.top_speed())
