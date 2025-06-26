# This script checks if a server's CPU and memory usage is within healthy limits

# Dummy data (normally this will come from system commands)
cpu_usage = 82.4   # in percentage
free_memory = 1200  # in MB

# Check CPU health
if cpu_usage < 70:
    print("CPU Usage is Normal.")
elif cpu_usage < 85:
    print("CPU Usage is Moderate. Keep an eye.")
else:
    print(" High CPU Usage! Action needed!")

# Check Memory health
if free_memory > 2000:
    print("Memory is Healthy.")
elif free_memory > 1000:
    print("Memory is Moderate. Monitor it.")
else:
    print(" Low Memory! Clean up needed!")
