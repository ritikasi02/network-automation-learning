import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import os
import requests

#look up credentials 
url = os.environ["CML_URL"]
username = os.environ["CML_USER"]
password = os.environ["CML_PASS"]

#build login url 
login = f"{url}/api/v0/authenticate"

#POST request for providing credentials to login url
response = requests.post(login,json={"username":username, "password":password}, timeout=10, verify=False)

print(response.status_code)

#print login ok if status code of HTTP request is 200
if response.status_code == 200:
    print("login ok")
    token = response.json() #capture token
    print("token length", len(token)) #print token length
    #use GET request to fetch lab detail and provide authorization token as part of the header
    labs = requests.get(f"{url}/api/v0/labs", headers={"Authorization": f"Bearer {token}"}, timeout=10, verify=False)
    print (labs.status_code) #print status code
    print(labs.json()) #print lab IDs

