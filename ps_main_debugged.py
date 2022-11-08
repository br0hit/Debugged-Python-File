#Print result after every function to check 
#Read the info in every functions to get the proper understanding of desired output

import json
from multiprocessing.sharedctypes import Value
filepaths='data.json'

def read_data(filepaths):
    with open(filepaths) as json_file:
      data = json.load(json_file)
    
    return data
    # Read data from filepaths

data = read_data(filepaths)

def get_oldest(data):
     max=0
     c=0
     oldest={}

     for i in data["AVENGERS"]:
        if (data["AVENGERS"][i]['age'] >max):
            max=data["AVENGERS"][i]['age']

     for i in data["AVENGERS"]:
        if data["AVENGERS"][i]['age'] == max:
            oldest[c]=data["AVENGERS"][i]
            c+=1        

     for i in data["DC"]:
        if (data["DC"][i]['age'] >max):
            max=data["DC"][i]['age']

     for i in data["DC"]:
        if data["DC"][i]['age'] == max:
            oldest[c]=data["DC"][i]
            c+=1
    # Return all info of the oldest superheroes
    # Return all info of the oldest superheroes
     return oldest

# returns info: Thor and Wonder Woman

# once we find the maximum age we need to search for that maximum age in the data and then store it 
# alternatively we can also keep changing the value every time the max changes ( But the above code looks more detailed so preferred)

# Printing the data

oldest=get_oldest(data)
print(oldest)

def get_oldest_avenger(data):
   max=0
   for i in data["AVENGERS"]:
        if (data["AVENGERS"][i]['age'] >max):
            max=data["AVENGERS"][i]['age']
            oldest_avenger=data["AVENGERS"][i]
    # Return all info of the oldest avenger
   return oldest_avenger

# returns info: Thor

# Error in the function: Too many variables were used in lines 40 and 42 of intital code,
# Since we only want the oldest 'avenger' the use of j for a secondary for loop was un-necessary

# Printing the data of the Oldest Avenger 
print(get_oldest_avenger(data))


def get_total_points(data):
    total_points={}
    for i in data["AVENGERS"]:
        key=data["AVENGERS"][i]["name"]
        total_points[key] = 0
        for j in data["AVENGERS"][i]['points']:
          total_points[key]+=data["AVENGERS"][i]['points'][j]
    for i in data["DC"]:
        key=data["DC"][i]["name"]
        total_points[key] = 0
        for j in data["DC"][i]['points']:
          total_points[key]+=data["DC"][i]['points'][j]
    # Return a dictionary
    # Key: superhero name
    # Value: total points
    return total_points

# returns info: Dict of superhero name and total points

# In line '57' of intial code DCU was used instead of DC

# Printing the total points of all the superheroes
total_points=get_total_points(data)

for i in data["AVENGERS"]:
        key=data["AVENGERS"][i]["name"]
        print(f"{key} : {total_points[key]}")
for i in data["DC"]:
        key=data["DC"][i]["name"]
        print(f"{key} : {total_points[key]}")


def get_more_than_average(data):
    more_than_average=[]
    avg_mcu=0
    avg_dc=0
    for i in data["AVENGERS"]:
        avg_mcu+=data["AVENGERS"][i]["points"]["stealth"]
    avg_mcu=avg_mcu/len(data["AVENGERS"])
    c=0
    for i in data["AVENGERS"]:
        if(data["AVENGERS"][i]['points']['stealth']>avg_mcu):
            more_than_average.insert(c,data["AVENGERS"][i])
            c+=1
    for i in data["DC"]:
      avg_dc+=data["DC"][i]['points']['strength']
    avg_dc=avg_dc/len(data["DC"])
    for i in data["DC"]:
        if(data["DC"][i]['points']['strength']>avg_dc):
            more_than_average.insert(c,data["DC"][i])
            c+=1
    '''
    Return list of superheroes with stealth more than average in MCU 
    and list of superheroes with strength more than average in DCEU
    '''
    return more_than_average

  #returns info: Steve Rogers and Superman

# A tuple was used which is changed to list and then the elements were inserted

more_than_average = get_more_than_average(data)

print(more_than_average)


def get_names(data):
    names=[]
    temp=0
    for i in data["AVENGERS"]:
        names.insert(temp,data["AVENGERS"][i]["name"])
        temp+=1
    temp=0
    for i in data["DC"]:
        names.insert(temp,data["DC"][i]["name"])
        temp+=1
    # Return a list of superhero names
    return names

#returns a list 

# The insert function on line 99 and 101 of the original code requires 2 parameters where the first parameter indicates the index of the place where the data is going to be stored
# The string of name which is going to be stored was also wrongly indicated

# Storing and printing the list 

names=get_names(data)

print(names)








