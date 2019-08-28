# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:05:38 2019
Calculator Program

This program will prompt a user for input of 2 numbers and will process them
according to the user request.

Present the user with the options below:
    Add
    Subtract
    Multiply
    Divide

Once user makes selection, prompt user for input of 2 numbers.
Process the numbers according to selection and display output.
Prompt the user to go again or go to the main menu.

@author: Kyler
"""

def formatting():
    print("="*30)
    print("="*30)
    print(" ")
    
def menu():
    formatting()
    print("Calculator Application:")
    print("Please enter the number corresponding with the selection you'd like:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit the application")
    formatting()
    
def enterANumber():
    while True:
        try:
            userNumber = int(input("Enter a number: "))
            break
        except ValueError:
            print("\n This is not a number. Please enter a number.")
        
    return userNumber
    
    
def addition():
    #Adition
    print("Addition")
            
    firstNumber = enterANumber()
    secondNumber = enterANumber()
    answer = firstNumber+secondNumber
    print(firstNumber, "+", secondNumber, "=", answer )

def subtraction():
    #subtraction
    print("Subtraction")
    firstNumber = enterANumber()
    secondNumber = enterANumber()
    answer = firstNumber-secondNumber
    print(firstNumber, "-", secondNumber, "=", answer )
    
def multiplication():
    #multiplication
    print("Multiplication")
    firstNumber = enterANumber()
    secondNumber = enterANumber()
    answer = firstNumber*secondNumber
    print(firstNumber, "*", secondNumber, "=", answer )
    
def division():
    #division
    print("Division")
    firstNumber = enterANumber()
    secondNumber = enterANumber()
    answer = firstNumber/secondNumber
    print(firstNumber, "/", secondNumber, "=", answer )
    
    
#def askForRepeat():
#    print("1. Repeat \n 2. Main Menu")
#    repeatAnswer = int(input(enterANumber()))
#    return repeatAnswer

# MAIN
def main():

    menuLoopBool = True
    
    while (menuLoopBool == True):
        
        # Call the menu to show the user.
        menu()
        
        # Menu selection
        userInput = input("Enter your selection: ")
        if userInput == "1":
            #Addition
            addition()
            
        elif userInput == "2":
            #Subtraction
            subtraction()
            
        elif userInput == "3":
            #Multiplication
            multiplication()
            
        elif userInput == "4":
            #Division
            division()
            
        elif userInput == "5":
            #Exit
            menuLoopBool = False
            
            
        # User validation
        else: 
            #Repeat
            formatting()
            print("Invalid input. Please enter a number: ")
            menuLoopBool = True

    
# Call main
main()