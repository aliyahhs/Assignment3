import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import unittest

class EventManagementSystem:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("The Best Events Company")
        self.events = []
        self.employees = []
        self.venues = []
        self.suppliers = []
        self.guests = []
        self.clients = []

        self.create_widgets()

    def initialize_test_data(self):
        self.events.append(
            {"event_id": 11011, "event_type": "Conference", "event_theme": "Technology", "event_date": "2024-05-10",
             "event_time": "09:00", "event_duration": 3.5, "event_venue": "Convention Center"})
        self.employees.append(
            {"emp_id": 47899, "name": "Susan Mayers", "department": "Sales", "JobTitle": "Manager",
             "BasicSalary": 37500,
             "age": 35, "dateOfBirth": "1989-03-15", "passportDetails": "AE123456"})
        self.venues.append(
            {"venue_id": 18892, "name": "Convention Center", "location": "City Center", "minGuests": 100,
             "maxGuests": 500})
        self.suppliers.append(
            {"supplier_id": 76652, "name": "Catering Co.", "service": "Food and Beverage", "contact": "Salma j"})
        self.guests.append({"guest_id": 98726, "name": "Aliya", "contact": "123-456-7890", "contactDetails": "VIP"})
        self.clients.append(
            {"client_id": 67883, "name": "Adnoc Comp", "contact": "456-789-0123", "email": "aliya@gmail.com"})

    def create_widgets(self):
        # Create and pack all necessary widgets for the GUI
        tk.Label(self.root, text="ID:").pack()
        self.id_entry = tk.Entry(self.root)
        self.id_entry.pack()

        tk.Button(self.root, text="Display Event Details", command=lambda: self.display_details("event")).pack()
        tk.Button(self.root, text="Display Employee Details", command=lambda: self.display_details("employee")).pack()
        tk.Button(self.root, text="Display Venue Details", command=lambda: self.display_details("venue")).pack()
        tk.Button(self.root, text="Display Supplier Details", command=lambda: self.display_details("supplier")).pack()
        tk.Button(self.root, text="Display Guest Details", command=lambda: self.display_details("guest")).pack()
        tk.Button(self.root, text="Display Client Details", command=lambda: self.display_details("client")).pack()

    def display_details(self, entity_type):
        entity_id = int(self.id_entry.get())
        entity = None
        if entity_type == "event":
            entity = next((e for e in self.events if e["event_id"] == entity_id), None)
        elif entity_type == "employee":
            entity = next((e for e in self.employees if e["emp_id"] == entity_id), None)
        elif entity_type == "venue":
            entity = next((e for e in self.venues if e["venue_id"] == entity_id), None)
        elif entity_type == "supplier":
            entity = next((e for e in self.suppliers if e["supplier_id"] == entity_id), None)
        elif entity_type == "guest":
            entity = next((e for e in self.guests if e["guest_id"] == entity_id), None)
        elif entity_type == "client":
            entity = next((e for e in self.clients if e["client_id"] == entity_id), None)

        if entity:
            details = "\n".join([f"{key}: {value}" for key, value in entity.items()])
            messagebox.showinfo(f"{entity_type.capitalize()} Details", details)
        else:
            messagebox.showinfo("Not Found", f"No {entity_type} found with ID {entity_id}")

    def delete_entity(self, entity_type):
        entity_id = int(self.id_entry.get())
        deleted = False
        if entity_type == "event":
            for e in self.events:
                if e["event_id"] == entity_id:
                    self.events.remove(e)
                    deleted = True
                    break
        elif entity_type == "employee":
            for e in self.employees:
                if e["emp_id"] == entity_id:
                    self.employees.remove(e)
                    deleted = True
                    break
        elif entity_type == "venue":
            for e in self.venues:
                if e["venue_id"] == entity_id:
                    self.venues.remove(e)
                    deleted = True
                    break
        elif entity_type == "supplier":
            for e in self.suppliers:
                if e["supplier_id"] == entity_id:
                    self.suppliers.remove(e)
                    deleted = True
                    break
        elif entity_type == "guest":
            for e in self.guests:
                if e["guest_id"] == entity_id:
                    self.guests.remove(e)
                    deleted = True
                    break
        elif entity_type == "client":
            for e in self.clients:
                if e["client_id"] == entity_id:
                    self.clients.remove(e)
                    deleted = True
                    break

        if deleted:
            messagebox.showinfo("Success", f"{entity_type.capitalize()} deleted successfully!")
        else:
            messagebox.showinfo("Not Found", f"No {entity_type} found with ID {entity_id}")

    # CRUD operation methods for Employee
    def add_employee(self, entity_type):
        new_entity = {
            "emp_id": simpledialog.askinteger("Employee ID", "Enter employee ID:"),
            "name": simpledialog.askstring("Name", "Enter name:"),
            "department": simpledialog.askstring("Department", "Enter department:"),
            "JobTitle": simpledialog.askstring("Job Title", "Enter Job Title:"),
            "BasicSalary": simpledialog.askinteger("BasicSalary", "Enter BasicSalary:"),
            "age": simpledialog.askstring("Age", "Enter age:"),
            "dateOfBirth": simpledialog.askstring("Date of birth", "Enter Date of birth:"),
            "passportDetails": simpledialog.askstring("Passport Details", "Enter passport Details:")}
        self.employees.append(new_entity)
        messagebox.showinfo("Success", "Employee added successfully!")

    # CRUD operation methods for Event
    def add_event(self, entity_type):
        new_entity = {
            "event_id": simpledialog.askinteger("Event ID", "Enter event ID:"),
            "event_type": simpledialog.askstring("Event Type", "Enter event type:"),
            "event_theme": simpledialog.askstring("Event Theme", "Enter event theme:"),
            "event_date": simpledialog.askstring("Event Date", "Enter event date:"),
            "event_time": simpledialog.askstring("Event Time", "Enter event time:"),
            "event_duration": simpledialog.askfloat("Event Duration", "Enter event duration:"),
            "event_venue": simpledialog.askstring("Event Venue", "Enter event venue:")}
        self.events.append(new_entity)
        messagebox.showinfo("Success", "Event added successfully!")

    # CRUD operation methods for Venue
    def add_venue(self, entity_type):
        new_entity = {
            "venue_id": simpledialog.askinteger("Venue ID", "Enter venue ID:"),
            "name": simpledialog.askstring("Name", "Enter name:"),
            "location": simpledialog.askstring("Location", "Enter location:"),
            "minGuests": simpledialog.askinteger("Minimum Guests", "Enter Min Guests:"),
            "maxGuests": simpledialog.askinteger("Maximum Guests", "Enter Max Guests:")
        }
        self.venues.append(new_entity)
        messagebox.showinfo("Success", "Venue added successfully!")

    # CRUD operation methods for Supplier
    def add_supplier(self, entity_type):
        new_entity = {
            "supplier_id": simpledialog.askinteger("Supplier ID", "Enter supplier ID:"),
            "name": simpledialog.askstring("Name", "Enter name:"),
            "service": simpledialog.askstring("Service", "Enter service:"),
            "contact": simpledialog.askstring("Contact", "Enter contact:")
        }
        self.suppliers.append(new_entity)
        messagebox.showinfo("Success", "Supplier added successfully!")

    # CRUD operation methods for Guest
    def add_guest(self, entity_type):
        new_entity = {
            "guest_id": simpledialog.askinteger("Guest ID", "Enter guest ID:"),
            "name": simpledialog.askstring("Name", "Enter name:"),
            "contact": simpledialog.askstring("Contact", "Enter contact:"),
            "contactDetails": simpledialog.askinteger("Contact Details", "Enter Contact Details:")
        }
        self.guests.append(new_entity)
        messagebox.showinfo("Success", "Guest added successfully!")

    # CRUD operation methods for Client
    def add_client(self, entity_type):
        new_entity = {
            "client_id": simpledialog.askinteger("Client ID", "Enter client ID:"),
            "name": simpledialog.askstring("Name", "Enter name:"),
            "contact": simpledialog.askstring("Contact", "Enter contact:"),
            "email": simpledialog.askstring("Email", "Enter email:")
        }
        self.clients.append(new_entity)
        messagebox.showinfo("Success", "Client added successfully!")

    def modify_entity(self, entity_type):
        entity_id = int(self.id_entry.get())
        modified = False
        if entity_type == "event":
            for e in self.events:
                if e["event_id"] == entity_id:
                    new_entity = {}
                    new_entity["event_id"] = e["event_id"]
                    new_entity["event_type"] = simpledialog.askstring("Event Type", "Enter event type:",
                                                                      initialvalue=e["event_type"])
                    new_entity["event_theme"] = simpledialog.askstring("Event Theme", "Enter event theme:",
                                                                       initialvalue=e["event_theme"])
                    new_entity["event_date"] = simpledialog.askstring("Event Date", "Enter event date:",
                                                                      initialvalue=e["event_date"])
                    new_entity["event_time"] = simpledialog.askstring("Event Time", "Enter event time:",
                                                                      initialvalue=e["event_time"])
                    new_entity["event_duration"] = simpledialog.askfloat("Event Duration", "Enter event duration:",
                                                                         initialvalue=e["event_duration"])
                    new_entity["event_venue"] = simpledialog.askstring("Event Venue", "Enter event venue:",
                                                                       initialvalue=e["event_venue"])
                    self.events.remove(e)
                    self.events.append(new_entity)
                    modified = True
                    break
        elif entity_type == "employee":
            for e in self.employees:
                if e["emp_id"] == entity_id:
                    new_entity = {}
                    new_entity["emp_id"] = e["emp_id"]
                    new_entity["name"] = simpledialog.askstring("Name", "Enter name:", initialvalue=e["name"])
                    new_entity["department"] = simpledialog.askstring("Department", "Enter department:",
                                                                      initialvalue=e["department"])
                    new_entity["JobTitle"] = simpledialog.askstring("Job Title", "Enter job title:",
                                                                    initialvalue=e["JobTitle"])
                    new_entity["BasicSalary"] = simpledialog.askinteger("Basic Salary", "Enter basic salary:",
                                                                        initialvalue=e["BasicSalary"])
                    new_entity["age"] = simpledialog.askinteger("Age", "Enter age:", initialvalue=e["age"])
                    new_entity["dateOfBirth"] = simpledialog.askstring("Date of Birth", "Enter date of birth:",
                                                                       initialvalue=e["dateOfBirth"])
                    new_entity["passportDetails"] = simpledialog.askstring("Passport Details",
                                                                           "Enter passport details:",
                                                                           initialvalue=e["passportDetails"])
                    self.employees.remove(e)
                    self.employees.append(new_entity)
                    modified = True
                    break
        elif entity_type == "venue":
            for e in self.venues:
                if e["venue_id"] == entity_id:
                    new_entity = {}
                    new_entity["venue_id"] = e["venue_id"]
                    new_entity["name"] = simpledialog.askstring("Name", "Enter name:", initialvalue=e["name"])
                    new_entity["location"] = simpledialog.askstring("Location", "Enter location:",
                                                                    initialvalue=e["location"])
                    new_entity["minGuests"] = simpledialog.askinteger("Minimum Guests", "Enter minimum guests:",
                                                                      initialvalue=e["minGuests"])
                    new_entity["maxGuests"] = simpledialog.askinteger("Maximum Guests", "Enter maximum guests:",
                                                                      initialvalue=e["maxGuests"])
                    self.venues.remove(e)
                    self.venues.append(new_entity)
                    modified = True
                    break
        elif entity_type == "supplier":
            for e in self.suppliers:
                if e["supplier_id"] == entity_id:
                    new_entity = {}
                    new_entity["supplier_id"] = e["supplier_id"]
                    new_entity["name"] = simpledialog.askstring("Name", "Enter name:", initialvalue=e["name"])
                    new_entity["service"] = simpledialog.askstring("Service", "Enter service:",
                                                                   initialvalue=e["service"])
                    new_entity["contact"] = simpledialog.askstring("Contact", "Enter contact:",
                                                                   initialvalue=e["contact"])
                    self.suppliers.remove(e)
                    self.suppliers.append(new_entity)
                    modified = True
                    break
        elif entity_type == "guest":
            for e in self.guests:
                if e["guest_id"] == entity_id:
                    new_entity = {}
                    new_entity["guest_id"] = e["guest_id"]
                    new_entity["name"] = simpledialog.askstring("Name", "Enter name:", initialvalue=e["name"])
                    new_entity["contact"] = simpledialog.askstring("Contact", "Enter contact:",
                                                                   initialvalue=e["contact"])
                    new_entity["contactDetails"] = simpledialog.askstring("Contact Details", "Enter contact details:",
                                                                          initialvalue=e["contactDetails"])
                    self.guests.remove(e)
                    self.guests.append(new_entity)
                    modified = True
                    break
        elif entity_type == "client":
            for e in self.clients:
                if e["client_id"] == entity_id:
                    new_entity = {}
                    new_entity["client_id"] = e["client_id"]
                    new_entity["name"] = simpledialog.askstring("Name", "Enter name:", initialvalue=e["name"])
                    new_entity["contact"] = simpledialog.askstring("Contact", "Enter contact:",
                                                                   initialvalue=e["contact"])
                    new_entity["email"] = simpledialog.askstring("Email", "Enter email:", initialvalue=e["email"])
                    self.clients.remove(e)
                    self.clients.append(new_entity)
                    modified = True
                    break

        if not modified:
            messagebox.showinfo("Not Found", f"No {entity_type} found with ID {entity_id}")
        else:
            messagebox.showinfo("Success", f"{entity_type.capitalize()} modified successfully!")


# Test cases
class TestEventManagementSystem(unittest.TestCase):
    def setUp(self):
        self.app = EventManagementSystem()

    def test_display_event_details(self):
        self.app.id_entry.insert(0, "11011")
        self.app.display_details("event")

    def test_add_event(self):
        self.app.add_entity("event")

    def test_delete_event(self):
        self.app.id_entry.insert(0, "11011")
        self.app.delete_entity("event")

    def test_modify_event(self):
        self.app.id_entry.insert(0, "11011")
        self.app.modify_entity("event")

if __name__ == "__main__":
    unittest.main()
