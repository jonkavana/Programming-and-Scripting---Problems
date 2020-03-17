# creating a program with a menu
students = []

def displayMenu():
    print("MENU")
    print("\ta) Add Student")
    print("\tv) View Student")
    print("\tq) Quit")
    choice = input("Select One: ")
    return choice

def readModules():
    modules = []
    currentName = input("enter Module name (blank to end):")
    while currentName != '':
        module = {}
        module['name']=currentName
        module['grade'] = input("enter grade:")
        modules.append(module)

        currentName = input("enter next Module name (blank to end):")

    return modules

def doAdd():
    global students
    # print("in do add")
    student = {}
    student["name"] = input("Enter student name:")
    student["modules"] = readModules()
    students.append(student)
   
def displayModules(modules):
    print("\t\tname\tgrade")
    for module in modules:
        print("\t\t{}\t{}".format(module['name'], module['grade']))

def doView():
    print ("all students")
    for student in students:
        print ("\t{}".format(student['name']))
        displayModules(student['modules'])

#Main
choice = displayMenu()
while choice != 'q':
    if choice == 'a':
        doAdd()
    elif choice == 'v':
        doView()
    elif choice =='q':
        pass
    else:
        print("please select a, v or q")

    choice = displayMenu()
