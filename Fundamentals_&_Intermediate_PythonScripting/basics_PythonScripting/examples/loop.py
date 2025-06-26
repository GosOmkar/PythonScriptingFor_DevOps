# This script will  check CPU usage for multiple server
# here we will use dictionary for storing the servers info

# dummy Server data store as a dictionary
Servers = {

    "aws-Server": 46,                 
    "azure-Server": 76.98,                     
    "GCP-Server": 54,                         #key - Servers name | values - CPU usages
    "RedHat-Server": 80,                      
    "Digital-Server": 85
} 

#loop through servers and check CPU usage

for server,cpu in Servers.items():
    print(f"\n checking {Servers}.....")
    if cpu < 65:
        print("CPU usage is nornal")
    elif cpu < 75 :
        print("CPu usage is moderate")
    else:
        print("CPU usage is high, Action Needed")


