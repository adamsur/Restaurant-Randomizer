from GUI import selectorGUI
from GUI import choiceGUI

def main():
    food, foodList = selectorGUI()

    while True:
        food = choiceGUI(food, foodList)

if __name__ == "__main__":
    main()
