
# List in Python 

environments = ["dev", "prd", "test","stg"]
print(f"Here are the environments : {environments}")
print(f"1st index or the second env :{environments[1]}")

print(len(environments))                             # will print the length of the list


environments.append("basiton")                       # will append an element of the list at the end 
print(f"Here are the environments after appen :- {environments}")



# Dictionary in Python

devive_info = {

    "name": "Ubuntu-machine",
    "RAM": "8 GB",                     
    "CPU": 8,
    "IsItNew": False
    }

print(devive_info.get("name"))        # to get the value from a key called name
print(devive_info.get("RAM"))         # to get the value from a key called RAM
print(devive_info.get("CPU"))         # to get the value from a key called CPU
print(devive_info.get("IsItNew"))     # to get the value from a key called IsItNew

devive_info.update({"env": environments})  # so here we just added another item from in the dict from our last environment we created as a list using update
print(devive_info)



# Sets in Python

device_id = {1,2,3,4,5,12,14,15,23,2,2,3,33}
new_device_id = {1,2,3,7,9,11,16,19,20}
print(f"It will only show the unique id from device_Id: {device_id}")  
print(f"It will only show the unique id from new device Id: {new_device_id}")


print(device_id.union(new_device_id))           #it will just showe the  unique ids from the two different sets               
print(device_id.intersection(new_device_id))    #it will just showe the  unique common  ids from the two different sets 



# Typle in Python

days_of_week = ("sunday","Monday","Tuesday")
print(f"The days of week {days_of_week}")

