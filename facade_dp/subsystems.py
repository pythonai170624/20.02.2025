class Amplifier:
    def on(self):
        print("Amplifier is ON")

    def off(self):
        print("Amplifier is OFF")

class DVDPlayer:
    def on(self):
        print("DVD Player is ON")

    def play(self, movie):
        print(f"Playing '{movie}'")

    def off(self):
        print("DVD Player is OFF")

class Projector:
    def on(self):
        print("Projector is ON")

    def off(self):
        print("Projector is OFF")

class Lights:
    def dim(self, level):
        print(f"Lights dimmed to {level}%")

class Screen:
    def down(self):
        print("Screen is down")

    def up(self):
        print("Screen is up")
