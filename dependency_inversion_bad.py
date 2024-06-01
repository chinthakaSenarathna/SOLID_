from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass
    

## ---> Low Level
class LightBulb(Switchable):
    def turn_on(self):
        print("Turning on")

    def turn_off(self):
        print("turning off")


## ---> Low Level
class TV(Switchable):
    def turn_on(self):
        print("Turning on TV")

    def turn_off(self):
        print("turning off TV")


## ---> High Level
class Switch:
    def __init__(self, device: Switchable) -> None:
        self.on = False
        self.bulb = bulb

    def press(self):
        if self.on:
            self.bulb.turn_off()
        else:
            self.bulb.turn_on()

        self.on = not self.on


bulb = LightBulb()
switch1 = Switch(bulb)
switch1.press()
switch1.press()


tv = TV()
switch2 = Switch(tv)
switch2.press()
switch2.press()





## -----------------------------------------------------------------------------------------


from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("Connecting to MySQL database")

class UserService:
    def __init__(self, db: Database):
        self.db = db

    def connect_to_database(self):
        self.db.connect()

db = MySQLDatabase()
service = UserService(db)
service.connect_to_database()







