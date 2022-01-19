import random
import sys
import time

#Add Restaurants based on prices here
cheapList = [] #Insert Cheap Restaurants Here
mediumList = [] #Insert Medium Priced Restaurants here
expensiveList = [] #Insert Expensive Restaurants here

def foodSelection(List):
    while True:
        try:
            choice = random.randint(0,len(List)-1)
            foodChoice = List[choice]
            List.pop(choice)
            return foodChoice

        except:
            sys.exit(0)