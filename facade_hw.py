class Lights:
    def turn_on(self):
        print("Lights are ON")
    
    def turn_off(self):
        print("Lights are OFF")

class TV:
    def turn_on(self):
        print("TV is ON")
    
    def turn_off(self):
        print("TV is OFF")

    def set_channel(self, channel):
        print(f"TV channel set to {channel}")

class AirConditioner:
    def turn_on(self):
        print("Air Conditioner is ON")
    
    def turn_off(self):
        print("Air Conditioner is OFF")

    def set_temperature(self, temp):
        print(f"Air Conditioner set to {temp}°C")
