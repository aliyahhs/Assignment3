from event import Event

class Guest:
    """Class to represent a Guest who may attend multiple Events"""
    def __init__(self, guestID, name, address, contactDetails):
        """Initialize a Guest attributes"""
        self._guestID = guestID
        self._name = name
        self._address = address
        self._contactDetails = contactDetails
        self._events = []  # This will hold a list of Event objects

#setter and getter methods
    def get_guestID(self):
        return self._guestID

    def set_guestID(self, guestID = " "):
        self._guestID = guestID

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

    def add_event(self, event):
        if isinstance(event, Event):
            self._events.append(event)
        else:
            raise ValueError("The argument must be an Event object")

    def remove_event(self, event):
        if event in self._events:
            self._events.remove(event)

    def get_events(self):
        return self._events

    def __str__(self):
        event_details = '\n'.join(str(event) for event in self._events)
        return (f"Guest ID: {self._guestID}\nName: {self._name}\n"
                f"Address: {self._address}\nContact Details: {self._contactDetails}\n"
                f"Events:\n{event_details}")
