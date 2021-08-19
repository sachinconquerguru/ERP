from emp_store import employee
from emp_store import teams
from emp_store import organization
from Employees import display_employee



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
