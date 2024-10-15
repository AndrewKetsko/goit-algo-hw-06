from field_class import Field


class Phone(Field):
    def __init__(self, value):
        assert len(value)>=10, f'phone number must be greater than 10 digit'
        super().__init__(value)