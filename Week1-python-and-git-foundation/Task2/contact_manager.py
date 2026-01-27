"""File-Based Contact Manager | Read/Write/Append operations"""

import json
import os

class ContactManager:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = {}
        self.load_contacts()
    
    def load_contacts(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as file:
                    self.contacts = json.load(file)
        except json.JSONDecodeError:
            self.contacts = {}
    
    def save_contacts(self):
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.contacts, file, indent=4)
            return True
        except Exception as e:
            print(f"Error saving: {e}")
            return False
    
    def add_contact(self, name, phone, email="", address=""):
        if name in self.contacts:
            print(f"Contact '{name}' already exists")
            return False
        
        self.contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        self.save_contacts()
        return True
    
    def update_contact(self, name, **fields):
        if name not in self.contacts:
            print(f"Contact '{name}' not found")
            return False
        
        for field, value in fields.items():
            if field in ["phone", "email", "address"]:
                self.contacts[name][field] = value
        
        self.save_contacts()
        return True
    
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            return True
        return False
    
    def search_contact(self, query):
        query = query.lower()
        results = []
        for name, info in self.contacts.items():
            if (query in name.lower() or 
                query in info.get("phone", "").lower() or 
                query in info.get("email", "").lower()):
                results.append({"name": name, **info})
        return results
    
    def display_all_contacts(self):
        for name, info in sorted(self.contacts.items()):
            print(f"\n{name}")
            print(f"  Phone: {info.get('phone', 'N/A')}")
            print(f"  Email: {info.get('email', 'N/A')}")

if __name__ == "__main__":
    manager = ContactManager()
    
    manager.add_contact("Ali", "5551234", "ali@email.com")
    
    print("All Contacts =-")
    manager.display_all_contacts()
    
    print("\nSearch Results =-")
    results = manager.search_contact("Ali")
    print(results)
