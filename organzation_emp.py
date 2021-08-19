

from emp_store import employee
from emp_store import teams
from emp_store import organization


def manage_organization():
    print("1.Add organization")
    print("2.edit organization")
    print("3.display organization")
    print("4.exit")

def manage_all_organiz():
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

