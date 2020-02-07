
from cloudmesh.common.dotdict import dotdict

data ={
            "state_id":"AR",
            "state_name":"Arunachal Pradesh"
      }

data = dotdict(data)

if data.state_name.contains("A"):
   print(data.state_id)