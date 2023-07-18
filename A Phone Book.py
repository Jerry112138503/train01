def add(name,phone):
    dict1[name] = phone
    print("Added successfully!")
def find(search):
    print(dict1.get(search,"Doesn't exit!"))
def print_all():
    print(dict1)

dict1 = {"John":"0987-954321","Andrew":"0912-343531","Catherine":"0956-396471"}
command = input("Please enter the function you want (1)Add (2)Find (3)Show (-1)Exit : ")
while(command != '-1'):   
    if(command == '1'):
        name = input("Please enter name: ")
        phone = input("Please enter phone number: ")
        add(name,phone) 
        command = input("Please enter the function you want (1)Add (2)Find (3)Show (-1)Exit : ")
    elif(command == '2'):
        search = input("Please enter name: ")
        find(search)
        command = input("Please enter the function you want (1)Add (2)Find (3)Show (-1)Exit : ")
    elif(command == '3'):
        print_all()
        command = input("Please enter the function you want (1)Add (2)Find (3)Show (-1)Exit : ")
    else:
        print("Please enter again ...")
        command = input("Please enter the function you want (1)Add (2)Find (3)Show (-1)Exit : ")