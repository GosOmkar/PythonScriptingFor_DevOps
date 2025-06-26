import requests

demo_url = "https://jsonplaceholder.typicode.com/posts" # this is demo url where we can jet some json data for a user

responce = requests.get(url=demo_url)

# here we only get the responce
print(f"Here we will get the responce from our demo url: {responce}")      

# here we get that what else we can do with the requests library
print(dir(responce))       

# display the json data from the url 
#print(responce.json())  

# display the type of our data that we get from our url
print(type(responce.json()))

""" As we get that our url that we got through the api is a list,
so to fetchg the 1st item we can use this
""" 
print(responce.json()[1])