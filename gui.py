import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class EventManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("The Best Events Company")
        self.events = []
        self.employees = []
        self.venues = []
        self.suppliers = []
        self.guests = []
        self.clients = []

        self.create_widgets()

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

        tk.Button(self.root, text="Add Event", command=lambda: self.add_event("event")).pack()
        tk.Button(self.root, text="Add Employee", command=lambda: self.add_employee("employee")).pack()
        tk.Button(self.root, text="Add Venue", command=lambda: self.add_venue("venue")).pack()
        tk.Button(self.root, text="Add Supplier", command=lambda: self.add_supplier("supplier")).pack()
        tk.Button(self.root, text="Add Guest", command=lambda: self.add_guest("guest")).pack()
        tk.Button(self.root, text="Add Client", command=lambda: self.add_client("client")).pack()

        tk.Button(self.root, text="Delete Event Details", command=lambda: self.delete_entity("event")).pack()
        tk.Button(self.root, text="Delete Employee Details", command=lambda: self.delete_entity("employee")).pack()
        tk.Button(self.root, text="Delete Venue Details", command=lambda: self.delete_entity("venue")).pack()
        tk.Button(self.root, text="Delete Supplier Details", command=lambda: self.delete_entity("supplier")).pack()
        tk.Button(self.root, text="Delete Guest Details", command=lambda: self.delete_entity("guest")).pack()
        tk.Button(self.root, text="Delete Client Details", command=lambda: self.delete_entity("client")).pack()

        tk.Button(self.root, text="Modify Event Details", command=lambda: self.modify_entity("event")).pack()
        tk.Button(self.root, text="Modify Employee Details", command=lambda: self.modify_entity("employee")).pack()
        tk.Button(self.root, text="Modify Venue Details", command=lambda: self.modify_entity("venue")).pack()
        tk.Button(self.root, text="Modify Supplier Details", command=lambda: self.modify_entity("supplier")).pack()
        tk.Button(self.root, text="Modify Guest Details", command=lambda: self.modify_entity("guest")).pack()
        tk.Button(self.root, text="Modify Client Details", command=lambda: self.modify_entity("client")).pack()

    def modify_entity(self, entity_type):
        entity_id = int(self.id_entry.get())
        entity_index = None
        if entity_type == "event":
            entity_index, entity = next(((i, e) for i, e in enumerate(self.events) if e["event_id"] == entity_id),
                                        (None, None))
        elif entity_type == "employee":
            entity_index, entity = next(((i, e) for i, e in enumerate(self.employees) if e["emp_id"] == entity_id),
                                        (None, None))
        elif entity_type == "venue":
            entity_index, entity = next(((i, e) for i, e in enumerate(self.venues) if e["venue_id"] == entity_id),
                                        (None, None))
        elif entity_type == "supplier":
            entity_index, entity = next(((i, e) for i, e in enumerate(self.suppliers) if e["supplier_id"] == entity_id),
                                        (None, None))
        elif entity_type == "guest":
            entity_index, entity = next(((i, e) for i, e in enumerate(self.guests) if e["guest_id"] == entity_id),
                                        (None, None))
        elif entity_type == "client":
            entity_index, entity = next(((i, e) for i, e in enumerate(self.clients) if e["client_id"] == entity_id),
                                        (None, None))

        if entity is None:
            messagebox.showinfo("Not Found", f"No {entity_type} found with ID {entity_id}")
            return

        # Create a new window for modifying the entity
        modify_window = tk.Toplevel(self.root)
        modify_window.title(f"Modify {entity_type.capitalize()} Details")

        entry_dict = {}

        def modify():
            nonlocal entity
            modified_entity = {}
            for key in entity.keys():
                modified_entity[key] = entry_dict[key].get()
            # Update the entity in the list
            if entity_index is not None:
                if entity_type == "event":
                    self.events[entity_index] = modified_entity
                elif entity_type == "employee":
                    self.employees[entity_index] = modified_entity
                elif entity_type == "venue":
                    self.venues[entity_index] = modified_entity
                elif entity_type == "supplier":
                    self.suppliers[entity_index] = modified_entity
                elif entity_type == "guest":
                    self.guests[entity_index] = modified_entity
                elif entity_type == "client":
                    self.clients[entity_index] = modified_entity
            messagebox.showinfo("Success", f"{entity_type.capitalize()} modified successfully!")
            modify_window.destroy()

        def cancel():
            modify_window.destroy()

        # Display current details
        for key, value in entity.items():
            label = tk.Label(modify_window, text=key.capitalize())
            label.grid(column=0, row=list(entity.keys()).index(key))
            entry = tk.Entry(modify_window)
            entry.insert(0, str(value))
            entry.grid(column=1, row=list(entity.keys()).index(key))
            entry_dict[key] = entry

        tk.Button(modify_window, text="Modify", command=modify).grid(column=0, row=len(entity) + 1)
        tk.Button(modify_window, text="Cancel", command=cancel).grid(column=1, row=len(entity) + 1)

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
            "JobTitle" : simpledialog.askstring("Job Title", "Enter Job Title:"),
            "BasicSalary": simpledialog.askinteger("BasicSalary", "Enter BasicSalary:"),
            "age": simpledialog.askstring("Age", "Enter age:"),
            "dateOfBirth" : simpledialog.askstring("Date of birth", "Enter Date of birth:"),
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


if __name__ == "__main__":
    root = tk.Tk()
    app = EventManagementSystem(root)
    root.mainloop()