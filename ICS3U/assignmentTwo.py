#-----------------------------------------------------------------------------
# Name:        Assignment 2 Reassessment  - Zookeeper Andy (main.py)
# Purpose:     Manage and upkeep a Zoo
#
# Author:      Andy Zhang
# Created:     2021-02-01
# Updated:     2021-02-01
#-----------------------------------------------------------------------------
 
# Copy your Assignment 2 code here.  Remove the documentation of Assignment 1 improvements.
 
# If you wish to have Assignment 2 criteria re-assessed, place the required documention (see instructions) here.  Line numbers MUST be accurate for re-assessment.
 
'''
Mistakes from last Assignment
 
In the future - your clearScreen() function is really annoying.  I'd like to see what's happening.
 
7) I'm able to enter a negative number of animals - that should be raised.
 
8) Documentation is good, but consider adding another function so you can "exceed".
 
9) Same as above.
 
-----------------------------------------------------------------------------------------
Fixes for Assignment 2
 
clearScreen() is removed
 
7) Lines 110-112, added exceptions if the amount is negative and updates the documentation for it
 
8) Lines 121-143, added a new functon(0ffSpring()) and the additonal documenation
 
9) Lines 178-182, added more assertions for the new function aswell
 
 
 
 
'''
#This LINE STARTS ON THE 40th
 
import logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
 
#logging.disable(logging.error)
 
logging.info("Start of Program")
 
animalList = ["monkey", "lion", "elephant", "giraffe", "penguin", "polarbear", "panda", "koala", "gorilla", "hippo"]
animalCost = [300, 700, 550, 450, 300, 600, 1200, 400, 650, 500]
animalRevenue = [100, 250, 125, 150, 100, 200, 400, 125, 225, 175]
animalCount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
totalBudget = 1000
 
months = 0
profit = 0
 
def addAnimal(name, budget, amount):
 '''
 Add an animal from the given list
  Takes a animal name, and amount and checks to see if the budget can afford the animal(s). It then adds the animals to a list and returns the updated budget
 Parameters
 ----------
 name : str
   name of the animal in the given list(10 types)
 budget : int
   the budget of the zookeeper, what he can spend
 amount : int
   how many animal(s) the zookeeper is buying
  Returns
 -------
 int
   the updated budget value; how much credits are left after buying the new animals
  Warnings (this section is optional)
 --------
 None, but I don't want to remove it since the lines would change
 Raises (this section is only applicable if your function raises an exception)
 ------
 TypeError
   values are not the correct types for the function to RuntimeError
 ValueError
   animal is not a registered animal in the selling list
 ValueError
   budget is too low for the function to add animal(s)
 ValueError
   amount cannot be negative
 '''
 logging.info("addAnimal() begins with " + name + " name " + str(budget) + " budget " + str(amount) + " amount")
 
 #lowers all string values to make comparisions easier
 lowerCase = name.lower()
 #stores index value of specified animal
 tempIndex = animalList.index(lowerCase)
 #checks parameter type
 if not isinstance(lowerCase, str) or not isinstance(budget, int) or not isinstance(amount, int):
   logging.error("addAnimal() | values are not the correct type for function to continue")
   raise TypeError("values are not the correct type for function to continue")
 #checks parameter value 
 if lowerCase not in animalList:
   logging.error("addAnimal() | " + str(lowerCase) + "is not a animal in the list given")
   raise ValueError(lowerCase, "is not a animal in the list given")
 if budget < animalCost[tempIndex] * amount:
   logging.error("addAnimal() | " + "budget to low to add animal to zoo")
   raise ValueError("budget to low to add animal to zoo")
 if amount < 0:
   logging.error("addAnimal() | " + "amount of animals cannot be negative")
   raise ValueError("amount of animals cannot be negative")
 #add animal to list and returns the new budget which is subtracted by animal(s) price
 else:
   logging.debug("Parameter check complete for addAnimal()")
   budget -= animalCost[tempIndex] * amount
   animalCount[tempIndex] += amount
   logging.info("Returned budget as "+ str(budget))
   return(budget)
 
def offSpring(count):
 '''
 Detect animal population and create offspring
  Takes in the number of animals, finds how many pairs there can be and creates offsprings of those respective animals
 Parameters
 ----------
 count : int
   the number of animals there are
  Returns
 -------
 int
   the number of offsprings that can be created, if there are no pairs, it automatically returns zero
 Raises (this section is only applicable if your function raises an exception)
 ------
 TypeError
   the parameter is not an integer
 ValueError
   the parameter is less than 0
 '''
 logging.info("offSpring() begins with " + str(count) + " count ")
 #Stores the count variable in a another variable so we don't change the list
 temporaryCount = count
 
 if not isinstance(count, int):
   logging.error("offSpring() | values is not an int")
   raise TypeError("values is not an int")
 if count < 0:
   logging.error("offspring() | 'count' cannot be negative")
   raise ValueError("'count' cannot be negative")
 else:
   logging.debug("Parameter check complete for offSpring()")
   #if an offspring can even be created(2 animals)
   if count >= 2:
     #finds the remainder when divided by 2
     remainder = temporaryCount % 2
     #subtracts the remainder from the count and divides it by 2 to find the number of sets of animals there are.
     setsOfAnimals = round((temporaryCount - remainder) / 2)
     logging.info("Returned offsprings as "+ str(setsOfAnimals))
     return (setsOfAnimals)
   else:
     logging.info("no offsprings created")
     return (0)
 
#assertions
#assertions are commented out to not flood the log file
 
# assert addAnimal("monkey", 1000, 3) == 100, "1000 - 300*3 = 100"
# assert addAnimal("panda", 2400, 2) == 0, "2400 - 1200*2 = 0"
# assert addAnimal("hippo", 1400, 2) == 400, "1400 - 500*2 = 400"
# assert addAnimal("elephant", 1650, 3) == 0, "1650 - 550*3 = 0"
# assert addAnimal("giraffe", 5000, 6) == 2300, "5000 - 450*6 = 2300"
 
# assert offSpring(11) == 5, "(11 - (11%2)) / 2 = 5"
# assert offSpring(0) == 0,  "value is less than 2, 0 offsprings can be created"
# assert offSpring(13) == 6, "(13 - (13%2)) / 2 = 6"
# assert offSpring(25) == 12, "(25 - (25%2)) / 2 = 12"
# assert offSpring(37) == 18, "(37 - (11%2)) / 2 = 18"
 
#main code
print("Welcome to the Zoo! As the Zookeeper, you will be managing our budget and adding more animals\n")
 
print("We currently have no animals but you have 1000 credits to spend in order to start bringing revenue to the Zoo!\n")
 
print("Revenue is calculated per month, and you can purchase more animals each month aswell\n")
 
#loop to keep code running forever so the Zoo can run
while(True):
 #Cyclomatic Capacity reached, didn't know how I can fix it but I think its because of the looping
 print("Here are the animals we can acquire, their prices and their revenue per month\n")
 #for loop to print the pre-stored animal list with cost and revenue values
 for x in range(0, len(animalList)):
   print("Name:", animalList[x], "|| Cost:", animalCost[x], "|| Revenue:", animalRevenue[x])
 #tries each line and moves on with success
 try:
   #requests zookeeper input for what and how many animals to buy
   logging.debug("Asks zookeeper to select a animal and the amount they want to buy")
   selectedAnimal = input("\nWhat animal do you wish to add to the Zoo? ")
   animalAmount = int(input("How many? "))
   #budget updated by the function
   logging.info("Function started with " + str(selectedAnimal) + " budget of " + str(totalBudget) + " amount of " + str(animalAmount))
   totalBudget = addAnimal(selectedAnimal, totalBudget, animalAmount)
   #refreshs the screen
 
 #different errors for the 2 inputs(selectedAnimal, animalAmount)
 except TypeError as e:
   logging.error("addAnimal() | " + str(e))
   print("TypeError, " + str(e), "\nTry again\n")
 except ValueError as e:
   logging.error("addAnimal() | " + str(e))
   print("ValueError, " + str(e), "\nTry again\n")
 except Exception as e:
   logging.error("addAnimal() | " + str(e))
   print("Error, " + str(e), "\nTry again\n")
 else:
   #if no errors happen, the else statement is run
   logging.info("No errors in first try segment, animal is added")
   #animal is added to the list and printed
   print("Added", animalAmount, selectedAnimal, "to the zoo, budget is now", totalBudget)
   print("--------------------------------------------------------------------\n")
   #see if budget is high enough to buy another animal
   try:
     if(totalBudget >= min(animalCost)):
       logging.debug("Asks zookeeper if he wants to acquire more animals if he can")
       userVal = input("Do you want to acquire more animals? Yes | No ")
       logging.info("zookeeper entered " + str(userVal))
       #if the answer is neither or incorrect value or type, the value is automatically changed to "no" and the code proceeds as normal
       if(userVal.lower() != "yes" and userVal.lower() != "no"):
         logging.info("ValueError, value is not 'Yes' or 'No', moving on as no")
         print("ValueError, value is not 'Yes' or 'No', moving on as no")
         userVal = "no"
   #additional errors for userVal input
   except TypeError as e:
     logging.error("addAnimal() | " + str(e))
     print("TypeError, " + str(e), "\nTry again\n")
   except ValueError as e:
     logging.error("addAnimal() | " + str(e))
     print("ValueError, " + str(e), "\nTry again\n")
   except Exception as e:
     logging.error("addAnimal() | " + str(e))
     print("Error, " + str(e), "\nTry again\n")
   else:
     #if no errors occur, proceed
     logging.debug("No errors from zookeeper selection, continuing to revenue statistics")
 
     if(totalBudget < min(animalCost) or userVal.lower() == "no"):
       #if no animals are being added, or the budget is too low to add another animal, proceed with end of month report
 
       #adds one month to the counter
       logging.info("month " + str(months))
       months += 1
       print("\nAfter month", months, "\n")
      
       #another for loop to print revenue statistics and calculate total profit for the month
 
       for x in range(0, len(animalList)):
         animalCount[x] += offSpring(animalCount[x])
         print(animalList[x], "created", offSpring(animalCount[x]), "offsprings" )
 
       print("\nYou currently have:\n")
       for x in range(0, len(animalList)):
         print(animalCount[x], animalList[x], "(s)", "generating", animalRevenue[x] * animalCount[x], "credits per month")
         profit += animalRevenue[x] * animalCount[x]  
       print("You have made a profit of", profit, "this month\n\n")
       logging.info("profit "+ str(profit))
       #add profit to budget
       totalBudget += profit
       logging.info("new totalBudget "+ str(totalBudget))
       profit = 0
       #starts next month with new budget and profit is reset to 0 for next month
       print("Your new budget for next month is", totalBudget, "credits\n")
     else:
       #zookeeper requests to add another animal within the same month, loop the program again with a different starting line
       logging.debug("zookeeper requested to buy another animal, loop is repeating once more")
       print("\nYour budget currently is", totalBudget, "Please select another animal to add\n")
 
 
    
   
    
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

