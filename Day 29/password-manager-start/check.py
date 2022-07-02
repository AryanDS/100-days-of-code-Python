import json
import collections

json1={
    "Facebook": {
        "email": "aryansaini117@gmail.com",
        "password": "1NGFk(6ZorRj*"
    }
}

# print(json1["Facebook"]["email"])


with open("/Users/aryansaini/Documents/Visual Studio Code/100 days of code/100-days-of-code-Python/Day 29/pass_data.json", "r") as file:
    website_entry ="Facebook"
    #loading the json object into a dictionary 
    json_dict=  json.load(file)
    for key in json_dict.keys():
            if website_entry == key:
                print(website_entry, key)
                print(json_dict[key]['email'])
         
        
        # for k,v in j.items():
        #     print(k)
