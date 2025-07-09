from abc import ABC, abstractmethod
from enum import Enum 

class VehicleSize(Enum):
    SMALL=1
    MEDIUM=2 
    LARGE=3 


class VehicleInterface(ABC):
    @abstractmethod
    def get_license_no(self) -> str:
        pass

    @abstractmethod
    def get_vehicle_size(self) -> VehicleSize :
        pass


class Bike(VehicleInterface):
    __license = "" 
    __vehicle_size = VehicleSize.SMALL

    def __init__(self, license : str):
        self.__license = license

    def get_license_no(self) -> str:
        return self.__license

    def get_vehicle_size(self) -> VehicleSize :
        return self.__vehicle_size
    
class Car(VehicleInterface):
    __license = "" 
    __vehicle_size = VehicleSize.MEDIUM

    def __init__(self, license : str):
        self.__license = license

    def get_license_no(self) -> str:
        return self.__license

    def get_vehicle_size(self) -> VehicleSize :
        return self.__vehicle_size
    

class ParkingSpot(ABC):
    @abstractmethod
    def get_spot_number(self) -> int:
        pass 

    @abstractmethod
    def is_available(self) -> bool:
        pass

    @abstractmethod
    def park_vehicle(self):
        pass

    @abstractmethod
    def un_park_vehicle(self):
        pass