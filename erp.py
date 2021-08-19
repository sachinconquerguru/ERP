print("-------------------ERP-----------------")
employee = {}
teams = {}
organization = {}


def erp_menu():
    print("1.Add Employee")
    print("2.Delete Employee")
    print("3.Search Employee")
    print("4.Change Employee Data")
    print("5.Display Employee data : ")
    print("6.Manage all Teams ")
    print("8.exit")
#    choice = int(input("Enter your choice :"))


def manage_organization():
    print("1.Add organization")
    print("2.edit organization")
    print("3.display organization")
    print("4.exit")



def manage_all_organization():
    manage_organization()
    while True:
        
        ch = int(input("\ttenter your choice : "))
        if ch == 1:

            emp_id= input("\tEnter your employee id :")
            if emp_id in employee.keys():

                org_name = input("\tEnter thr organization")
                org_email = input("\tEnter the organization email :")
                temp = {
                    "org_name":org_name,
                    "org_email":org_email

                    }
                organization[emp_id] = temp
            else:
                print("employee id is wrong ")
        elif ch == 2:
            emp_id = input("\tEnter employee no :")
            if emp_id not in employee.keys():
                print("\twrong employee id")
            else:
                organization[emp_id]['org_name'] = input("\tEnter the new organization name :")
                display_organization()

        elif ch == 3:
            display_organization()
        elif ch == 4:
            break;
        else:
            print("invalid choice")

        


def display_organization():
    for empid,org_details in organization.items():
        print(f"\t{empid} | {org_details['org_name']} | {org_details['org_email']} ")



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



def manage_all_teams_menu():
    print("\t1.Create team")
    print("\t2.Display team")
    print("\t3.Manage team(Particular)")
    print("\t4.Delete team")
    print("\t5.Exit")

def managa_all_teams():
    while True:
        manage_all_teams_menu()
        ch = int(input("\tEnter your choice "))
        if ch == 1:
            create_teams()
        elif ch == 2:
            display_teams()
        elif ch == 3:
            manage_teams()
        elif ch == 4:
            delete_teams()
        elif ch == 5:
            break
        else:
            print("\tInvalid choice")	

def create_teams():
    team_name = input("\tEnter team name ")
    teams[team_name] = []

def delete_teams():
    team_name = input("\tEnter team name ")
    if team_name in teams.keys():
        del teams[team_name]
        print("\tDeleted the teams")
    else:
        print("\tWrong teams name")

def display_teams():
    for key,value in teams.items():
        name_string = ""
        for i in value:
            name_string = name_string +"|"+employee[i]["name"]
        print(f"{key} => {name_string}")



def manage_teams_menu():
    print("\t1 . Add employee")
    print("\t2 . delete employee")
    print("\t3 . list employee")

def manage_teams():
    team_name = input("\tEnter team name : ")
    manage_teams_menu()
    ch = int(input("Enter your choice :"))
    if ch == 1:
        add_employee(team_name)
    elif ch == 2 :
        delete_employee_from_team(team_name)
    elif ch == 3:
        list_employees(team_name)
    else :
        print("\tInvalid choice")

def add_employee(team_name):
    display_employee()
    emp_id = input("\tEnter the employee id to add this team :")
    if emp_id in employee.keys():
        teams[team_name].append(emp_id)
    else:
        print("\tWrong employee id.")

def list_employees(team_name):
    name_string=""
    for i in teams[team_name]:
        name_string = name_string + "|"+i+"."+employee[i]["name"]
    print(f"{name_string}")


def delete_employee_from_team(team_name):
    list_employees(team_name)
    emp_id = input("\t\tEnter the emp id from list")
    if emp_id in teams[team_name]:
        teams[team_name].remove(emp_id)
    else:
        print("\t\tWrong employee id")




while True :
    manage_all_organization()
    erp_menu()
    ch = int(input("Enter the choice"))
    if ch == 1 :
        print("-----Add Employee-----")
        add_employee_details()
    elif ch == 2 :
        print("-----Delete Employee------")
        delete_employee()
    elif ch == 3:
        print("------Search Employee by name-----")
        search_employee_name()
    elif ch == 4:
        print("------Change Employee Data-------")
        change_employee_details()
    elif ch == 5:
        print("-------Display Employee data-----")
        display_employee()
    elif ch == 6:
        print("--------Manage all Teams-----")
        managa_all_teams()
    elif ch == 7:
        break;
    else:
        print("Invalid Choice")