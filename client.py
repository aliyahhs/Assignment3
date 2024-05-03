from event import Event

class Client:
    '''Class to represent Client'''
    def __init__(self, clientID, name, address, contactDetails, budget):
        """Initialize a Company attributes"""
        self._clientID = clientID
        self._name = name
        self._address = address
        self._contactDetails = contactDetails
        self._budget = budget
        self._events = []  # This will hold a list of Event objects

    # Setter and Getter methods
    def get_clientID(self):
        return self._clientID

    def set_clientID(self, clientID = " "):
        self._clientID = clientID

    def get_name(self):
        return self._name

    def set_name(self, name = " "):
        self._name = name

    def get_address(self):
        return self._address

    def set_address(self, address = " "):
        self._address = address

    def get_contactDetails(self):
        return self._contactDetails

    def set_contactDetails(self, contactDetails = " "):
        self._contactDetails = contactDetails

    def get_budget(self):
        return self._budget

    def set_budget(self, budget = " "):
        self._budget = budget

    def get_events(self):
        return self._events

    def set_events(self, events):
        if isinstance(events, list):
            self._events = events
        else:
            raise ValueError("Events must be a list of Event objects")

    def add_event(self, event_id, event_name, event_date):
        # Create a new Event object and add it to the events list
        new_event = Event(event_id, event_name, event_date)
        self._events.append(new_event)

    def remove_event_by_id(self, event_id):
        # Remove an Event object by its ID from the events list
        self._events = [event for event in self._events if event.event_id != event_id]

    def __str__(self):
        return f"Client ID: {self._clientID}\nName: {self._name}\nAddress: {self._address}\nContact Details: {self._contactDetails}\nBudget: {self._budget}\nEvents: {[str(event) for event in self._events]}"
