# Name: Farhana Lima
# Purpose: Creating bike class for assignment named 'bike class'
# It's a object oriented python programming. Here the object is bike.

# Properties:
# Number of Gears (1 - 15)
# Current Gear (should default to 1)
# Number of Wheels (1, 2, 3, or 4)
# Brake Type ("hand brakes" or "foot brakes")

# Methods:
# Set & Get Number of Gears
# Set & Get Current Gear
# Set & Get Number of Wheels
# Set & Get Brake Type
# Reset Gears: Set gear back to 1
# Increase Gear: Increase Current Gear by 1, do not allow going over Number of Gears
# Decrease Gear: Decrease Current

# At first I'm creating a class named Bike
class Bike:

    # Private properties
    # Using dunder as the used in person class
    __numGears: int = 1
    __currentGear: int = 1
    __numWheels: int = 2
    __brakeType: str = "hand brakes"

    # Construct an instance of the class
    # Here __init__ is for instantiation, and self is for reference of the instance.

    def __init__(self, numGears=1, currentGear=10, numWheels=2, brakeType="hand brakes"):
        self.setNumberOfGears(numGears)
        self.setCurrentGear(currentGear)
        self.setNumberOfWheels(numWheels)
        self.setBreakType(brakeType)

    # Here is the getter for the number of gears property
    def getNumberOfGears(self) -> int:
        return self.__numGears

    # Setter for the number of gear, it should be (1-15)
    def setNumberOfGears(self, numGears: int) -> None:
        if 1 <= numGears <= 15:
            self.__numGears = numGears
        else:
            print("Number of gears must be between 1 and 15")

    # Getter and setter for the current gear property
    # By default it should be 1.
    def getCurrentGear(self) -> int:
        return self.__currentGear

    def setCurrentGear(self, currentGear: int) -> None:
        if 1 <= currentGear <= self.__numGears:
            self.__currentGear = currentGear
        else:
            print("Current gear must be within the allowed range")

    # Getter and setter for the number of wheels property
    # Number of wheels can be 1,2,3 and 4.
    def getNumberOfWheels(self) -> int:
        return self.__numWheels

    def setNumberOfWheels(self, numWheels: int) -> None:
        if numWheels in [1, 2, 3, 4]:  # Corrected the variable name here
            self.__numWheels = numWheels
        else:
            print("Number of wheels must be 1, 2, 3, or 4")

    # Getter and setter for the brake type property.
    # either hand breaks or foot breaks.
    def getBreakType(self) -> str:
        return self.__brakeType

    def setBreakType(self, brakeType: str) -> None:
        if brakeType in ["hand brakes", "foot brakes"]:
            self.__brakeType = brakeType
        else:
            print("Invalid brake type")

    # Few steps for this window

    # It sets the current gear of the bike back to 1,
    def resetGears(self):
        self.__currentGear = 1

    # To increase current gear
    def increaseGear(self):
        if self.__currentGear < self.__numGears:
            self.__currentGear += 1
        else:
            print("Cannot increase gear beyond the maximum")

    # It's for the Decrease of current gear
    def decreaseGear(self):
        if self.__currentGear > 1:
            self.__currentGear -= 1
        else:
            print("Cannot decrease gear below 1")
