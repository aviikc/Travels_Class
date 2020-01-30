from buss import Busses
from passenger import Passenger

class BusService():
    self.count = 0

    def __init__(self, busNumber):
        self.current_busses = Busses()
        self.current_busses.assign_bus(busNumber)
        self.buss_passangers = []
        
    def load_bus(self, name, boarding, destination,):
        if self.checkSeat():
            passenger = Passenger(name, boarding, destination)
            self.buss_passangers.append(passenger)
        else:
            return self.buss_passangers
        return self.buss_passangers

    def unload_bus(self):
        

    def checkSeat(self):
        count = count + 1
        if count >= 10:
            return None
        else:
            return count