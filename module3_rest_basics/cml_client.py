import os
import re
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class CmlClient:
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.token = None
        self.session = requests.Session()
        self.session.verify = False

    def _url(self,path):
        return f"{self.base_url}/api/v0/{path}"

    def login(self):
        url = self._url("authenticate")
        response = self.session.post(
            url,
            json={
                "username":self.username, 
                "password":self.password
                },
            timeout=10,
        )
        response.raise_for_status()
        self.token=response.json()
        self.session.headers.update({"Authorization": f"Bearer {self.token}"})
    
    def get_labs(self):
        response = self.session.get(self._url("labs"), timeout=10) 
        response.raise_for_status()
        return response.json()
   

    def get_lab(self, lab_id):
        response = self.session.get(self._url(f"labs/{lab_id}"),timeout =10)
        response.raise_for_status()
        return response.json()
        

if __name__ == "__main__":
    base = os.environ["CML_URL"]
    user = os.environ["CML_USER"]
    pw = os.environ["CML_PASS"]

    client = CmlClient(base,user,pw)
    client.login()

    labs = client.get_labs()
    for lab_id in labs:
        try:
            detail = client.get_lab(lab_id) #lab_id is the string you send. detail is the body CML sends back. you send 12345, CML responds with {"title": "HQ", "state":"up"}
            print(detail["lab_title"], detail["state"])
        except requests.exceptions.HTTPError as error: #storing error code as 'error'
            status = error.response.status_code
            if status in (400,404):
                print("Invalid lab ID", error.response.status_code)
            elif status == 401:
                client.login()
                try:
                    detail = client.get_lab(lab_id)
                    print(detail["lab_title"], detail["state"])
                except requests.exceptions.HTTPError as error:
                    print("not authorized still", error.response.status_code)
            
            else:
                print("request failed", status) 


#you send:  GET /api/v0/labs/this-lab-does-not-exist
#CML sends: 400 Bad Request
#get_lab:   raise_for_status() raises HTTPError
#           the return line never runs
#           detail is never created

    print(client.base_url)
    print("token length:", len(client.token))

    
   
