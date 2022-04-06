import json
from urllib import response
from studentData import StudentData


with open('data.json') as f:
    data = dict(json.load(f))
    # print(data)


response = []


def importJson():
    for items in data.values():
        response.append(StudentData(
            items))


importJson()
print(response[1].returnFactors())
