class Passenger:
    def __init__(self, name, booking_reference, seat_number):
        self.name = name
        self.booking_reference = booking_reference
        self.seat_number = seat_number
        self.boarding_pass = None

    def get_name(self):
        return self.name

    def get_booking_reference(self):
        return self.booking_reference

    def get_seat_number(self):
        return self.seat_number

    def set_boarding_pass(self, boarding_pass):
        self.boarding_pass = boarding_pass

    def get_boarding_pass(self):
        return self.boarding_pass




class TicketingAgent:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name




class System:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def get_flights(self):
        return self.flights




class Flight:
    def __init__(self, flight_number, destination, departure_time):
        self.flight_number = flight_number
        self.destination = destination
        self.departure_time = departure_time

    def get_flight_number(self):
        return self.flight_number

    def get_destination(self):
        return self.destination

    def get_departure_time(self):
        return self.departure_time




class BoardingPass:
    def __init__(self, passenger, flight, gate):
        self.passenger = passenger
        self.flight = flight
        self.gate = gate

    def get_passenger(self):
        return self.passenger

    def get_flight(self):
        return self.flight

    def get_gate(self):
        return self.gate



class GateScanner:
    def __init__(self):
        pass

    def scan_boarding_pass(self, boarding_pass):
        pass

  # creating objects
passenger = Passenger(name="Ibraheim", booking_reference="ABC123", seat_number="23A")

ticketing_agent = TicketingAgent(name="Sara")

system = System()

flight = Flight(flight_number="XY123", destination="Italy", departure_time="2024-02-21 09:00")

system.add_flight(flight)

boarding_pass = BoardingPass(passenger=passenger, flight=flight, gate="A1")
passenger.set_boarding_pass(boarding_pass)
gate_scanner = GateScanner()
gate_scanner.scan_boarding_pass(boarding_pass)

print("Passenger Name:", passenger.get_name())
print("Flight Number:", boarding_pass.get_flight().get_flight_number())
print("Destination:", boarding_pass.get_flight().get_destination())
print("Departure Time:", boarding_pass.get_flight().get_departure_time())
print("Seat Number:", passenger.get_seat_number())
print("Gate:", boarding_pass.get_gate())
