class Employee:
    def __init__(self, emp_id = 0, name = "", age = 0, gender = "",place = "",salary = 0,previous_company = "",joining_date = ""):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.gender = gender
        self.place = place
        self.salary = salary
        self.previous_company = previous_company
        self.joining_date = joining_date
    def set_name(self,name):
        self.name = name
        return "Name assigned Successfully"
    def set_age(self,age):
        self.age = age
        return "Age assigned Successfully"
    def set_gender(self,gender):
        self.gender = gender
        return "gender assigned Successfully"
    def set_place(self,place):
        self.place = place
        return "Age assigned Successfully"
    def set_salary(self,salary):
        self.salary = salary
        return "salary assigned Successfully"
    def set_previous_company(self,previous_company):
        self.previous_company = previous_company
        return "previous_company assigned Successfully" 
    def set_joining_date(self,joining_date):
        self.joining_date = joining_date
        return "joining_date assigned Successfully"                         