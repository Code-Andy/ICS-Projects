import json
from studentData import StudentData
from employerData import EmployerData


with open('data.json') as f:
    data = dict(json.load(f))
    # print(data)

jfssData = []
microhardData = []


def importJson():
    for items in data.values():
        if items["tag"] == "student":
            jfssData.append(StudentData(items))
        else:
            microhardData.append(EmployerData(items))


importJson()
microhardData[1].userTrait()
