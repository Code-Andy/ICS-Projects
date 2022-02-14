#-----------------------------------------------------------------------------
# Name:        Officer K(main.py)
# Purpose:     Displays the knowledge of everything we've learned so far(P1 Assignment)
#              Utilizing Ifs, Variables, Functions, Lists or Dictionaries, etc.
#
# Author:      Andy Zhang
# Created:     2020-12-17
# Updated:     2020-12-18
#-----------------------------------------------------------------------------
# Procrasinated too much. However, I finished early and I think I showed everything.
# Also changed topics because the bully one was too complex and needed to much dialogue
 
 
#function that checks the users input with other predetemined values
def checkResponse(inputValue, correctValue, secondaryValue, incorrectValue):
 #Only conversion that is really needed and I used, since using != automatically removes other data types and incorrect values from coversions.
 inputValue = inputValue.lower()
 #Find if value is a digit or integer
 if inputValue.isdigit():
   inputValue = int(inputValue)
 while inputValue != correctValue and inputValue != secondaryValue and inputValue!= incorrectValue:
     inputValue = input("Incorrect answer, please enter one of the given options ").lower()
     if inputValue.isdigit():
       inputValue = int(inputValue)
 clearScreen()
 if inputValue == correctValue:
   return True
 elif inputValue == incorrectValue:
   return False
 else:
   return "Alternative"
  
#function to display creditscore and its effects   
def checkCreditScore(name):
 name = str(name)
 if name in creditScore:
   print("Credit score of", creditScore[name])
   if creditScore[name] < 0:
     return "Bad Student"
   elif creditScore[name] < 10:
     return "Troublesome"
   else:
     return "Good Student"
 
#clears the screen with 100 lines, so you can't view your student id. forces people to go through other choices
def clearScreen():
 for x in range(0,100):
   print('\n')
 
#2 dictionaries that store info for students. However there's an error and the id for 2 students are the same
idList = {'Joe':568711, 'Bob': 562721, 'William':568721, 'Tyler': 568712, 'Andy':568712}
creditScore = {'Joe':40, 'Bob': -100, 'William':0, 'Tyler': -80, 'Andy':50}
 
#Main Code
print("Your name is 'Andy' and new student at JFSS and your ID is '568712'. Remember This.")
 
checkResponse(input("Type 'Y' or 'y' to continue "), 'y', 'fill', 'fill')
 
clearScreen()
 
print("On a sunny afternoon, you're walking home from a normal day at school")
print("An officer approaches you")
print("1) Run away, 2) Talk to the officer")
 
dialogueOne = checkResponse(input("What would you do? "), 2, None, 1)
 
if dialogueOne == True:
 #scenario one
 print("Hi my name is Officer Kowalczewski, can I get your student number")
 print("1) 562721, 2) 568721, 3) 568712")
 
 dialogueTwo = checkResponse(input("What number was it? ") , 3, 2, 1)
 
 if dialogueTwo == True:
   #scenario one 3) Could've of made it less hard coded, but since it was a story I thought it would be fine
   print("*Officer K checks your information*")
   #This loop was from googling, However it was needed since I used dictionaries and there was no other way I found that worked(I intially used for x in idList and for x in idList.values()) but none of those worked.
   for x,y in idList.items():
     if y == 568712:
       studentName = x
   print(checkCreditScore(studentName),'\n')
 
   print("So, I see here that there is a compliant filed on your student number")
   print("But since you have a good credit score of", creditScore[studentName], "and you don't seem to be in this part of the school often, do you know anyone who could of done it?" )
   print("You - Umm I don't know, maybe Tyler? He has been here alot recently.\n")
 
   otherStudent = "Tyler"
 
   print("Mr.K walks away and checks on Tyler")
   print(checkCreditScore(otherStudent))
   print(otherStudent, "'s id", idList[otherStudent], studentName, "'s id", idList[studentName],'\n')
 
   print("So it seems there might of been a glitch for the student number")
   print("I also checked your attendance and you weren't in the school that day so it would not be you")
   print("But since you helped me I'll add a few points to you number and fix the typo")
   creditScore[studentName] = creditScore[studentName] + 10
   print("Creditscore has been updated to", creditScore[studentName])
   idList[otherStudent] = 567812
   print("Have a good day,", studentName)
 
 elif dialogueTwo == False:
    #scenario one 2) explained in 3)
   print("*Officer K checks your information*")
   for x,y in idList.items():
     if y == 562721:
       studentName = x
   print(checkCreditScore(studentName),'\n')
 
   print("Officer K realized that you had -100 points, meaning you deserve auto suspesnion, so he takes you to the office without questioning anything else thinking your the culprit. You waste a whole day finding out it was an error and now you can't finish your comp sci assignement for Mr.K")
 
 else:
    #scenario one 1) explained in 3)
   print("*Officer K checks your information*")
   for x,y in idList.items():
     if y == 568721:
       studentName = x
   print(checkCreditScore(studentName), '\n')
 
   print("Oh William, not again, the records say this is the fourth time, I'll just take 15 points away this time\n*Leaves*")
   creditScore["William"] +- 15
   print("You waste a whole day explaining how you did nothing wrong because William complained about losing points and now you can't finish your comp sci assignement for Mr.K")
 
else:
 #scenario two
 print("You flee, but Officer Kowalczewski uses his hidden 'stamina' to easily chase you, and bring you to the school office. You waste a whole day finding out it was an error and now you can't finish your comp sci assignement for Mr.K")