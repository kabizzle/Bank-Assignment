class Customer:
    current_id = 000000
    
    def __init__(self, name):
        self.name = name
        self.id = self.create_id()

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def create_id(self):
        Customer.current_id += 1
        return Customer.current_id
