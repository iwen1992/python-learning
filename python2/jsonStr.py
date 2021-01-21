import json
json_str='{"name":"qiyue","age":18}'
print(type(json_str))
student = json.loads(json_str)
print(type(student)) 
print(student)
student1 = json.dumps(student)
print(type(student1))
print(student1)