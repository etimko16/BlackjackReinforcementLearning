# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 21:30:30 2019

@author: brandon
"""

def main():
    sum = 0
    
    print("Here is your card: ", card) #draw card
    sum += card
    
    if sum < 21:
        print("Here is your sum: ", sum)
        move = input("Would you like to hit or stand? (Please enter H or S)")
        if move == 'H':
            #draw new card
            sum += card
        if move == 'S':
            print("You're total is: ", sum)
    if sum > 21:
        print("You're hand is too high and you lost. Here was your total: ", sum)
        