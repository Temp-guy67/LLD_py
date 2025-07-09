# import sys
# sys.stdin = open("ip.txt","r")
# sys.stdout = open("op.txt","w")


from abc import ABC, abstractmethod 

class BatteryFeatures(ABC):
    @abstractmethod 
    def show_battery_percentage():
        pass 

class ChargingActions(ABC):
    @abstractmethod 
    def is_charging():
        pass

    @abstractmethod 
    def switch_on_charging():
        pass 

    @abstractmethod 
    def switch_off_charging():
        pass

class AudioFeatures(ABC):
    @abstractmethod 
    def play_audio():
        pass 


class ScreeFeatures(ABC):
    @abstractmethod 
    def display():
        pass 


class BatteriedDevice(BatteryFeatures):
    __current_charge = -1
    def __init__(self, current_charge : float):
        self.__current_charge = current_charge

    def show_battery_percentage(self) -> float:
        return self.__current_charge
        


class NonBatteriedDevice(BatteryFeatures):
    def __init__(self):
        pass

    def show_battery_percentage(self) -> float:
        return -1
    

    
class AlexaDevice(ChargingActions):
    __batter_functions = None 
    __charging_status = False 

    def __init__(self, batteryFeatures : BatteryFeatures):
        self.__batter_functions = batteryFeatures 

    def is_charging(self):
        return self.__charging_status

    def switch_on_charging(self):
        self.__charging_status = True 

    def switch_off_charging(self):
        self.__charging_status = False 

    def display_battery_status(self):
        battery_per = self.__batter_functions.show_battery_percentage()
        if battery_per > -1:
            print("{}% ".format(battery_per))
        else:
            print("No Battery Availeable")

        
    
class AudioAlexa(AlexaDevice, AudioFeatures):
    def __init__(self, batteryFeatures : BatteryFeatures):
        super(self, batteryFeatures)

    def play_audio():
        print("Playing Audio")

class ScreenAlexa(AlexaDevice, ScreeFeatures):
    def __init__(self, batteryFeatures : BatteryFeatures):
        super(batteryFeatures)

    def display():
        print("Showing screen")


class AudioScreenAlexa(AlexaDevice, AudioFeatures, ScreeFeatures):
    def __init__(self, batteryFeatures : BatteryFeatures):
        super(batteryFeatures)

    def play_audio():
        print("Playing Audio")

    def display():
        print("Showing screen")




if __name__ == "__main__":
    batteriedDevice = BatteriedDevice(76)
    audioScreenDevice = AudioScreenAlexa(batteriedDevice)
    audioScreenDevice.display_battery_status()
    audioScreenDevice.play_audio()


    