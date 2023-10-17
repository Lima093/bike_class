# In this file I want to run some examples, exceptions that may occur
# At first importing my bike class
from bike import Bike

# Using try blocks to raise the exception that may occur
try:
    # lets starts with myBike
    myBike = Bike(numGears=16, currentGear=1, numWheels=5, brakeType="hand brakes")

    # Now its time for print!
    print(f"Number of Gears: {myBike.getNumberOfGears()}")
    print(f"Current Gear: {myBike.getCurrentGear()}")
    print(f"Number of Wheels: {myBike.getNumberOfWheels()}")
    print(f"Brake Type: {myBike.getBreakType()}")

    myBike.increaseGear()
    print(f"Current Gear: {myBike.getCurrentGear()}")

    myBike.decreaseGear()
    print(f"Current Gear: {myBike.getCurrentGear()}")

    myBike.resetGears()
    print(f"Current Gear: {myBike.getCurrentGear()}")

except Exception as e:
    print(f"Error creating the bike: {str(e)}")
except nameError:
    print("NameError: Check the capitalization of your variable and method names.")