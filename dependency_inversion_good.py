## ---> Low Level
class LightBulb:
    def turn_on(self):
        print("Turning on")

    def turn_off(self):
        print("turning off")


## ---> High Level
class Switch:
    def __init__(self, bulb: lightBulb) -> None:
        self.on = False
        self.bulb = bulb

    def press(self):
        if self.on:
            self.bulb.turn_off()
        else:
            self.bulb.turn_on()

        self.on = not self.on


bulb = LightBulb()
switch = Switch(bulb)
switch.press()
