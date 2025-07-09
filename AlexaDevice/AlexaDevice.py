from abc import ABC, abstractmethod
from typing import Optional


# ========== INTERFACES ==========
class BatteryPowered(ABC):
    @abstractmethod
    def battery_percentage(self) -> float:
        pass


class Chargable(ABC):
    @abstractmethod
    def is_charging(self) -> bool:
        pass

    @abstractmethod
    def start_charging(self):
        pass

    @abstractmethod
    def stop_charging(self):
        pass


class Displayable(ABC):
    @abstractmethod
    def display(self):
        pass


class Playable(ABC):
    @abstractmethod
    def play_audio(self):
        pass


# ========== COMPONENTS ==========
class BatteryModule(BatteryPowered, Chargable):
    def __init__(self, initial_charge: float = 100.0):
        self._charge = initial_charge
        self._is_charging = False

    def battery_percentage(self) -> float:
        return self._charge

    def is_charging(self) -> bool:
        return self._is_charging

    def start_charging(self):
        self._is_charging = True

    def stop_charging(self):
        self._is_charging = False


class NoBatteryModule(BatteryPowered, Chargable):
    def battery_percentage(self) -> float:
        return -1.0

    def is_charging(self) -> bool:
        return False

    def start_charging(self):
        pass

    def stop_charging(self):
        pass


# ========== DEVICE BASE CLASS ==========
class AlexaDevice:
    def __init__(
        self,
        battery_module: Optional[BatteryPowered] = None,
    ):
        self.battery_module = battery_module

    def show_status(self):
        if self.battery_module:
            charge = self.battery_module.battery_percentage()
            charging = self.battery_module.is_charging() # type: ignore

            if charging:
                if charge > 0:
                    print("Charging... {:.2f}%".format(charge))
                else:
                    print("Charging... Battery not available")
            else:
                if charge > 0:
                    print("Battery: {:.2f}%".format(charge))
                else:
                    print("Battery not available")
        else:
            print("Battery not available")


class AudioAlexa(AlexaDevice, Playable):
    def play_audio(self):
        print("🔊 Playing audio...")


class ScreenAlexa(AlexaDevice, Displayable):
    def display(self):
        print("🖥️ Showing screen...")


class HybridAlexa(AlexaDevice, Playable, Displayable):
    def play_audio(self):
        print("🔊 Playing audio...")

    def display(self):
        print("🖥️ Showing screen...")


# ========== MAIN ==========
if __name__ == "__main__":
    # Create battery and non-battery modules
    battery = BatteryModule(76)
    no_battery = NoBatteryModule()

    # Devices with different features
    device1 = AudioAlexa(battery_module=battery)
    device2 = ScreenAlexa(battery_module=no_battery)
    device3 = HybridAlexa(battery_module=battery)

    # Simulate actions
    battery.start_charging()
    device1.show_status()  # Charging + battery
    battery.stop_charging()
    device1.play_audio()

    print()

    device2.show_status()  # No battery
    device2.display()

    print()

    device3.show_status()  # Battery only
    device3.display()
    device3.play_audio()