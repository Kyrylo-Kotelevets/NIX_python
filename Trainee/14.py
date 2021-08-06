"""This module is used to implement a task with inheritance"""


class Engine:
    """This class combines information about a car's engine"""

    def __init__(self, types: str, volume: int, speed: int) -> None:
        """
        Initialization of parameters of the class Engine
        :param types: indicates the type of engine
        :param volume: indicates engine displacement
        :param speed: indicates the maximum possible speed
        """
        self.engine_type = types
        self.engine_volume = volume
        self.maximum_speed = speed
        self.move_flag = False

    @staticmethod
    def description() -> None:
        """A function that describes the type of motors"""
        print("Vehicle engines can be gasoline, diesel, gas, electric and hybrid")

    def __str__(self) -> str:
        """A function that allows you to display information about an object as a string"""
        return str("Engine type: %s, engine volume: %d, maximum speed: %s, routine: %s" %
                   (self.engine_type, self.engine_volume, self.maximum_speed, self.move_flag))

    def start(self) -> None:
        """Function that sets the engine start flag as active"""
        self.move_flag = True

    def stop(self) -> None:
        """Function that sets the engine start flag as stopped"""
        self.move_flag = False


class Car(Engine):
    """This is a descendant class of the Engine class. Class describes the car"""
    NUM_CAR = 0

    def __init__(self, *args) -> None:
        """
        Initialization of parameters of the class Car
        :param args: A set of parameters for initializing an object
        """
        self.car_brand, self.car_gearbox, self.car_mileage, self.car_year = args[:4]
        self.flag_doors = True
        Engine.__init__(self, *args[4:])
        Car.NUM_CAR += 1

    def __str__(self) -> str:
        """A function that allows you to display information about an object as a string"""
        return str("Brand: %s, gearbox: %s, mileage: %d, year %d, engine type: %s, "
                   "engine volume: %d, maximum speed: %s, routine: %s, close doors: %s" %
                   (self.car_brand, self.car_gearbox, self.car_mileage,
                    self.car_year, self.engine_type, self.engine_volume,
                    self.maximum_speed, self.move_flag, self.flag_doors))

    @property
    def num_car(self) -> str:
        """The function that allows you to return the number of cars is used as a field"""
        return Car.count_cars()

    @classmethod
    def count_cars(cls) -> str:
        """A function that forms a line with the number of cars"""
        return "Number cars: %d" % cls.NUM_CAR

    def open_doors(self) -> None:
        """A function that sets the door open flag to open"""
        self.flag_doors = False

    def close_doors(self) -> None:
        """A function that sets the door open flag to close"""
        self.flag_doors = True

    def __call__(self, flag: str) -> None:
        """This magic method allows you to call an instance of a class as a function.
        Allows you to open or close the car"""
        options = {"open": self.open_doors, "close": self.close_doors}
        try:
            options[flag]()
        except:
            print("The flag name does not correspond to the valid state of the doors")


class Honda(Car):
    """This class describes a specific brand of car - Honda"""

    def __init__(self, *args) -> None:
        Car.__init__(self, "Honda", *args[:-2])
        self.owner_name, self.owner_surname = args[-2:]

    def __str__(self) -> str:
        """A function that allows you to display information about an object as a string"""
        return str("Owner: %s %s" % (self.owner_name, self.owner_surname))

    def change_name(self, new_name: str) -> None:
        """The function allows you to change the user`s name of the car"""
        self.owner_name = new_name

    def change_surname(self, new_surname: str) -> None:
        """The function allows you to change the user`s surname of the car"""
        self.owner_surname = new_surname
