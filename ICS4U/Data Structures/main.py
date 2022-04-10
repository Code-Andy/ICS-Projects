import json
from studentData import StudentData
from employeeData import EmployerData

'''
Future To Do's

Use the class structure to implement searching algorithms for userresponse data
Find common patterns such as stress in departments etc.
This is for algorithms

'''

open('output.txt', 'w').close()


def writeToTxt(outputString):
    """Output data to txt file

    Args:
        outputString (string): Takes in return strings from the object list's functions and saves them in a txt file
    """
    with open('output.txt', 'a') as f:
        f.write(outputString)
        f.write("\n")


with open('studentData.json') as f:
    studentData = json.load(f)

with open('employeeData.json') as f:
    employeeData = json.load(f)

jfssData = []
microSoftData = []

jfssReq = {
    "department": ["math", "science", "english", "music", "arts", "technology", "physed"],
    "maxDigits": 7,
    "domain": "pdsb.net"
}


microSoftReq = {
    "department": ["management", "hardware", "software", "maintenance"],
    "maxDigits": 8
}

for items in studentData.values():
    jfssData.append(StudentData(items, jfssReq))

for items in employeeData.values():
    microSoftData.append(EmployerData(items, microSoftReq))


print(jfssData[1].studentInfo())
print(jfssData[1].sumOfFactors())
print(jfssData[1].returnAll())
jfssData[1].changeHomeroom('science')
writeToTxt(jfssData[1].studentInfo())
writeToTxt(jfssData[1].userTrait())

print(microSoftData[2].employeeInfo())
print(microSoftData[2].sumOfFactors())
print(microSoftData[2].returnAll())
microSoftData[1].changeDepartment('software')
writeToTxt(microSoftData[2].employeeInfo())
writeToTxt(microSoftData[2].userTrait())
