import sys
from tkinter import font
import PySimpleGUI as sg
import Lists

#Sets color theme for all windows
sg.theme(new_theme="DarkBlue12")

def eventLoop(window, chooseAgainList=[]):
    
    while True:
        event, values = window.read() #Opens the GUI window passed through the parameter

#First three choices pick a random restaurant based on list selection to be returned to the GUI
        if event == "Cheap ($)":
            window.close()
            foodChoice = Lists.foodSelection(Lists.cheapList)
            chooseAgainList = Lists.cheapList
            return foodChoice, chooseAgainList
        elif event == "Medium ($$)":
            window.close()
            foodChoice = Lists.foodSelection(Lists.mediumList)
            chooseAgainList = Lists.mediumList
            return foodChoice, chooseAgainList
        elif event == "Expensive ($$$)":
            window.close()
            foodChoice = Lists.foodSelection(Lists.expensiveList)
            chooseAgainList = Lists.expensiveList
            return foodChoice, chooseAgainList

#Used with the choice GUI if a user wants to pick another restaurant or exit the program
        elif event == "Choose Again":
            window.close()
            foodChoice = Lists.foodSelection(chooseAgainList)
            return foodChoice
        elif event == "Cancel":
            window.close()
            sys.exit(0)

#First window that a user picks for cheap, medium, or expensive
def selectorGUI():

    layout = [
        [sg.Text(text="Would you like Cheap or Expensive Restuarants?\n\n", font=("OCR A Extended", "9", "bold"))],
        [sg.Button(button_text="Cheap ($)", button_color="#288818"), sg.Button(button_text="Medium ($$)", button_color="#34ab20"), 
        sg.Button(button_text="Expensive ($$$)", button_color="#3ac224")]
    ]

    window = sg.Window(title="Food Selector", size=(400, 150), layout=layout, element_justification="c", no_titlebar=True, grab_anywhere=True)

    food, foodList = eventLoop(window)
    return food, foodList

#Window that displays the random choice and allows to choose again or quit
def choiceGUI(food, foodList):

    layout2 = [
        [sg.Text(text="\n" + food + "\n", font=("OCR A Extended", "16", "bold"))],
        [sg.Button(button_text="Choose Again", button_color="#3ac224", auto_size_button=True), 
        sg.Button(button_text="Cancel", button_color="#c50f0a", auto_size_button=True)]
    ]

    window = sg.Window("Food Selector", size=(400, 150), layout=layout2, element_justification="c", no_titlebar=True, grab_anywhere=True)

    food = eventLoop(window, foodList)
    return food