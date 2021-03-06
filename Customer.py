class Customer:
    def __init__(self, id, firstName, lastName, addressId):
        self.__id = id
        self.firstName = firstName
        self.lastName = lastName
        self.addressId = addressId

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        try:
            if id in range(1, 1000000):
                self.__id = id
            else:
                raise ValueError
        except ValueError:
            raise ValueError ("Enter a range of values from 1 to 1 000 000")

    
    def __str__(self):
        return f" - ID customer: {self.__id}, \n - First name: {self.firstName}, \n - Last name: {self.lastName}, \n - Adress Id: {self.addressId}"
    
    def __repr__(self):
       return self.__str__()


d = Customer(100000, "Jim", "Conor", 100)

d.id = 2000000000

print(d)

