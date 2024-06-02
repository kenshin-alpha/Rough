import os
 
def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result

def new_data(name):
    new = open("Files/" + name  + ".txt", 'r').readlines()
    new = new[1:]
    priority_decoder = {
    '!!!' : 'high',
    ' !!' : 'medium',
    '  !' : 'low',
    '   ' : 'none'
    }
    record = {}
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

# assign directory
directory = 'Files'
 
# iterate over files in
# that directory
string = input("Enter a string you want to search : ")
string2 = strike(string)
for filename in os.scandir(directory):
    if filename.is_file():
        name = filename.name[:-4]

        data = new_data(name)

        for i in data:
 
            if(string in i['todo'] or string2 in i['todo']):
                print(filename.name + '   ' + i['todo'])

    #data = new_data(name)

    
