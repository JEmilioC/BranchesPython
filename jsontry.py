import json

with open('ej.json') as jsonEscuela:
    data=json.load(jsonEscuela)

print(data['Escuela'])

data_string=json.dumps(data)
print (data_string)
decoded= json.loads(data_string)
print (decoded)
# print (str(decoded["Escuela"[1]["Verduras"][0]["Cantidad"]+"Alumnos."]))
