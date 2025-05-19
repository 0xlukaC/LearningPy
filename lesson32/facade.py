# /usr/bin/python3
"""
Model a simple home theatre system that starts up multiple devices
        ◦ Users should be able to conveniently turn on a projector and sound system, and dim the lights with a convenient method, activate()
        ◦ Users should be able to reverse the above (i.e, turn of the projector and sound system, and turn the lights back on), deactivate()
        ◦ Print simple statements to represent the actions. E.g., “The projector is on.”

"""


class Remote:
    def __init__(self, homeTheatre):
        self.state = 0
        self.homeTheatre = homeTheatre

    def toggle(self):
        self.state = not self.state
        if self.state:
            self.homeTheatre.activate()
        else:
            self.homeTheatre.deactivate()

        print("toggled remote")


class homeTheatre:
    def __init__(self, speaker, projector, lighting):
        self.speaker = speaker
        self.projector = projector
        self.lighting = lighting
        # self.state = 0

    def activate(self):
        self.projector.on()
        self.speaker.on()
        self.lighting.dim()
        print("Home theatre activated")

    def deactivate(self):
        self.projector.off()
        self.speaker.off()
        self.lighting.brighten()
        print("Home theatre deactivated")


class Speaker:
    def __init__(self, brightness, contrast):
        self.brightness = brightness
        self.contrast = contrast
        self.is_on = False

    def toggle(self):
        self.is_on = not self.is_on
        print(f"Speaker is now {'on' if self.is_on else 'off'}")


# I couldnt be botherd after this


class Projector:
    def on(self):
        print("Projector is now on")

    def off(self):
        print("Projector is now off")


class Lighting:
    def dim(self):
        print("Lights dimmed")

    def brighten(self):
        print("Lights brightened")


speaker = Speaker(1, 2)
projector = Projector()
lighting = Lighting()
theatre = homeTheatre(speaker, projector, lighting)
remote = Remote(theatre)

remote.toggle()
remote.toggle()
