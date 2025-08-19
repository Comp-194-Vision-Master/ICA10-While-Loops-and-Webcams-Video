""" ==============================================================================================
File: activ10.py
Author: Susan Fox
Date: Fall 2025

Contains functions to practice with while loops and processing video
==================================================================================================
"""

import cv2
import numpy as np

# -----------------------------------------------------------------------------------------------------------
# printEveryOther and printEveryFifth

def printEveryOther(x):
    while x >= 0:  # x is the loop variable
        print(x)
        x = x - 2
    # when indentation stops, while loop is over
    print("Done!")


# TODO: Put your definition of printEveryFifth here


# -----------------------------------------------------------------------------------------------------------
# squareUserNums

def squareUserNums():
    # Initialize loop variable
    userInp = input("Enter the next number (negative to quit): ")
    userNum = int(userInp)
    while userNum >= 0:
        print(userNum, "squared is", userNum ** 2)
        userInp = input("Enter the next number (negative to quit): ")
        userNum = int(userInp)


# -----------------------------------------------------------------------------------------------------------
# sumToN

def sumToN(topNum):
    """Takes in a number and computes and returns the sum of the numbers
    from zero to the input number."""
    currVal = 0  # the loop variable
    total = 0  # the accumulator variable
    while currVal < topNum:
        total = total + currVal  # add next value to accumulator
        currVal = currVal + 1  # update the loop variable
    return total

# TODO: Put your definition of addUserNums here

# -----------------------------------------------------------------------------------------------------------
# nextWord

def nextWord(text):
    """Takes in a string of text and builds and returns a new string
    that is the next "word" in the text. In other words, the next
    sequence of characters up to a space, tab, or newline."""
    wordStr = ""
    i = 0
    for ch in text:
        if ch in " \t\n":  # if character is space, tab (\t), or newline (\n)
            break
        else:
            wordStr = wordStr + ch
    return wordStr


# TODO: Put your copy of squareUserNums2 here


# -----------------------------------------------------------------------------------------------------------
# videoFeeder

# TODO: Modify this function as described in the activity

def videoFeeder(camOrFile=0):
    vidCap = cv2.VideoCapture(0)
    while True:
        ret, img = vidCap.read()  # Read a frame from the video camera
        cv2.imshow("Webcam", img)  # Display the frame
        cv2.waitKey(10)  # Wait 10 milliseconds and then go on

    vidCap.release()

# TODO: Add your definition of processImage here


# -----------------------------------------------------------------------------------------------------------
# Main script

if __name__ == "__main__":
    # ---------------------------------------------
    # Test calls for printEveryOther
    print("Testing printEveryOther")
    # TODO: Add calls to printEveryOther here

    # TODO: Add calls to printEveryFifth here

    # ---------------------------------------------
    # Test calls for squareUserNums
    print("Testing squareUserNums")
    squareUserNums()

    # ---------------------------------------------
    # Test calls for sumToN
    print("Testing sumToN")
    # TODO: Add calls to sumToN here

    # TODO: Add calls to addUserNums here

    # ---------------------------------------------
    # Test calls for nextWord
    print("Testing nextWord")
    # TODO: Add calls to nextWord here

    # TODO: Add calls to squareUserNums2 here

    # ---------------------------------------------
    # Test calls for videoFeeder
    print("Testing videoFeeder")
    videoFeeder()
