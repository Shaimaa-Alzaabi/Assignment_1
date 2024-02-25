class Passenger:
    def __init__(self, name, booking_reference, seat_number): # Constructor method for Passenger class
        # Initialize attributes for passenger's name, booking reference, and seat number
        self.name = name
        self.booking_reference = booking_reference
        self.seat_number = seat_number
        self.boarding_pass = None # Initialize boarding_pass to None

    # Getter methods to get passenger details
    def get_name(self):
        return self.name

    def get_booking_reference(self):
        return self.booking_reference

    def get_seat_number(self):
        return self.seat_number

    # Setter and getter methods for boarding pass
    def set_boarding_pass(self, boarding_pass):
        self.boarding_pass = boarding_pass

    def get_boarding_pass(self):
        return self.boarding_pass




class TicketingAgent:
    def __init__(self, name): # Constructor method for TicketingAgent class
        # Initialize attribute for ticketing agent's name
        self.name = name

    def get_name(self): # Getter method to get ticketing agent's name
        return self.name




class System:
    def __init__(self):# Constructor method for class System
        # Initialize an empty list to store flights
        self.flights = []

    def add_flight(self, flight): # Method to add a flight to the system
        self.flights.append(flight)

    def get_flights(self): # Method to get all flights in the system
        return self.flights




class Flight:
    def __init__(self, flight_number, destination, departure_time):# Constructor method for Flight class
        # Initialize attributes for flight number, destination, and departure time
        self.flight_number = flight_number
        self.destination = destination
        self.departure_time = departure_time

    # Getter methods to retrieve flight details
    def get_flight_number(self):
        return self.flight_number

    def get_destination(self):
        return self.destination

    def get_departure_time(self):
        return self.departure_time




class BoardingPass:
    def __init__(self, passenger, flight, gate):# Constructor method for BoardingPass class
        # Initialize attributes for passenger, flight, and gate
        self.passenger = passenger
        self.flight = flight
        self.gate = gate

    # Getter methods to get boarding pass details
    def get_passenger(self):
        return self.passenger

    def get_flight(self):
        return self.flight

    def get_gate(self):
        return self.gate



class GateScanner:
    def __init__(self): # Constructor method for GateScanner class
        pass

    def scan_boarding_pass(self, boarding_pass): # Method to scan a boarding pass
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
