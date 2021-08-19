from employee_r import Employee
employee =[]


def erp_menu():
    print("1.Add Employee")
    print("2.Delete Employee")
    print("3.Search Employee")
    print("4.Display Employee data")
    print("5.Change Employee Data : ")
    print("6.Manage all Teams ")
    print("7.Manage all organizations ")
    print("8.exit")

def search_employee_all_menu():
    print("\t1.Search Employee name")
    print("\t2.Search Employee age")
    print("\t3.Search Employee salery")
    print("\t4.Search Employee gender")
    print("\t5.exit")    
def change_employee_details():
    print("1  .Change name")
    print("2  .change age")
    print("3  .Change gender")
    print("4  .change salary")
    print("5  .exit")
            

while True:
    erp_menu()
    ch = int(input("Enter your choice"))
    if ch == 1:
        emp_id = input("\tEnter employee id :")
        name = input("\tEnter name ")
        age = int(input("\tEnter age "))
        gender = input("\tEnter gender ")
        place = input("\tEnter place ")
        salary = int(input("\tEnter salary "))
        previous_company = input("\tEnter previous_company ")
        joining_date = input("\tEnter joining_date (in DD/MM/YYYY) :")
        emp_temp = Employee(emp_id,name,age,gender,place,salary,previous_company,joining_date)
        employee.append(emp_temp)

    elif ch == 2:
        emp_id = input("\tEnter employee id :")
        flag = False
        for i in employee:
            if emp_id == i.emp_id:
                flag = True
                employee.pop(employee.index(i))               
            else:
                print("wrong id ")


        
    elif ch == 3:


        search_employee_all_menu()
        while True:
            ch = int(input("\tenter your choice : "))
            if ch == 1:
                name = input("Enter name :")
                emp = list(filter(lambda a: a.name == name, employee))
                if len(emp) == 0: #not st #st
                    print("No student found")
                else:
                    for i in emp:
                        print(f"{i.name}")       
            elif ch == 2: 
                age = int(input("\tEnter the age to be search : "))
                emp = list(filter(lambda a: a.age == age, employee))
                if len(emp) == 0: 
                    print("No student found")
                else:
                    for i in emp:
                        print(f"{i.age}")
            elif ch == 3: 
                salary = int(input("\tEnter the salery to be search : "))
                emp = list(filter(lambda a: a.salary == salary, employee))
                if len(emp) == 0: 
                    print("No student found")
                else:
                    for i in emp:
                        print(f"{i.salary}") 
            elif ch == 4: 
                gender = input("\tEnter the gender to be search ::")
                emp = list(filter(lambda a: a.gender == gender, employee))
                if len(emp) == 0: 
                    print("No student found")
                else:
                    for i in emp:
                        print(f"{i.gender}")                                                  
            elif ch == 5:
                break;
            else:
                print("invalid choice")      
    elif ch == 4:
		#Display employe
        for i in employee:
            print(f"\t {i.name} | {i.age} | {i.gender} | {i.place} | {i.salary} | {i.previous_company} | {i.joining_date}")


    elif ch== 5:
        while True:

            change_employee_details()

            choice = int(input("\tenter your choice : "))

            if choice == 1:
                
                emp_id = input("\tEnter employee id :")
                emp_temp  = list(filter(lambda a: a.emp_id == emp_id,employee))
                emp_temp[0].set_name(input("Enter new name: "))


            elif choice == 2:
                emp_id = input("\tEnter employee id :")
                emp_temp  = list(filter(lambda a: a.emp_id == emp_id,employee))
                emp_temp[0].set_age(input("Enter new age: "))  
            elif choice == 3:
                emp_id = input("\tEnter employee id :")
                emp_temp  = list(filter(lambda a: a.emp_id == emp_id,employee))
                emp_temp[0].set_gender(input("Enter new gender: "))  
            elif choice == 4:
                emp_id = input("\tEnter employee id :")
                emp_temp  = list(filter(lambda a: a.emp_id == emp_id,employee))
                emp_temp[0].set_salary(input("Enter new salary: ")) 
            elif choice == 5:
                break;
            else:
                print("invalid choice ")



    elif ch == 6:
		
        pass
    elif ch == 8:
		#Exit
        break;
    else:
        print("Invalid Choice")
