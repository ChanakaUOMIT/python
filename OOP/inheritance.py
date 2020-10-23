# parent class
class Anyone:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def display(self):
        print(self.firstName, self.lastName)


# object
myObj = Anyone("Mo", "Salah")
myObj.display()
