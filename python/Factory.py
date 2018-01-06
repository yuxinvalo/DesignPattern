import random
import abc

'''Simple Factory'''
class BasicCar(object):
    def get_cars(self):
        return "production: [basic car]"
    def __str__(self):
        return "BasicCar"

class BWMCars(object):
    def get_cars(self):
        return "production: [BWM car]"
    def __str__(self):
        return "BWMCars"

class SimpleCarFactory(object):
    @staticmethod
    def create_cars(type):
        if type == 'bc':
            return BasicCar()
        elif type == 'bwmc':
            return BWMCars()

cartype = random.choice(['bc', 'bwmc'])
car = SimpleCarFactory.create_cars(cartype)
print("Simple Factory")
print(car.get_cars())


'''Abstract Factory'''
class Engine(object):
    def get_comp(self):
        return "production: [engine]"

class Tyre(object):
    def get_comp(self):
        return "production: [tyre]"

class Factory(object):
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def create_car(self):
        pass
    def create_component(self):
        pass

class BasicCarEngineFactory(Factory):
    def create_car(self):
        return BasicCar()
    def create_engine(self):
        return Engine()

class BWMCarsTyreFactory(Factory):
    def create_car(self):
        return BWMCars()
    def create_component(self):
        return Tyre()

factory = random.choice([BasicCarEngineFactory, BWMCarsTyreFactory])()
car = factory.create_car()
component = factory.create_component()
print("Abstract Factory")
print(car.get_cars())
print(component.get_comp())
