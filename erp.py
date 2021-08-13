
employee = {}
while True:
    print("1.Add Employee")
    print("2.Delete Employee")
    print("3.Search Employee by name")
    print("4.Change Employee Data")
    print("5.Display Employee data : ")
    print("6.exit")
    choice = int(input("Enter your choice :"))

    if choice == 1:
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


    elif choice == 2:
        emp_id = input("\tEnter employee no :")
        if emp_id not in employee.keys():
            print("\twrong employee id")
        else:
            del employee[emp_id]
    
    elif choice == 3:
        name = input("\tEnter the name you want search :")
        flag = False
        for i in employee.values():
            if i["name"] == name:
                print(f"\t{i['name']} | {i['age']} | {i['gender']} | {i['place']} | {i['salary']} | {i['previous_company']} | {i['joining_date']} ")
                flag = True
                break
        if flag == False :
            print("\tNot found")
    elif choice == 4:
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
        elif choice == 2:
            emp_id = input("\tEnter employee id :")
            if emp_id not in employee.keys():
                print("\twrong employee no")
            else:
                employee[emp_id]['age'] = input("\tEnter new age")  
        elif choice == 3:
            emp_id = input("\tEnter employee id :")
            if emp_id not in employee.keys():
                print("\twrong employee no")
            else:
                employee[emp_id]['gender'] = input("\tEnter new gender")
        elif choice == 4:
            emp_id = input("\tEnter employee id :")
            if emp_id not in employee.keys():
                print("\twrong employee no")
            else:
                employee[emp_id]['salary'] = input("\tEnter new salary")

    elif choice == 5:
        for empid,employe in employee.items():
            print(f"\t{empid} | {employe['name']} | {employe['age']} | {employe['gender']} | {employe['place']} | {employe['salary']} | {employe['previous_company']} | {employe['joining_date']}")
            

    elif choice == 6:
        break;
    else:
        print("invalid choice")



