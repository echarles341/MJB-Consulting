# Application Programing Interface
from fastapi import FastAPI

app = FastAPI()

@app.get("/jsontestingdata_mjbconsulting.com")
def read_root():
    return {"Welcome 123 !!"}


# Example 2

#client_info = {
#    1: {
#        "Name": "Mirlande Coulois",
#        "Address": "245 St. Martin st",
#        "City": "Tucson",
#        "State" : "Arizona",
#        "Zip Code" : "11003"
#    }
#}

#@app.get("/client-info/{name}")
#def get_name(name: str = None):
#    return client_info[name]