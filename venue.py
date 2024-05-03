from event import Event
class Venue:
    """Class to represent a Venue associated with an Event"""
    def __init__(self, venueID, name, address, contact, minGuests, maxGuests):
        """Initialize a Venue attributes"""
        self._venueID = venueID
        self._name = name
        self._address = address
        self._contact = contact
        self._minGuests = minGuests
        self._maxGuests = maxGuests
        self._event = None  # This will hold the associated Event object

    #Setter and getter methods
    def get_venueID(self):
        return self._venueID

    def set_venueID(self, venueID = " "):
        self._venueID = venueID


    def get_name(self):
        return self._name

    def set_name(self, name = " "):
        self._name = name


    def get_address(self):
        return self._address

    def set_address(self, address = " "):
        self._address = address

    def get_contact(self):
        return self._contact

    def set_contact(self, contact = " "):
        self._contact = contact

    def get_minGuests(self):
        return self._minGuests

    def set_minGuests(self, minGuests = 0):
        self._minGuests = minGuests

    def get_maxGuests(self):
        return self._maxGuests

    def set_maxGuests(self, maxGuests = 0):
        self._maxGuests = maxGuests


    #Method to associate an Event object with this Venue
    def set_event(self, event):
        if isinstance(event, Event):
            self._event = event
        else:
            raise ValueError("The argument must be an Event object")

    #Method to disassociate the Event object from this Venue
    def remove_event(self):
        self._event = None

    #Method to get the associated Event object
    def get_event(self):
        return self._event

    def __str__(self):
        return f"Venue ID: {self._venueID}\nName: {self._name}\nAddress: {self._address}\nContact: {self._contact}\nMin Guests: {self._minGuests}\nMax Guests: {self._maxGuests}"
