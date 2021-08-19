from emp_store import employee
from emp_store import teams
from emp_store import organization


def add_employee_details():

    emp_id = input("\tEnter employee id :")
    if emp_id not in employee.keys():
        name = input("\tEnter name ")
        age = int(input("\tEnter age "))
        gender = input("\tEnter gender ")
        place = input("\tEnter place ")
        salary = int(input("\tEnter salary "))
        previous_company = input("\tEnter previous_company ")
        joining_date = input("\tEnter joining_date (in DD/MM/YYYY) :")
        temp ={
            "name":name,
            "age":age,
            "gender":gender,
            "place":place,
            "salary":salary,
            "previous_company":previous_company,
            "joining_date":joining_date
            }
        employee[emp_id] = temp
    else:
        print("employee id already taken ")

def delete_employee():

    emp_id = input("\tEnter employee no :")
    if emp_id not in employee.keys():
        print("\twrong employee id")
    else:
        del employee[emp_id]


def search_employee_all_menu():
    print("\t1.Search Employee name")
    print("\t2.Search Employee age")
    print("\t3.Search Employee salery")
    print("\t4.Search Employee gender")
    print("\t5.exit")
    
      

def search_employee_name():
    search_employee_all_menu()
    while True:
        ch = int(input("\ttenter your choice : "))
        if ch == 1:


            name = input("\tEnter the name you want search :")
            print(list(filter(lambda a: a["name"] == name,employee.values())))
        elif ch == 2:
            age = int(input("\tEnter the age to be search : "))
            print(list(filter(lambda a: a["age"] == age,employee.values())))
        elif ch == 3:
            salary = int(input("\tEnter the salery to be search : "))
            print(list(filter(lambda a: a["salary"] == salary,employee.values())))
        elif ch == 4:
            gender = input("\tEnter the gender to be search ::")
            print(list(filter(lambda a: a["gender"] == gender,employee.values())))
        elif ch == 5:
            break;
        else:
            print("invalid choice")
	



def change_employee_details():
    print("1  .Change name")
    print("2  .change age")
    print("3  .Change gender")
    print("4  .change salary")
    choice = int(input("/tenter your choice : "))

    if choice == 1:


        emp_id = input("\tEnter employee id :")
        if emp_id not in employee.keys():
            print("\twrong employee no")
        else:
            employee[emp_id]['name'] = input("\tEnter new name")  
    if choice == 2:
        emp_id = input("\tEnter employee id :")
        if emp_id not in employee.keys():
            print("\twrong employee no")
        else:
            employee[emp_id]['age'] = input("\tEnter new age")  
    if choice == 3:
        emp_id = input("\tEnter employee id :")
        if emp_id not in employee.keys():
            print("\twrong employee no")
        else:
            employee[emp_id]['gender'] = input("\tEnter new gender")
    if choice == 4:
        emp_id = input("\tEnter employee id :")
        if emp_id not in employee.keys():
            print("\twrong employee no")
        else:
            employee[emp_id]['salary'] = input("\tEnter new salary")
def display_employee():
    for empid,employe in employee.items():
        print(f"\t{empid} | {employe['name']} | {employe['age']} | {employe['gender']} | {employe['place']} | {employe['salary']} | {employe['previous_company']} | {employe['joining_date']}")

