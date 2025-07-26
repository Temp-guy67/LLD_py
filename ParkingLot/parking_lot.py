from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional 

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
    def park_vehicle(self, vehicle : VehicleInterface) -> bool:
        pass

    @abstractmethod
    def un_park_vehicle(self) -> bool:
        pass

    

class CompactSpot(ParkingSpot):
    __if_available = True 
    __spot_number = -1
    __vehicle = None

    def __init__(self, spot_number : int):
        self.__spot_number = spot_number

    def get_spot_number(self) -> int:
        return self.__spot_number


    def is_available(self) -> bool:
        return self.__if_available


    def get_vehicle(self) -> VehicleSize:  
        return VehicleSize.SMALL
    
    def park_vehicle(self, vehicle : VehicleInterface) -> bool:
        if self.is_available():
            self.__vehicle = vehicle
            self.__if_available = False
            print("Spot - {} | Parked by {} ".format(self.__spot_number,self.__vehicle))

            return True
        else :
            print("Spot - {} | Not Available".format(self.__spot_number))
            return False

    def un_park_vehicle(self):
        self.__vehicle = None 
        self.__if_available = True
        print("Spot - {} | Parked by {} ".format(self.__spot_number,self.__vehicle))
        return True


class MediumSpot(ParkingSpot):
    __if_available = True 
    __spot_number = -1
    __vehicle = None

    def __init__(self, spot_number : int):
        self.__spot_number = spot_number

    def get_spot_number(self) -> int:
        return self.__spot_number


    def is_available(self) -> bool:
        return self.__if_available


    def get_vehicle(self) -> VehicleSize:  
        return VehicleSize.MEDIUM
    
    def park_vehicle(self, vehicle : VehicleInterface):
        if self.is_available():
            self.__vehicle = vehicle
            self.__if_available = False
            return True
        else :
            print("Spot - {} | Not Available".format(self.__spot_number))
            return False

    def un_park_vehicle(self):
        self.__vehicle = None 
        self.__if_available = True
        print("Spot - {} | Parked by {} ".format(self.__spot_number,self.__vehicle))
        return False


class ParkingLotManager():
    __map_of_parking_spots = None
    __map2spot = []

    def __init__(self, vehicle_size_vs_spots : dict[VehicleSize, list[ParkingSpot]]):
        self.__map_of_parking_spots = vehicle_size_vs_spots

    def find_spot(self, vehicle_size : VehicleSize) -> Optional[ParkingSpot] :

        for size in VehicleSize:
            if size.value >= vehicle_size.value:
                spots = self.__map_of_parking_spots.get(size) # type: ignore
                if spots:
                    for spot in spots:
                        if spot.is_available():
                            return spot
        return None


    def park_vehicle(self, vehicle):
        parking_spot = self.find_spot(vehicle.get_vehicle_size())
        if parking_spot.park_vehicle(vehicle) :  # type: ignore
            self.__map2spot[vehicle.get_license_no()] = parking_spot

    def un_park_vehicle(self, vehicle):
        parking_spot = self.__map2spot[vehicle.get_license_no()]
        if parking_spot :
            parking_spot.un_park_vehicle()




