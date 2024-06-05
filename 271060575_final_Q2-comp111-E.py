print("question 1")
class Property_info:
    def __init__(self,property_id,name,location,description,price_night,avail_status):
        self.property_id = property_id
        self.name = name
        self.location = location
        self.description = description
        self.price_night = price_night
        self.avail_status = avail_status
    def descrip(self):  
        print("enter description of the property : ")
        k = str(input())
        self.description = k
    def check_status(self):
        self.avail_status== "available"
class Property_list:
    def __init__(self):
        self.pro_list = []
    def add_property(self,pro_to_add):
        if pro_to_add not in self.pro_list :
            self.pro_list.append(pro_to_add)
            print("property has been added")
        else:
            print("property already exists in property list ")
    def remove_property(self,pro_to_remove):
        if pro_to_remove in self.pro_list:
            self.pro_list.remove(pro_to_remove)
        else:
            print("property does not exist")
    def display_list(self):
        for i in self.pro_list:
            return(i)       
class User:
    def __init__(self,name,age,gender,phone_num):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone_num = phone_num
class Guest(User):
    def __init__(self,name,age,gender,phone_num):
        super().__init__(name,age,gender,phone_num)  
    def display_guest(self):
        print("detail of guest is as follows: ") 
        print(self.name) 
        print(self.age)
        print(self.gender)
        print(self.phone_num)
class Host:
    def __init__(self,name,age,gender,post,phone_num,work_exp):
        super().__init__(name,age,gender,post,phone_num)
        self.work_exp = work_exp
        self.obj_property = Property_list()
        
    def menu(self):
        while True:
            print("welcome host")
            print("what would you like to do: ")
            print("1. propety list")
            print("2. add property")
            print("3. remove property ")
            choice = str(input("enter your choice: "))
            if choice == 1:
                return self.obj_property.display_list()
            if choice == 2:
                return self.obj_property.add_property()
            if choice == 3:
                return self.obj_property.remove_property()

class Booking_system:
    def __init__(self,id,property,guest,check_in,check_out,booking_status):
        self.id = id
        self.property = property
        self.guest = guest
        self.check_in = check_in
        self.check_out = check_out
        self.booking_status = "confirmed"
    def cancel_booking(self):
        self.booking_status = "unavailable"    





