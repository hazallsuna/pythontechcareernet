import json
data={
    "name":"Hazal",
    "age":23,
    "city":"Kahramanmaraş"
}

with open("day2/data.json","w",encoding="utf-8") as file:
    json.dump(data,file,ensure_ascii=False,indent=4)
    
print("Data oluşturuldu")