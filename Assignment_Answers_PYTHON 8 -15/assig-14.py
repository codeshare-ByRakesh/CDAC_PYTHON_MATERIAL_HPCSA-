from abc import ABC, abstractmethod


class SmartDevice(ABC):
    def __init__(self, name):
        self._name = name
        self._status = 'off'

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    def device_info(self):
        return f"Device: {self._name}, Status: {self._status}"


class SmartLight(SmartDevice):
    def __init__(self, name):
        super().__init__(name)

    def turn_on(self):
        self._status = 'on'
        return "Smart light is now on."

    def turn_off(self):
        self._status = 'off'
        return "Smart light is now off."

    def set_brightness(self, level):
        if 0 <= level <= 100:
            return f"Brightness set to {level}%."
        else:
            return "Brightness level must be between 0 and 100."


if __name__ == "__main__":
    my_light = SmartLight("Living Room Light")

    print(my_light.device_info())
    print(my_light.turn_on())
    print(my_light.device_info())
    print(my_light.set_brightness(70))
    print(my_light.turn_off())
    print(my_light.device_info())  
