
from cloudmesh.common.dotdict import dotdict

data ={
            "state_id":"AR",
            "state_name":"Arunachal Pradesh"
      }

data = dotdict(data)

if data.state_name == ("Arunachal Pradesh"):
   print(data.state_id)
else:
    print("Not Found")