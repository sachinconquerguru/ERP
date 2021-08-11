employee = []
while True:
    print("1.Add Employee")
    print("2.Delete Employee")
    print("3.Search Employee")
    print("4.Change Employee Data")
    print("5.Display Employee name : ")
    print("6.exit")
    choice = int(input("Enter your choice :"))

    if choice == 1:
        
        name = input("Enter name :")
        if name:
            employee.append(name)

    elif choice == 2:
        print(employee)
        print(" choose name from this ")
        name = input("Enter name to delete : ")
        employee.remove(name)
    
    elif choice == 3:
        name = input("Enter name you want to search :")
        if name in employee:
            print(name + " is in the employee list")
        else:
            print(name + " not in the employee list")

    elif choice == 4:
        name = input("Enter the name you want to change :")
        update_name= input("Enter the new name :")
        index1 = employee.index(name)
        employee[index1]=update_name
        
    elif choice == 5:
        for i in range(0,len(employee)):
            print(i+1,".",employee[i])
            

    elif choice == 6:
        break;
    else:
        print("invalid choice")



