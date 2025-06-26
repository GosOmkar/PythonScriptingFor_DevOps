# Simulating retry logic with a while loop
# Let's say we retry SSH connection until successful or max retries hit

max_retries = 10
attempt = 1
connected = False

while attempt <= max_retries:
    print(f"Attempt {attempt}: Trying to connect to server...")

    # Simulating success on 3rd try
    if attempt == 3:
        print(" Connected successfully!")
        connected = True
        break
    else:
        print(" Connection failed. Retrying...")

    attempt += 1

if not connected:
    print(" All connection attempts failed. Alert the admin!")

