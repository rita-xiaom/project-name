import json
json_str={"id":"1","name":"51zxw","password":"66666"}
print(json_str)

data=json.loads(json_str)
print(type(data))
print(data)
print(data['id'])
print(data['name'])

with open('data.json','w')as f:
    json.dump(data,f)

# with open('data.json','r') as f:
#     data=json.loads(f)
#     print(data)