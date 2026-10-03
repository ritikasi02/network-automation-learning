import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/users",timeout=10) #get response from website

print(response.status_code) #print the status code

user = response.json() #put response from website into user in json format

deet = [] # create an empty list 
for entry in user: #loop over user that is just website repsonse in json format
    small = {      #create a small dict with few details
        "id": entry["id"],
        "name": entry["name"], 
        "city": entry["address"]["city"] #city is subset of address
        }
    deet.append(small) #keep adding dict to the deet list


with open("outputs/users_report.json", "w") as f:
    json.dump(deet, f, indent=2) #in an empty json file, open it as f, and dump deet list of dicts

with open("sample_responses/labs.json") as f:
    data = json.load(f) # from a pre-built jason, load it into data variable
    for lab in data["labs"]: #loop over one key "labs" that has 3 dicts
        if lab["state"] == "STARTED":
            print(lab["title"])
        else:
            continue







