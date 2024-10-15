from collections import UserDict
from record_class import Record


class AddressBook(UserDict):

    def __str__(self):
        list=''
        for record in self.data.values():
            list+=f'{record.name}: {[record.value for record in record.phones]}\n'
        return list
    
    def add_record(self,record:Record)->None:
        self.data[record.name.value]=record

    def find(self,name:str)->Record|None:
       return self.data.get(name)
    
    def delete(self,name:str)->None|str:
        try:
            del self.data[name]
        except KeyError:
            return f'Name {name} is not in your phonebook'
