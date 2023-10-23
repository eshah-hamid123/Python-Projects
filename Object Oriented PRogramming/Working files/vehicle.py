class Vehicle:
    def __init__(self):
        print('Vehicle class')


class Car(Vehicle):
    def __init__(self):
        super().__init__()
        print('Car class')


# class Seats (Vehicle, Car):
#     def __init__(self):
#         super().__init__()
#         super().__init__()
#         print('Seats Class')


car1 = Car()
