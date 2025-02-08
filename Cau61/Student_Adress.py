class Address:
    def __init__(self, street, district, city, zipcode):
        self.street: str = street
        self.district: str = district
        self.city: str = city
        self.zipcode: str = zipcode

    def string_address(self):
        return f"{self.street}, {self.district}, {self.city}, {self.zipcode}"

class Student:
    def __init__(self, id, first_name, last_name, home_address, school_address=None):
        self.id: str = id
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.home_address: Address = home_address
        self.school_address: Address = school_address

    def string_student(self):
        return f"{self.id} {self.first_name} {self.last_name}\nHome address: {self.home_address}\nSchool address: {self.school_address}"

st = Student('123','Nguyen', 'Quynh', Address('No.9', 'HCMC', 'VN', '7000'))