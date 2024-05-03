from event import Event

class Company:
    '''Class to represent Company'''
    def __init__(self, name, eventTypes, outsourcedServices, suppliers):
        """Initialize a Company attributes"""
        self._name = name
        self._eventTypes = eventTypes
        self._outsourcedServices = outsourcedServices
        self._suppliers = suppliers
        self._events = []  # This will hold a list of Event objects

    # Setter and getter methods
    def get_name(self):
        return self._name

    def set_name(self, name = " "):
        self._name = name

    def get_eventTypes(self):
        return self._eventTypes

    def set_eventTypes(self, eventTypes = " "):
        self._eventTypes = eventTypes

    def get_outsourcedServices(self):
        return self._outsourcedServices

    def set_outsourcedServices(self, outsourcedServices = " "):
        self._outsourcedServices = outsourcedServices

    def get_suppliers(self):
        return self._suppliers

    def set_suppliers(self, suppliers = " "):
        self._suppliers = suppliers

    def get_events(self):
        return self._events

    # Method to add an event to the company's list of events
    def add_event(self, eventID, eventType, theme, date, time, duration, venueAddr, guestList, caterComp, cleanComp, decComp, entertComp, furnComp, invoice):
        new_event = Event(eventID, eventType, theme, date, time, duration, venueAddr, self._name, guestList, caterComp, cleanComp, decComp, entertComp, furnComp, invoice)
        self._events.append(new_event)

    def __str__(self):
        return f"Company Name: {self._name}\nEvent Types: {self._eventTypes}\nOutsourced Services: {self._outsourcedServices}\nSuppliers: {self._suppliers}\nEvents: {[str(event) for event in self._events]}"
