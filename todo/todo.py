import os

def show():
    for i in range(0,len(data)):
        text = data[i]['todo']
        status = data[i]['status']
        priority = data[i]['priority']
        if(data[i]['status'] == 'completed'):
            text = strike(data[i]['todo'])
        
        print(str(i+1) + "  |  " + text + "  |  " + status  + "  | " + priority)


def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result


def update(name):

    file = open("Files/" + name + ".txt", 'w')
        
    file.write("Imp Todo List \n")
    for i in data:
        text = i['todo']
        if(i['status'] == 'completed'):
            text = strike(i['todo'])
        prio = i['priority']
        file.write(priority[prio] + " " + text + "\n")
            
    file.close()

        
def read(name):
    data = open("Files/" + name  + ".txt", 'r').read()
    print(data)


def add():
    todo = input("enter todo name: ")

    priority = input("enter priority high / low / medium : ").lower()
    if(priority not in ['high','low','medium','none','' ]):
        print("Please select from given parameters")
        add()
    
    status = ''
    

    if(status == ''):
        status = 'pending'
    if(priority == ''):
        priority = 'none'

    record = {           
                'todo' : todo,
                'priority' : priority,
                'status' : status
        }

    data.append(record)
    update(name)
    print("Added Successfully")

def delete():
    show()

    try:
        title = int(input("which todo you want to remove : "))
        if(title < 1  or title > len(data)):
            raise Exception

    except:
        print("please provide numbers in given range")
        delete()
    
    del data[title - 1] 

    print("Deleted Successfully")
    update(name)
    

def mark_status():
    show()

    try:
        num = int(input("please select an option for changing the status : "))
        if(num < 1  or num > len(data)):
            raise Exception
        
    except:
        print("please provide numbers in given range")
        mark_status()

    num = num - 1
    status = input("enter status pending / completed : ").lower()
    if(status not in ['pending','completed','none','']):
        print("Please select from given parameters")
        mark_status()

    data[num]['status'] =  status 
    update(name)
    print("Updated successfully")

def search():

    key=input('enter keyword to search ')
    print('''   Priorities   
        high = !!!,
        medium :  !!,
        low :   !,
        none :     ''')
    key2 = strike(key)
    cmd = "grep {} Files/*.txt".format(key)
    cmd2 = "grep {} Files/*.txt".format(key2)
    os.system(cmd)
    os.system(cmd2)
# def search():
#     directory = 'Files'
 
#     string = input("Enter a string you want to search : ")
#     string2 = strike(string)
#     for filename in os.scandir(directory):
#         if filename.is_file():
#             name_for_search = filename.name[:-4]
#             data_search = new_data(name_for_search)
#             for i in data_search:
#                 if(string in i['todo'] or string2 in i['todo']):
#                     print(filename.name + '   ' + i['todo'])

def mark_prioriy():

    show()

    try:
        num = int(input("please select an option to change the priority : "))
        if(num < 1  or num > len(data)):
            raise Exception

    except:
        print("please provide numbers in given range")
        mark_prioriy()

    num = num - 1
    priority = input("enter priority high / medium / low: ").lower()
    if(priority not in ['high','medium','low','none','']):
        print("Please select from given parameters")

    data[num]['priority'] =  priority      
    
    update(name)
    print("Updated successfully")


def edit():
    show()

    try:
        num = int(input("please select an todo to edit : "))
        if(num < 1  or num > len(data)):
            raise Exception

    except:
        print("please provide numbers in given range")
        edit()

    num = num - 1
    todo = input('Give the todo : ')
    data[num]['todo'] =  todo 
    
    update(name)
    print("Updated successfully")

def getData():
    print(data)


def new_data(name):
    new = open("Files/" + name  + ".txt", 'r').readlines()
    new = new[1:]
    priority_decoder = {
    '!!!' : 'high',
    ' !!' : 'medium',
    '  !' : 'low',
    '   ' : 'none'
    }
    
    new_data = []
    for c in new:
        
        record['priority'] = priority_decoder[c[:3]]
        record['todo'] =  c.rstrip("\n").split(" ")[-1]
   
        if('\u0336' in record['todo']):
            record['status'] = 'completed'
        else:
            record['status'] = 'pending'
    
        new_data.append(record)
    
    return new_data



data = []
name = ''
record = {           
                'todo' : '',
                'priority' : '',
                'status' : ''
            }
        


priority = {
        'high' : '!!!',
        'medium' : ' !!',
        'low' : '  !',
        'none' : '   '
        }


if(not os.path.exists("Files")):
    os.makedirs("Files")


print("***********  Welcome to To-Do  ************")
print('Here you can add,delete,search,edit,provide priority and mark status of Your to-do Activities')
date = input("Please Enter date : ")
name = date

if(os.path.exists("Files/" + name + ".txt")): 
    data = new_data(name)

while(1):

    print("\nplease select and option")

    try:
        c = int(input('''        1. Add a todo
        2. Delete a todo
        3. Mark Status of Todo
        4. Search a todo
        5. Provide Priority to a todo
        6. Edit a todo
        7. Change the date
        8. Exit\n'''))

        if(c < 1 or c > 8):
            raise Exception

    except:
        print("Please provide numbers in the given range")
        continue

    if(c == 1):
        add()
    elif(c == 2):
        delete()
    elif(c == 3):
        mark_status()
    elif(c == 4):
        search()
    elif(c == 5):
        mark_prioriy()
    elif(c == 6):
        edit()
    elif(c == 7):
        name = input("Please Enter date : ")
        if(os.path.exists("Files/" + name + ".txt")): 
            data = new_data(name)

        continue   

    elif(c == 10):
        getData()
    elif(c == 8):
        exit()

