class Event:
    '''Class to represent Event'''
    def __init__(self, eventID, eventType, theme, date, time, duration, venueAddr, client, guestList, caterComp, cleanCompany, decCompany, entertComp, furnComp, invoice):
        """Initialize a Company attributes"""
        self._eventID = eventID
        self._eventType = eventType
        self._theme = theme
        self._date = date
        self._time = time
        self._duration = duration
        self._venueAddr = venueAddr
        self._client = client
        self._guestList = guestList
        self._caterComp = caterComp
        self._cleanCompany = cleanCompany
        self._decCompany = decCompany
        self._entertComp = entertComp
        self._furnComp = furnComp
        self._invoice = invoice

#Setter and Getter methods
    def get_eventID(self):
        return self._eventID
    def set_eventID(self, eventID = " "):
        self._eventID = eventID

    def get_eventType(self):
        return self._eventType
    def set_eventType(self, eventType = " "):
        self._eventType = eventType

    def get_theme(self):
        return self._theme
    def set_theme(self, theme = " "):
        self._theme = theme

    def get_date(self):
        return self._date

    def set_date(self, date = " "):
        self._date = date
    def get_time(self):
        return self._time

    def set_time(self, time = " "):
        self._time = time
    def get_duration(self):
        return self._duration

    def set_duration(self, duration = " "):
        self._duration = duration
    def get_venueAddr(self):
        return self._venueAddr
    def set_venueAddr(self, venueAddr = " "):
        self._venueAddr = venueAddr

    def get_client(self):
        return self._client

    def set_client(self, client = " "):
        self._client = client

    def get_guestList(self):
        return self._guestList

    def set_guestList(self, guestList = " "):
        self._guestList = guestList

    def get_caterComp(self):
        return self._caterComp

    def set_caterComp(self, caterComp = " "):
        self._caterComp = caterComp

    def get_cleanCompany(self):
        return self._cleanCompany

    def set_cleanCompany(self, cleanCompany = " "):
        self._cleanCompany = cleanCompany

    def get_decCompany(self):
        return self._decCompany

    def set_decCompany(self, decCompany = " "):
        self._decCompany = decCompany

    def get_entertComp(self):
        return self._entertComp

    def set_entertComp(self, entertComp = " "):
        self._entertComp = entertComp

    def get_furnComp(self):
        return self._furnComp

    def set_furnComp(self, furnComp = " "):
        self._furnComp = furnComp

    def get_invoice(self):
        return self._invoice

    def set_invoice(self, invoice = " "):
        self._invoice = invoice

    def __str__(self):
        return f"Event ID: {self._eventID}\nEvent Type: {self._eventType}\nTheme: {self._theme}\nDate: {self._date}\nTime: {self._time}\nDuration: {self._duration}\nVenue Address: {self._venueAddr}\nClient: {self._client}\nGuest List: {self._guestList}\nCatering Company: {self._caterComp}\nCleaning Company: {self._cleanCompany}\nDecoration Company: {self._decCompany}\nEntertainment Company: {self._entertComp}\nFurniture Company: {self._furnComp}\nInvoice: {self._invoice}"
