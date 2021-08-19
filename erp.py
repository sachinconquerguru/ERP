print("-------------------ERP-----------------")

from emp_store import employee
from emp_store import teams
from emp_store import organization

import organzation_emp as org
import teams_fun as team
import Employees as emp




def erp_menu():
    print("1.Add Employee")
    print("2.Delete Employee")
    print("3.Search Employee")
    print("4.Change Employee Data")
    print("5.Display Employee data : ")
    print("6.Manage all Teams ")
    print("7.Manage all organizations ")
    print("8.exit")



while True :
    
    erp_menu()
    ch = int(input("Enter the choice"))
    if ch == 1 :
        print("-----Add Employee-----")
        emp.add_employee_details()
    elif ch == 2 :
        print("-----Delete Employee------")
        emp.delete_employee()
    elif ch == 3:
        print("------Search Employee by name-----")
        emp.search_employee_name()
    elif ch == 4:
        print("------Change Employee Data-------")
        emp.change_employee_details()
    elif ch == 5:
        print("-------Display Employee data-----")
        emp.display_employee()
    elif ch == 6:
        print("--------Manage all Teams-----")
        team.managa_all_teams()
    elif ch == 7:
        org.manage_all_organiz()
    elif ch == 8:
        break;
    else:
        print("Invalid Choice")