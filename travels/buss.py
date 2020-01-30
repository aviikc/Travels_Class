class Busses():
    self.total_number_of_busses = [
                                    "MH 04 1234",
                                    "MH 06 4567",
                                    "MH 04 4243",
                                    "MH 05 3455",
                                    "MH 04 9876",
                                    "MH 05 7643",
                                    "MH 04 7243",
                                    "MH 05 0395",
                                    "MH 04 6111",
                                    "MH 07 7211",
                                    "MH 04 7428"
                                ]
    self.available_busses = []
    self.current_plying_buses = []

    def __init__(self):
        pass

    def make_current_plying_BusList(self):
        if len(self.current_plying_buses) != 0:
            for i in self.current_plying_buses:
                self.available_busses = self.total_number_of_busses.remove(i)
        else:
            self.available_busses = self.total_number_of_busses

    def assign_bus(self, bus_number):
        if bus_number in total_number_of_busses:
            self.current_plying_buses.append(bus_number)
            self.available_busses.remove(bus_number)
        else:
            self.total_number_of_busses.append(bus_number)
            self.current_plying_buses.append(bus_number)
            self.available_busses.remove(bus_number)

    def bus_depart(self, bus_number):
        if bus_number in total_number_of_busses:
            if bus_number in self.available_busses:
                self.available_busses.remove(bus_number)

    def bus_arrive(self, bus_number):
        if bus_number in total_number_of_busses:
            if bus_number in self.available_busses:
                self.available_busses.append(bus_number)

    

    