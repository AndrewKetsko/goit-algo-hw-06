from name_class import Name
from phone_class import Phone


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones=[]

    # реалізація класу

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    def add_phone(self, phone_str:str)->None:
        phone=Phone(phone_str)
        if phone not in self.phones:
            self.phones.append(phone)

    def remove_phone(self, phone_str:str)->None:
        phone=Phone(phone_str)
        try:
            self.phones.remove(phone)
        except ValueError:
            pass

    def find_phone(self,phone_str:str)->Phone|None:
        phone=Phone(phone_str) 
        return phone_str if phone_str in [phone.value for phone in self.phones] else None

    def edit_phone(self, old_phone_str:str, new_phone_str:str)->None:
        old_phone=Phone(old_phone_str)
        new_phone=Phone(new_phone_str)
        index=[phone.value for phone in self.phones].index(old_phone_str) #raise ValueError if not found
        self.phones[index]=new_phone