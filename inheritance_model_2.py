class Vehicles:
    def __init__(self, color, tyre_class, material_made, brand):
        self.color: str = color
        self.tyre_class: int = tyre_class
        self.material_made: str = material_made
        self.brand: str = brand

    def get_brand(self) -> str:
        return self.brand


class Cars(Vehicles):
    def __init__(self, color, tyre_class, material_made, brand, doors_numbers, brand_model):
        super().__init__(color, tyre_class, material_made, brand)
        self.doors_number: int = doors_numbers
        self.brand_model: str = brand_model

    def car_info(self) -> str:
        return f"Hello I am {self.brand}, I am made from {self.material_made} and my color is: {self.color}"


class SportsCars(Cars):
    def __init__(self, color, tyre_class, material_made, brand, doors_number, model, horse_powers):
        super().__init__(color, tyre_class, material_made, brand, doors_number, model)
        self.horse_powers: int = horse_powers

    def car_info(self) -> str:  # override a method: car_info
        return f"I am {self.brand_model} my color is: {self.color} and UNDER THE HOOD I HAVE: {self.horse_powers} :)"

    def km_per_hour(self):
        if self.horse_powers >= 350:
            return "Should be careful with this car its really fast !"\
                   " From 0 to 100 km for less than 5 seconds, depends from the car_brand !"

        elif self.horse_powers >= 90 < 350:
            return "WOW it's not bad for first sport car ;)"

        else:
            return "I've seen snails, which are faster :( "


class Bike(Vehicles):
    def __init__(self, color, tyre_class, material_made, brand, breaks_model):
        super().__init__(color, tyre_class, material_made, brand)
        self.breaks_model: str = breaks_model

    def get_breaks_model(self) -> str:
        return self.breaks_model


class MotorBike(Bike):
    def __init__(self, color, tyre_class, material_made, brand, breaks_model, speed_limit):
        super().__init__(color, tyre_class, material_made, brand, breaks_model)
        self.speed_limit: int = speed_limit

    def motor_bike_info(self):
        if self.speed_limit >= 200:
            return "Be careful this motor bikes is really fast and good looking, but its really DANGEROUS as well !!!"
        return f"Lets Rock and Roll with your: {self.brand} :)"


class PedalBike(Bike):
    def __init__(self, color, tyre_class, material_made, brand, breaks_model, shock_absorbers):
        super().__init__(color, tyre_class, material_made, brand, breaks_model)
        self.shock_absorbers: str = shock_absorbers


john_first_sport_car = SportsCars('red', 3, 'real steal', 'Nissan', 3, 'GTR', 465)
# first_sport_cars -> Референция към обекет от тип SportsCars
assert john_first_sport_car.tyre_class == 3
print(john_first_sport_car.km_per_hour())


mike_first_bike = MotorBike("red", 3, "steal", "Suzuki", "Brembo", 280)
assert mike_first_bike.brand == "Suzuki"
print(mike_first_bike.motor_bike_info())

viktor_first_sport_car = SportsCars("blue", 2, 'plastic', "Opel", 3, "Corsa-S", 44)
assert viktor_first_sport_car.km_per_hour() == "I've seen snails, which are faster :( "
print(viktor_first_sport_car.km_per_hour())
