import json
from studentData import StudentData
from employerData import EmployerData

with open('data.json') as f:
    data = dict(json.load(f))
    # print(data)

jfssData = []
microhardData = []

jfssReq = {
    "department": ["math", "science", "english", "music", "arts", "technology", "physed"],
    "maxDigits": 7,
    "domain": "@pdsb.net"
}


microhardReq = {
    "department": ["management", "hardware", "software", "maintenance"],
    "maxDigits": 8
}


def importJson():
    for items in data.values():
        if items["tag"] == "student":
            jfssData.append(StudentData(items, jfssReq))
        else:
            microhardData.append(EmployerData(items, microhardReq))


importJson()
microhardData[1].test()


newmicrohardData = microhardData[1].removeEmployee(microhardData)

newmicrohardData[1].test()
