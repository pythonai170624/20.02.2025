from facade_dp.subsystems import Amplifier, DVDPlayer, Projector, Lights, Screen

class HomeTheaterFacade:
    def __init__(self, amp = Amplifier(),
                 dvd = DVDPlayer(),
                 projector = Projector(),
                 lights = Lights(),
                 screen = Screen()):
        self.amp = amp
        self.dvd = dvd
        self.projector = projector
        self.lights = lights
        self.screen = screen

    def watch_movie(self, movie):
        print("\nSetting up the home theater to watch a movie...\n")
        self.lights.dim(30)
        self.screen.down()
        self.projector.on()
        self.amp.on()
        self.dvd.on()
        self.dvd.play(movie)
        print("\nEnjoy your movie!\n")

    def end_movie(self):
        print("\nShutting down the home theater...\n")
        self.dvd.off()
        self.amp.off()
        self.projector.off()
        self.screen.up()
        self.lights.dim(100)
        print("\nGoodbye!\n")
